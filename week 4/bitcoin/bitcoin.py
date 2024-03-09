import sys
import requests
import json

try:
    n = float(sys.argv[1])
    bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin_data = bitcoin.json()
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")
except requests.RequestException:
    exit ()
else:
    price = bitcoin_data["bpi"]["USD"]["rate_float"]
    amount = n * price
    print(f"${amount:,.4f}")
