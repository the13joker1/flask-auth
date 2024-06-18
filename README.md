# Flask Auth

usage: 
 
    BASE_OAUTH_URL = "https://example.com/oauth/"
    TOKEN_URL = "https://example.com/token"
    AUTHORIZATION_BASE_URL = "https://example.com/authorize"
    RESPONSE_TYPE = "code"
    SCOPES = "openid"
    
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
