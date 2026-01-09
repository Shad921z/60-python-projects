#currency converter
import requests

cur1 = input("\n \n \nEnter your currency: ").upper() #input for currency 1
cur2 = input("Enter the currency you want to convert: ").upper() #input for currency 2
amount = float(input("Enter the amount: ")) #amount input

#api url
url = f"https://v6.exchangerate-api.com/v6/16dbe26b38452a2683764095/pair/{cur1}/{cur2}/{amount}/"
response = requests.get(url)

#printing response
print(f"{amount} {cur1} is equal to {response.json()['conversion_result'] } {cur2}")