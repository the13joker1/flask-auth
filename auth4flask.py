import requests
import urllib.parse

"""
BASE_OAUTH_URL = "https://example.com/oauth/"
TOKEN_URL = "https://example.com/token"
AUTHORIZATION_BASE_URL = "https://example.com/authorize"
RESPONSE_TYPE = "code"
SCOPES = "openid"
"""
# Funktion zur Generierung der OAuth Autorisierungs-URL
def generate_authorization_url(client_id, redirect_uri, scope=SCOPES, response_type=RESPONSE_TYPE, base_oauth_url=BASE_OAUTH_URL):
    auth_url = urllib.parse.urljoin(base_oauth_url, 'authorize')
    params = {
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'response_type': response_type,
        'scope': scope
    }
    return f"{auth_url}?{urllib.parse.urlencode(params)}"

# Funktion zur Authentifizierung mit OAuth 2.0
def oauth2_authorize(client_id, redirect_uri, response_type=RESPONSE_TYPE, scopes=SCOPES):
    params = {
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'response_type': response_type,
        'scope': scopes
    }
    auth_url = f"{AUTHORIZATION_BASE_URL}?{urllib.parse.urlencode(params)}"
    return auth_url

# Funktion zum Austausch des Autorisierungscodes gegen ein Access Token
def exchange_code_for_token(code, client_id, client_secret, redirect_uri):
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }
    token_response = requests.post(TOKEN_URL, data=token_data)

    if token_response.status_code == 200:
        return token_response.json()
    else:
        return None

# Beispiel für die Verwendung:
if __name__ == '__main__':
    CLIENT_ID = 'your_client_id'
    CLIENT_SECRET = 'your_client_secret'
    REDIRECT_URI = 'https://yourapp.com/callback'

    # Beispiel für die Verwendung der Funktionen:
    auth_url = generate_authorization_url(CLIENT_ID, REDIRECT_URI)
    print("Authorization URL:", auth_url)

    # Weiterer Beispielaufruf
    code = 'authorization_code_received_from_callback'
    token_response = exchange_code_for_token(code, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
    print("Token Response:", token_response)
