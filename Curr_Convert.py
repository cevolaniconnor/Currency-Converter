import requests 

from_currency = str(
    input("Enter the currency that you'd like to convert:")).upper()

to_currency = str(input("Enter the currency you'd like to convert to:")).upper()

amount = float(input("Enter amount of money:"))

response = requests.get(
    f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

print(
    f"{amount} {from_currency} is {response.json()['rates'][to_currency]}{to_currency}"
)