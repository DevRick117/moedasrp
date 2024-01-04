import tkinter as tk
from tkinter import messagebox
import requests

def obter_cotacao(de, para):
    try:
        api = requests.get(f"https://economia.awesomeapi.com.br/{de}-{para}/")
        api.raise_for_status()  # Verifica se houve algum erro na requisição

        response = api.json()
        return float(response[0]['bid'])
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

def converter(valor, de, para):
    cotacao = obter_cotacao(de, para)
    if cotacao is not None:
        return valor * cotacao
    else:
        return None

def converter_moedas():
    try:
        valor = float(entry_valor.get())
        de = entry_de.get()
        para = entry_para.get()

        cotacao = converter(valor, de, para)

        if cotacao is not None:
            resultado_label.config(text=f"{valor} {de} é equivalente a {cotacao:.2f} {para}")
        else:
            messagebox.showerror("Erro", "Ocorreu um erro ao obter a cotação.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido.")

root = tk.Tk()
root.title("Conversor de Moedas")

# Layout
frame = tk.Frame(root, padx=10, pady=10)
frame.grid()

label_crit1 = tk.Label(frame, text="* Códigos: BRL, USD, EUR")
label_crit1.grid(row=0, column=0, columnspan=2, pady=5)

label_valor = tk.Label(frame, text="Valor:")
label_valor.grid(row=1, column=0, padx=5, pady=5)

entry_valor = tk.Entry(frame)
entry_valor.grid(row=1, column=1, padx=5, pady=5)

label_de = tk.Label(frame, text="De (código):")
label_de.grid(row=2, column=0, padx=5, pady=5)

entry_de = tk.Entry(frame)
entry_de.grid(row=2, column=1, padx=5, pady=5)

label_para = tk.Label(frame, text="Para (código):")
label_para.grid(row=3, column=0, padx=5, pady=5)

entry_para = tk.Entry(frame)
entry_para.grid(row=3, column=1, padx=5, pady=5)

btn_converter = tk.Button(frame, text="Converter", command=converter_moedas)
btn_converter.grid(row=4, column=0, columnspan=2, pady=10)

resultado_label = tk.Label(frame, text="")
resultado_label.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
