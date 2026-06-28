"""Test Phase 1 Authentication Flow"""
import sys
import json

def test_auth():
    """Test the authentication system"""
    print("Testing OWLBAN GROUP Phase 1 Authentication...")
    
    # Test imports
    print("\n1. Testing imports...")
    try:
        from auth_lib import AuthManager, authenticate_user, create_user, verify_token
        print("   ✓ Auth library imports: OK")
    except ImportError as e:
        print(f"   ✗ Import failed: {e}")
        return False
    
    # Test creating a user
    print("\n2. Testing user registration...")
    try:
        from auth_lib import auth_manager
        success, message = auth_manager.create_user(
            email='testuser@owlban.com',
            username='testuser',
            password='TestPass123!',
            role='user',
            company='OWLBAN_GROUP',
            permissions=['read', 'write']
        )
        if success:
            print(f"   ✓ User creation: {message}")
        else:
            print(f"   ℹ User exists: {message}")
    except Exception as e:
        print(f"   ✗ User creation failed: {e}")
    
    # Test authentication
    print("\n3. Testing authentication...")
    try:
        success, message, user = authenticate_user('testuser@owlban.com', 'TestPass123!')
        if success:
            print(f"   ✓ Authentication: {message}")
            print(f"   ✓ User: {user.username} ({user.role})")
        else:
            print(f"   ✗ Authentication failed: {message}")
    except Exception as e:
        print(f"   ✗ Authentication failed: {e}")
    
    # Test token generation
    print("\n4. Testing JWT token generation...")
    try:
        if user:
            access_token, refresh_token = auth_manager.generate_tokens(user)
            print(f"   ✓ Access token: {access_token[:30]}...")
            print(f"   ✓ Refresh token: {refresh_token[:30]}...")
            
            # Verify token
            payload = verify_token(access_token)
            if payload:
                print(f"   ✓ Token verification: OK")
                print(f"   ✓ User from token: {payload.get('email')}")
            else:
                print(f"   ✗ Token verification failed")
    except Exception as e:
        print(f"   ✗ Token generation failed: {e}")
    
    # Test API server import
    print("\n5. Testing API server imports...")
    try:
        from api_server import fastapi_app, AUTH_AVAILABLE
        print(f"   ✓ API server: OK")
        print(f"   ✓ Auth available: {AUTH_AVAILABLE}")
    except ImportError as e:
        print(f"   ✗ API server import failed: {e}")
    
    print("\n" + "="*50)
    print("Phase 1 Authentication: READY FOR TESTING")
    print("="*50)
    print("\nTo test API endpoints:")
    print("1. Start API server: python api_server.py")
    print("2. Test register: POST /auth/register")
    print("3. Test login: POST /auth/login")
    print("4. Test /auth/me with Bearer token")
    
    return True

if __name__ == '__main__':
    test_auth()
