import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv() 

client = genai.Client()
MODEL = "gemini-2.5-flash"

ALLOWED_ACTIONS = {"summarize_code"}

def ask_model(code: str) -> str:
    prompt = f"""
Você é um agente especialista em análise e melhoria de código Python.

Tarefas:
1. Explique o que o código faz.
2. Identifique problemas ou melhorias.
3. Sugira uma versão melhorada.


Código:
Responda de forma estruturada.
"""
    resp = client.models.generate_content(model=MODEL, contents=prompt)
    return resp.text


def main():
    print("Agente de Análise de Código iniciado. Cole o código abaixo e pressione ENTER duas vezes.\n")

    codigo = ""
    while True:
        linha = input()
        if linha.strip() == "":
            break
        codigo += linha + "\n"

    print("\n===== RESULTADO =====\n")
    print(ask_model(codigo))


if __name__ == "__main__":
    main()
