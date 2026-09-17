import hashlib
import os

caminho = input("Digite o caminho do arquivo: ")

if not os.path.exists(caminho):
    print("\nERRO: O arquivo informado não existe.")
    exit()

md5 = hashlib.md5()
sha256 = hashlib.sha256()

with open(caminho, "rb") as arquivo:
    while bloco := arquivo.read(4096):
        md5.update(bloco)
        sha256.update(bloco)

md5 = md5.hexdigest()
sha256 = sha256.hexdigest()

tamanho = os.path.getsize(caminho)

print("\n=== ANALISE DE INTEGRIDADE ===")
print(f"Arquivo: {caminho}")
print(f"Tamanho: {tamanho} bytes")
print(f"MD5: {md5}")
print(f"SHA-256: {sha256}")