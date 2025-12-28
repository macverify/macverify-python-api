README'yi Profesyonelleştirme: Ana sayfadaki README.md dosyasını düzenle ve içeriği şununla değiştir:

Markdown

# 🐍 MACVerify Python API Client

This repository provides a simple Python implementation to use the **[MACVerify.com](https://macverify.com)** API for instant MAC address vendor identification.

### 🚀 Quick Start
No API key or registration is required for the default tier.

```python
import requests
response = requests.get('[https://macverify.com/api/v1/lookup?mac=00:1A:2B:3C:4D:5E](https://macverify.com/api/v1/lookup?mac=00:1A:2B:3C:4D:5E)')
print(response.json())
📊 API Fair Usage
Requests: 5,000 per day (Free)

Authentication: None required

Data Source: Daily updated IEEE OUI records

For higher limits, please visit our API Documentation.


---

