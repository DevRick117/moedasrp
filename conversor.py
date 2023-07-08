import requests
import json

#criando as def

def converter(valor, de, para):
    api = requests.get(f"https://economia.awesomeapi.com.br/{de}-{para}/")
    
    if api.status_code == 200:
        response = api.json()
        return float(response[0]['bid']) * valor
    else:
        return None
    
print("==conversor de moedas==")
print("Moedas disponiveis: USD, BRL, EUR,\n")

valor = float(input("valor: "))
de = input("Converter de (codigo): ")
para = input("converter o (codigo): ")

cotacao = converter(valor, de, para)

if cotacao is not None:
    print(f"{valor} {de} é equivalente a {cotacao} {para}")
else:
    print("Error")