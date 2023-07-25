import requests
from bs4 import BeautifulSoup
import sys

url = "https://kur.doviz.com"
response = requests.get(url)
htmlicerigi = response.content
soup = BeautifulSoup(htmlicerigi, "html.parser")

currency = soup.find_all("span", {"class": "name"})
value = soup.find_all("span", {"class": "value"})

list_currency = []
list_value = []

for a in currency:
    list_currency.append(a.text)
for b in value:
    list_value.append((b.text).replace(",", "."))

print(list_currency)
print(list_value)

print("""***********
CURRENCY APPLİCATİON

Operations:
1)Instant Exchange:
2)EURO ---> TURKİSH LIRA
3)TURKİSH LIRA ---> EURO
4)DOLAR ---> TURKİSH LIRA
5)TURKİSH LIRA ---> DOLAR
6)EURO ---> DOLAR
7)DOLAR ---> EURO
8)Exit 

************""")

while True:
    operation = input("Enter a operation:")
    if operation == "1":
        for i, j in zip(currency, value):
            print(i.text, ":", j.text)
    elif operation == "2":
        amount = float(input("Enter the amount to convert:"))
        result = amount * float(list_value[2])
        print("{} Euro equals {} Türkish lira.".format(amount, result))
    elif operation == "3":
        amount = float(input("Enter the amount to convert:"))
        result = amount / float(list_value[2])
        print("{} Türkish lira equlas {} Euro.".format(amount, result))
    elif operation == "4":
        amount = float(input("Enter the amount to convert:"))
        result = amount * float(list_value[1])
        print("{} Dolar equals {} Türkish lira.".format(amount, result))
    elif operation == "5":
        amount = float(input("Enter the amount to convert:"))
        result = amount / float(list_value[1])
        print("{} Türkish lira equals {} Dolar.".format(amount, result))
    elif operation == "6":
        amount = float(input("Enter the amount to convert:"))
        result = amount * float(list_value[2]) / float(list_value[1])
        print("{} Euro equals {} Dolar.".format(amount, result))
    elif operation == "7":
        amount = float(input("Enter the amount to convert:"))
        result = amount * float(list_value[1]) / float(list_value[2])
        print("{} Dolar equals {} Euro.".format(amount, result))
    elif operation == "8":
        print("Logged out.")
        break
    else:
        sys.stderr.write("Please enter a valid operation...\n")
        sys.stderr.flush()
