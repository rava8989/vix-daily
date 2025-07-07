import requests
import json
from datetime import datetime

# Simple example fetching VIX from public API or dummy placeholder

VIX_API_URL = "https://api.twelvedata.com/time_series?symbol=VIX&interval=1day&apikey=YOUR_API_KEY"

response = requests.get(VIX_API_URL)
data = response.json()

output = {
    "last_updated": datetime.utcnow().isoformat(),
    "vix_data": data
}

with open("vix.json", "w") as f:
    json.dump(output, f, indent=2)

print("Updated vix.json")
