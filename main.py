import requests
api_key = "fca_live_ywXQP99lIaQ9bNcqp17E9oQwqF1ATav3FpCtDIz9"
base_url = f'https://api.freecurrencyapi.com/v1/latest?apikey={api_key}'

Currencies = ["USD","CAD","EUR","AUD","CNY"]

def convert_currency(base):
    currencies = ",".join(Currencies)
    url = f"{base_url}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid Currency")
        return None
while True:
    base = (input("Enter the currency: ")).upper()
    if base == "Q":
        break
    data = convert_currency(base)
    if not data:
        continue  
    del data[base]
    for curr, value in data.items():
        print(f"{curr}: {value}")