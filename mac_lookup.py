import requests

def lookup_mac(mac_address):
    url = 'https://macverify.com/api/v1/lookup'
    response = requests.get(url, params={'mac': mac_address})
    return response.json()

# Example usage
data = lookup_mac('00:1A:2B:3C:4D:5E')
print(data)
