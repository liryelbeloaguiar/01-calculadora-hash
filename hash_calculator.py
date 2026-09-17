import hashlib
import os
from datetime import datetime

caminho = input("Digite o caminho do arquivo: ")

id_evidencia = input("Digite o identificador da evidência: ")

if not os.path.exists(caminho):
    print("\nERRO: O arquivo informado não existe.")
    exit()

md5 = hashlib.md5()
sha256 = hashlib.sha256()
sha512 = hashlib.sha512()

with open(caminho, "rb") as arquivo:
    while bloco := arquivo.read(4096):
        md5.update(bloco)
        sha256.update(bloco)
        sha512.update(bloco)

md5 = md5.hexdigest()
sha256 = sha256.hexdigest()
sha512 = sha512.hexdigest()

tamanho = os.path.getsize(caminho)

data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

os.makedirs("resultado", exist_ok=True)

nome_arquivo = os.path.basename(caminho)
nome_arquivo_sem_extensao = os.path.splitext(nome_arquivo)[0]

registro = os.path.join(
    "resultado",
    f"{id_evidencia}_{nome_arquivo_sem_extensao}.txt"
)

with open(registro, "w", encoding="utf-8") as arquivo:
    arquivo.write("=== REGISTRO DE ANALISE DE EVIDENCIA DIGITAL ===\n\n")
    arquivo.write(f"ID da evidência: {id_evidencia}\n")
    arquivo.write(f"Arquivo: {nome_arquivo}\n")
    arquivo.write(f"Caminho: {caminho}\n")
    arquivo.write(f"Tamanho: {tamanho} bytes\n")
    arquivo.write(f"Data/Hora da análise: {data_hora}\n\n")
    arquivo.write("=== HASHES ===\n")
    arquivo.write(f"MD5: {md5}\n")
    arquivo.write(f"SHA-256: {sha256}\n")
    arquivo.write(f"SHA-512: {sha512}\n")

print("\n=== ANALISE DE INTEGRIDADE ===")
print(f"Arquivo: {caminho}")
print(f"Tamanho: {tamanho} bytes")
print(f"MD5: {md5}")
print(f"SHA-256: {sha256}")
print(f"SHA-512: {sha512}")
print(f"Data/Hora da análise: {data_hora}")
print(f"\nRegistro salvo em: {registro}")