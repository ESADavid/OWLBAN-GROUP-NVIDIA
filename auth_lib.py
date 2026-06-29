"""
Unified Authentication Library for OWLBAN GROUP
Provides JWT-based authentication, password management, and session handling
"""

import secrets
import logging
import json
import os
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict

import jwt
import bcrypt

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class User:
    """User data structure"""
    id: str
    email: str
    username: str
    password_hash: str
    role: str
    company: str
    permissions: List[str]
    mfa_enabled: bool = False
    mfa_secret: Optional[str] = None
    created_at: Optional[datetime] = None
    last_login: Optional[datetime] = None
    login_attempts: int = 0
    locked_until: Optional[datetime] = None
    active: bool = True

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now(timezone.utc)

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        # Convert datetime objects to ISO strings
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        # Convert ISO strings back to datetime objects
        for key in ['created_at', 'last_login', 'locked_until']:
            if data.get(key) and isinstance(data[key], str):
                data[key] = datetime.fromisoformat(data[key])
        return cls(**data)

@dataclass
class Session:
    """Session data structure"""
    session_id: str
    user_id: str
    email: str
    role: str
    permissions: List[str]
    company: str
    created_at: datetime
    expires_at: datetime
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    active: bool = True

class AuthConfig:
    """Authentication configuration"""
    JWT_SECRET = os.getenv('JWT_SECRET', secrets.token_hex(32))
    JWT_REFRESH_SECRET = os.getenv('JWT_REFRESH_SECRET', secrets.token_hex(32))
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRE_MINUTES', '15'))
    JWT_REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRE_DAYS', '7'))

    PASSWORD_MIN_LENGTH = int(os.getenv('PASSWORD_MIN_LENGTH', '8'))
    PASSWORD_REQUIRE_UPPERCASE = os.getenv('PASSWORD_REQUIRE_UPPERCASE', 'true').lower() == 'true'
    PASSWORD_REQUIRE_LOWERCASE = os.getenv('PASSWORD_REQUIRE_LOWERCASE', 'true').lower() == 'true'
PASSWORD_REQUIRE_NUMBERS = os.getenv('PASSWORD_REQUIRE_NUMBERS', 'true').lower() == 'true'
    PASSWORD_REQUIRE_SPECIAL = os.getenv('PASSWORD_REQUIRE_SPECIAL', 'false').lower() == 'true'

    MAX_LOGIN_ATTEMPTS = int(os.getenv('MAX_LOGIN_ATTEMPTS', '5'))
    LOCKOUT_DURATION_MINUTES = int(os.getenv('LOCKOUT_DURATION_MINUTES', '15'))

    COMPANIES = ['OWLBAN_GROUP', 'OSCAR_BROOME', 'BLACKBOX_AI', 'NVIDIA_INTEGRATION']
    ROLES = ['admin', 'user', 'executive', 'developer', 'analyst']

@dataclass
class PasswordResetToken:
    """Password reset token data structure"""
    token: str
    email: str
    created_at: datetime
    expires_at: datetime
    used: bool = False

@dataclass
class CSRFToken:
    """CSRF token data structure"""
    token: str
    user_id: str
    created_at: datetime
    expires_at: datetime

