import requests

# Sample request payload (replace with actual data)
sample_payload = {
    "cardNumber": "1234567890123456",
    "expiryDate": "12/24",
    "cvv": "123"
}

# Visa sandbox server URL
sandbox_url = "https://sandbox.api.visa.com/carddata"

# Visa API key (replace with your actual API key)
api_key = "your_api_key_here"

# Headers including the API key
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Send the request
response = requests.post(sandbox_url, json=sample_payload, headers=headers)

# Process the response
if response.status_code == 200:
    print("Transaction authenticated successfully.")
    print(response.json())  # Display the response data
else:
    print("Transaction authentication failed.")
    print("Response:", response.text)
