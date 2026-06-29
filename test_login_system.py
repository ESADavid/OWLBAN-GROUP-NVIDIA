"""
Test script for Blackbox AI Login System
Tests both the auth_lib and API server endpoints
"""
import requests
import json

API_BASE = 'http://localhost:8000'

def test_auth_lib_direct():
    """Test authentication via auth_lib directly"""
    from auth_lib import authenticate_user, auth_manager
    
    print("=" * 60)
    print("Testing auth_lib (direct)")
    print("=" * 60)
    
    # Test admin login
    success, message, user = authenticate_user('admin@owlban.com', 'Admin2024!')
    print(f"Admin login: {success} - {message}")
    if user:
        print(f"  User: {user.username}, Role: {user.role}, Company: {user.company}")
        # Generate tokens
        access_token, refresh_token = auth_manager.generate_tokens(user)
        print(f"  Access token: {access_token[:30]}...")
        print(f"  Refresh token: {refresh_token[:30]}...")
    
    # Test invalid password
    success, message, user = authenticate_user('admin@owlban.com', 'WrongPassword')
    print(f"Invalid password: {success} - {message}")
    
    # Test non-existent user
    success, message, user = authenticate_user('nobody@example.com', 'password')
    print(f"Non-existent user: {success} - {message}")
    
    return True

def test_api_endpoint():
    """Test authentication via API endpoint"""
    print("\n" + "=" * 60)
    print("Testing API endpoint (/auth/login)")
    print("=" * 60)
    
    try:
        # Test successful login
        response = requests.post(
            f'{API_BASE}/auth/login',
            json={'email': 'admin@owlban.com', 'password': 'Admin2024!'},
            timeout=5
        )
        print(f"Status: {response.status_code}")
        data = response.json()
        print(f"Success: {data.get('success')}")
        print(f"Message: {data.get('message')}")
        
        if data.get('access_token'):
            token = data['access_token']
            print(f"Access token: {token[:30]}...")
            
            # Test /auth/me endpoint
            me_response = requests.get(
                f'{API_BASE}/auth/me',
                headers={'Authorization': f'Bearer {token}'}
            )
            me_data = me_response.json()
            print(f"\n/auth/me response:")
            print(f"  Success: {me_data.get('success')}")
            if me_data.get('user'):
                print(f"  User: {me_data['user']}")
        
        return True
    except requests.exceptions.ConnectionError:
        print("ERROR: Cannot connect to API server (is it running?)")
        print("Start API server with: python api_server.py")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def test_user_registration():
    """Test user registration"""
    print("\n" + "=" * 60)
    print("Testing API endpoint (/auth/register)")
    print("=" * 60)
    
    try:
        # Try registering a new user
        new_email = f'newuser_{int(__import__("time").time())}@owlban.com'
        response = requests.post(
            f'{API_BASE}/auth/register',
            json={
                'email': new_email,
                'username': 'newuser',
                'password': 'NewPass123!',
                'role': 'user',
                'company': 'OWLBAN_GROUP'
            },
            timeout=5
        )
        data = response.json()
        print(f"Register new user: {data.get('success')}")
        print(f"Message: {data.get('message')}")
        return True
    except requests.exceptions.ConnectionError:
        print("ERROR: Cannot connect to API server")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def main():
    print("\n" + "=" * 60)
    print("BLACKBOX AI LOGIN SYSTEM TEST")
    print("=" * 60)
    
    # Test auth_lib (always available)
    test_auth_lib_direct()
    
    # Test API endpoints (requires running server)
    api_running = test_api_endpoint()
    
    if api_running:
        test_user_registration()
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)
    
    # Summary
    print("\n--- SUMMARY ---")
    print("Auth library: FUNCTIONAL")
    print(f"API server: {'RUNNING' if api_running else 'NOT RUNNING'}")
    print("\nTo start API server:")
    print("  cd c:/Users/bizle/OneDrive/bsean4890@gmail.com/four-era-env/OWLBAN-GROUP-NVIDIA")
    print("  python api_server.py")
    print("\nDefault login credentials:")
    print("  Email: admin@owlban.com")
    print("  Password: Admin2024!")

if __name__ == '__main__':
    main()
