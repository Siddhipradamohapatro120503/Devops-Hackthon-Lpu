import requests

from ln_oauth import auth, headers

# Your LinkedIn API credentials
client_id = '864q0g31l6q2t3'
client_secret = '83uXYxodL8hqVKKI'
access_token = 'AQVYht7gMuPTU6BoilGdG4fgUnADwNhEJdzCWkqICwtZ8iruYCV4elnewa653_6bISlY5sGtX_wSla6URrhUi3b67DAh3C0VQt8euJSJAeXAm2kzy73__2CfMaVIo8uixKbEZl1sZOYntMsi4xuu6jlsEnU_oLiM0egSCSKSjA22NxrdNmsz6kK0sdxr5qf9yybgWPAhdi7OgLUdnmKFAvFmV5mrbez0hrJjGhpFZnuXPgIbegRLpFUcYZzzadSwevvwgUpWhNzAZYESJko2qn78LbOLSzi7hYYqAToJb-2WAcZQ3r0ykwqciesA8cM3Z_fyIroJNPBGibgeuj6u3RERLtctlQ'

# Authentication endpoint
auth_url = 'https://www.linkedin.com/oauth/v2/accessToken'

# Endpoint for uploading media asset
upload_url = 'https://api.linkedin.com/v2/assets?action=upload'

# Endpoint for posting with media asset
post_url = 'https://api.linkedin.com/v2/shares'

# Headers for authentication
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

# Parameters for authentication
params = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
}

# Get access token
response = requests.post(auth_url, headers=headers, params=params)
access_token = response.json()['access_token']

# Upload PNG image
headers = {
    'Authorization': f'Bearer {access_token}',
}
files = {
    'file': open('output.png', 'rb')
}
response = requests.post(upload_url, headers=headers, files=files)
media_asset = response.json()

# Create post with media asset
post_data = {
    'author': 'urn:li:organization:123456789',
    'lifecycleState': 'PUBLISHED',
    'specificContent': {
        'com.linkedin.ugc.ShareContent': {
            'media': [
                {
                    'status': 'READY',
                    'media': media_asset['value']
                }
            ],
            'shareCommentary': {
                'text': 'Check out this image!'
            }
        }
    },
    'visibility': {
        'com.linkedin.ugc.MemberNetworkVisibility': 'PUBLIC'
    }
}
response = requests.post(auth_url, headers=headers, params=params)
print("Authentication response status code:", response.status_code)
print("Authentication response text:", response.text)
access_token = response.json().get('access_token')
print("Obtained access token:", access_token)