class AuthManager:
    """Unified authentication manager for all OWLBAN GROUP systems"""

    def __init__(self, user_store_file: str = 'users.json', session_store_file: str = 'sessions.json'):
        self.config = AuthConfig()
        self.user_store_file = user_store_file
        self.session_store_file = session_store_file
        self.users: Dict[str, User] = {}
        self.sessions: Dict[str, Session] = {}
        self.password_reset_tokens: Dict[str, PasswordResetToken] = {}
        self.csrf_tokens: Dict[str, CSRFToken] = {}
        self._load_data()

        # Create default admin user if no users exist
        if not self.users:
            self._create_default_admin()

    def _load_data(self):
        """Load users and sessions from storage"""
        try:
            if os.path.exists(self.user_store_file):
                with open(self.user_store_file, 'r', encoding='utf-8') as f:
                    user_data = json.load(f)
                    self.users = {email: User.from_dict(data) for email, data in user_data.items()}
        except Exception as e:
            logger.error("Failed to load user data: %s", e)

        try:
            if os.path.exists(self.session_store_file):
                with open(self.session_store_file, 'r', encoding='utf-8') as f:
                    session_data = json.load(f)
                    self.sessions = {sid: Session(**data) for sid, data in session_data.items()}
        except Exception as e:
            logger.error("Failed to load session data: %s", e)

    def _save_data(self):
        """Save users and sessions to storage"""
        try:
            user_data = {email: user.to_dict() for email, user in self.users.items()}
            with open(self.user_store_file, 'w', encoding='utf-8') as f:
                json.dump(user_data, f, indent=2)
        except Exception as e:
            logger.error("Failed to save user data: %s", e)

        try:
            session_data = {sid: asdict(session) for sid, session in self.sessions.items()}
            # Convert datetime objects to ISO strings
            for data in session_data.values():
                for key in ['created_at', 'expires_at']:
                    if isinstance(data[key], datetime):
                        data[key] = data[key].isoformat()
            with open(self.session_store_file, 'w', encoding='utf-8') as f:
                json.dump(session_data, f, indent=2)
        except Exception as e:
            logger.error("Failed to save session data: %s", e)

    def _create_default_admin(self):
        """Create default admin user"""
        admin_user = User(
            id='admin-001',
            email='admin@owlban.com',
            username='admin',
            password_hash=bcrypt.hashpw('Admin2024!'.encode(), bcrypt.gensalt()).decode(),
            role='admin',
            company='OWLBAN_GROUP',
            permissions=['read', 'write', 'delete', 'admin', 'manage_users']
        )
        self.users[admin_user.email] = admin_user
        self._save_data()
        logger.info("Default admin user created")

    def validate_password_policy(self, password: str) -> Tuple[bool, str]:
        """Validate password against policy"""
        if len(password) < self.config.PASSWORD_MIN_LENGTH:
            return False, "Password must be at least %d characters long" % self.config.PASSWORD_MIN_LENGTH

        if self.config.PASSWORD_REQUIRE_UPPERCASE and not any(c.isupper() for c in password):
            return False, "Password must contain at least one uppercase letter"

        if self.config.PASSWORD_REQUIRE_LOWERCASE and not any(c.islower() for c in password):
            return False, "Password must contain at least one lowercase letter"

        if self.config.PASSWORD_REQUIRE_NUMBERS and not any(c.isdigit() for c in password):
            return False, "Password must contain at least one number"

        if self.config.PASSWORD_REQUIRE_SPECIAL and not any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password):
            return False, "Password must contain at least one special character"

        return True, "Password is valid"

    def hash_password(self, password: str) -> str:
        """Hash a password"""
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify_password(self, password: str, password_hash: str) -> bool:
        """Verify a password against its hash"""
        return bcrypt.checkpw(password.encode(), password_hash.encode())

    def create_user(self, email: str, username: str, password: str, role: str = 'user',
                company: str = 'OWLBAN_GROUP', permissions: Optional[List[str]] = None) -> Tuple[bool, str]:
        """Create a new user"""
        if email in self.users:
            return False, "User already exists"

        if role not in self.config.ROLES:
            return False, "Invalid role. Must be one of: %s" % ', '.join(self.config.ROLES)

        if company not in self.config.COMPANIES:
            return False, "Invalid company. Must be one of: %s" % ', '.join(self.config.COMPANIES)

        # Validate password
        valid, message = self.validate_password_policy(password)
        if not valid:
            return False, message

        if permissions is None:
            permissions = ['read']

        user = User(
            id="%s-%s" % (company.lower(), secrets.token_hex(4)),
            email=email,
            username=username,
            password_hash=self.hash_password(password),
            role=role,
            company=company,
            permissions=permissions
        )

        self.users[email] = user
        self._save_data()
        logger.info("User created: %s", email)
        return True, "User created successfully"

    def authenticate_user(self, email: str, password: str, ip_address: Optional[str] = None,
                         user_agent: Optional[str] = None) -> Tuple[bool, str, Optional[User]]:
        """Authenticate a user"""
        user = self.users.get(email)
        if not user:
            logger.warning("Login attempt for non-existent user: %s", email)
            return False, "Invalid credentials", None

        # Check if account is locked
        if user.locked_until and datetime.now(timezone.utc) < user.locked_until:
            return False, "Account is temporarily locked", None

        # Verify password
        if not self.verify_password(password, user.password_hash):
            user.login_attempts += 1
            if user.login_attempts >= self.config.MAX_LOGIN_ATTEMPTS:
                user.locked_until = datetime.now(timezone.utc) + timedelta(minutes=self.config.LOCKOUT_DURATION_MINUTES)
                logger.warning("Account locked for user: %s", email)
            self._save_data()
            logger.warning("Invalid password for user: %s", email)
            return False, "Invalid credentials", None

        # Reset login attempts on successful login
        user.login_attempts = 0
        user.locked_until = None
        user.last_login = datetime.now(timezone.utc)
        self._save_data()

        logger.info("Successful login for user: %s", email)
        return True, "Login successful", user

    def generate_tokens(self, user: User) -> Tuple[str, str]:
        """Generate access and refresh tokens"""
        now = datetime.now(timezone.utc)

        access_token_payload = {
            'user_id': user.id,
            'email': user.email,
            'username': user.username,
            'role': user.role,
            'company': user.company,
            'permissions': user.permissions,
            'type': 'access',
            'iat': int(now.timestamp()),
            'exp': int((now + timedelta(minutes=self.config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)).timestamp())
        }

        refresh_token_payload = {
            'user_id': user.id,
            'email': user.email,
            'type': 'refresh',
            'iat': int(now.timestamp()),
            'exp': int((now + timedelta(days=self.config.JWT_REFRESH_TOKEN_EXPIRE_DAYS)).timestamp())
        }

        access_token = jwt.encode(access_token_payload, self.config.JWT_SECRET, algorithm='HS256')
        refresh_token = jwt.encode(refresh_token_payload, self.config.JWT_REFRESH_SECRET, algorithm='HS256')

        return access_token, refresh_token

    def verify_access_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Verify an access token"""
        try:
            payload = jwt.decode(token, self.config.JWT_SECRET, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    def refresh_access_token(self, refresh_token: str) -> Optional[Tuple[str, str]]:
        """Refresh an access token using a refresh token"""
        try:
            payload = jwt.decode(refresh_token, self.config.JWT_REFRESH_SECRET, algorithms=['HS256'])
            if payload.get('type') != 'refresh':
                return None

            user = self.users.get(payload['email'])
            if not user:
                return None

            return self.generate_tokens(user)
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    def create_session(self, user: User, ip_address: Optional[str] = None, user_agent: Optional[str] = None) -> str:
        """Create a new session"""
        session_id = secrets.token_urlsafe(32)
        now = datetime.now(timezone.utc)

        session = Session(
            session_id=session_id,
            user_id=user.id,
            email=user.email,
            role=user.role,
            permissions=user.permissions,
            company=user.company,
            created_at=now,
            expires_at=now + timedelta(hours=24),  # Sessions last 24 hours
            ip_address=ip_address,
            user_agent=user_agent
)

        self.sessions[session_id] = session
        self._save_data()
        logger.info("Session created for user: %s", user.email)
        return session_id

    def verify_session(self, session_id: str) -> Optional[Session]:
        """Verify a session"""
        session = self.sessions.get(session_id)
        if not session or not session.active:
            return None

        if datetime.now(timezone.utc) > session.expires_at:
            session.active = False
            self._save_data()
            return None

        return session

    def destroy_session(self, session_id: str):
        """Destroy a session"""
        if session_id in self.sessions:
            self.sessions[session_id].active = False
            self._save_data()
            logger.info("Session destroyed: %s", session_id)

    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        return self.users.get(email)

    def update_user(self, email: str, updates: Dict[str, Any]) -> bool:
        """Update user information"""
        user = self.users.get(email)
        if not user:
            return False

        for key, value in updates.items():
            if hasattr(user, key):
                setattr(user, key, value)

        self._save_data()
        logger.info("User updated: %s", email)
        return True

    def delete_user(self, email: str) -> bool:
        """Delete a user"""
        if email in self.users:
            del self.users[email]
            self._save_data()
            logger.info("User deleted: %s", email)
            return True
        return False

    def list_users(self, company: Optional[str] = None) -> List[Dict[str, Any]]:
        """List all users, optionally filtered by company"""
        users = []
        for user in self.users.values():
            if company is None or user.company == company:
                user_dict = user.to_dict()
                # Remove sensitive information
                user_dict.pop('password_hash', None)
                users.append(user_dict)
        return users

    def cleanup_expired_sessions(self):
        """Clean up expired sessions"""
        now = datetime.now(timezone.utc)
        expired_sessions = []

        for session_id, session in self.sessions.items():
            if not session.active or now > session.expires_at:
                expired_sessions.append(session_id)

        for session_id in expired_sessions:
            del self.sessions[session_id]

        if expired_sessions:
            self._save_data()
            logger.info("Cleaned up %d expired sessions", len(expired_sessions))

    def request_password_reset(self, email: str) -> Tuple[bool, str]:
        """Request a password reset for a user"""
        user = self.users.get(email)
        if not user:
            # Return success even if user doesn't exist (security best practice)
            logger.info("Password reset requested for non-existent user: %s", email)
            return True, "If the email exists, a reset link will be sent"

# Generate reset token
        token = secrets.token_urlsafe(32)
        now = datetime.now(timezone.utc)
        
        reset_token = PasswordResetToken(
            token=token,
            email=email,
            created_at=now,
            expires_at=now + timedelta(hours=1),  # Token expires in 1 hour
            used=False
        )
        
        self.password_reset_tokens[token] = reset_token
        
        # In production, send email here
        logger.info("Password reset token generated for user: %s", email)
        logger.info("Password reset token (dev): %s", token)
        
        return True, "If the email exists, a reset link will be sent"

    def reset_password(self, email: str, reset_token: str, new_password: str) -> Tuple[bool, str]:
        """Reset password using a valid reset token"""
        # Validate new password
        valid, message = self.validate_password_policy(new_password)
        if not valid:
            return False, message

        # Find the reset token
        token_obj = self.password_reset_tokens.get(reset_token)
        if not token_obj:
            logger.warning("Invalid password reset token used")
            return False, "Invalid or expired reset token"

        # Check if token is valid
        if token_obj.used:
            logger.warning("Used password reset token attempted")
            return False, "Invalid or expired reset token"

        if datetime.now(timezone.utc) > token_obj.expires_at:
            logger.warning("Expired password reset token used")
            return False, "Invalid or expired reset token"

        # Verify email matches
        if token_obj.email != email:
            logger.warning("Email mismatch in password reset")
            return False, "Invalid or expired reset token"

        # Get user and update password
        user = self.users.get(email)
        if not user:
            return False, "User not found"

        user.password_hash = self.hash_password(new_password)
        user.login_attempts = 0
        user.locked_until = None
        
        # Mark token as used
        token_obj.used = True
        del self.password_reset_tokens[reset_token]

        self._save_data()
        logger.info("Password reset successful for user: %s", email)
        
        return True, "Password reset successful"

    def cleanup_expired_reset_tokens(self):
        """Clean up expired password reset tokens"""
        now = datetime.now(timezone.utc)
        expired_tokens = []

        for token, token_obj in self.password_reset_tokens.items():
            if token_obj.used or now > token_obj.expires_at:
                expired_tokens.append(token)

        for token in expired_tokens:
            del self.password_reset_tokens[token]

        if expired_tokens:
            logger.info("Cleaned up %d expired reset tokens", len(expired_tokens))

    def generate_csrf_token(self, user_id: str) -> str:
        """Generate a CSRF token for a user"""
        token = secrets.token_urlsafe(32)
        now = datetime.now(timezone.utc)

        csrf_token_obj = CSRFToken(
            token=token,
            user_id=user_id,
            created_at=now,
            expires_at=now + timedelta(hours=24)
        )

        self.csrf_tokens[token] = csrf_token_obj
        logger.info("CSRF token generated for user: %s", user_id)
        return token

    def verify_csrf_token(self, token: str, user_id: str) -> bool:
        """Verify a CSRF token"""
        token_obj = self.csrf_tokens.get(token)
        if not token_obj:
            logger.warning("Invalid CSRF token used")
            return False

        if datetime.now(timezone.utc) > token_obj.expires_at:
            logger.warning("Expired CSRF token used")
            return False

        if token_obj.user_id != user_id:
            logger.warning("User ID mismatch in CSRF token verification")
            return False

        return True

    def cleanup_expired_csrf_tokens(self):
        """Clean up expired CSRF tokens"""
        now = datetime.now(timezone.utc)
        expired_tokens = []

        for token, token_obj in self.csrf_tokens.items():
            if now > token_obj.expires_at:
                expired_tokens.append(token)

        for token in expired_tokens:
            del self.csrf_tokens[token]

        if expired_tokens:
            logger.info("Cleaned up %d expired CSRF tokens", len(expired_tokens))

# Global auth manager instance
auth_manager = AuthManager()

# Convenience functions
def authenticate_user(email: str, password: str, ip_address: Optional[str] = None, user_agent: Optional[str] = None):
    return auth_manager.authenticate_user(email, password, ip_address, user_agent)

def verify_token(token: str):
    return auth_manager.verify_access_token(token)

def create_user(email: str, username: str, password: str, role: str = 'user',
               company: str = 'OWLBAN_GROUP', permissions: Optional[List[str]] = None):
    return auth_manager.create_user(email, username, password, role, company, permissions)

def get_user_by_email(email: str):
    return auth_manager.get_user_by_email(email)

if __name__ == '__main__':
    # Test the auth system
    print("Testing OWLBAN GROUP Authentication System")

    # Create a test user
    success, message = create_user('test@owlban.com', 'testuser', 'TestPass123!', 'user', 'OWLBAN_GROUP')
    print("Create user: %s - %s" % (success, message))

    # Test authentication
    success, message, user = authenticate_user('test@owlban.com', 'TestPass123!')
    print("Authenticate: %s - %s" % (success, message))

    if user:
        # Generate tokens
        access_token, refresh_token = auth_manager.generate_tokens(user)
        print("Access token: %s..." % access_token[:20])
        print("Refresh token: %s..." % refresh_token[:20])

        # Verify token
        payload = verify_token(access_token)
        print("Token valid: %s" % (payload is not None))
        if payload:
            print("User from token: %s" % payload['email'])
