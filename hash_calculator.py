import hashlib
import os
from datetime import datetime


def gerar_proximo_id():
    os.makedirs("resultado", exist_ok=True)

    arquivos = os.listdir("resultado")

    maior_numero = 0

    for arquivo in arquivos:
        if arquivo.startswith("EVIDENCIA_"):
            partes = arquivo.split("_")

            try:
                numero = int(partes[1])

                if numero > maior_numero:
                    maior_numero = numero

            except (IndexError, ValueError):
                continue

    proximo_numero = maior_numero + 1

    return f"EVIDENCIA_{proximo_numero:03d}"


caminho = input("Digite o caminho do arquivo: ")

id_evidencia = gerar_proximo_id()

tipos_evidencia = {
    "1": "DOCUMENTO",
    "2": "IMAGEM",
    "3": "VIDEO",
    "4": "AUDIO",
    "5": "ARQUIVO",
    "6": "LOG",
    "7": "BANCO DE DADOS",
    "8": "OUTRO"
}

print("\n=== TIPO DA EVIDÊNCIA ===")
print("1 - DOCUMENTO")
print("2 - IMAGEM")
print("3 - VIDEO")
print("4 - AUDIO")
print("5 - ARQUIVO")
print("6 - LOG")
print("7 - BANCO DE DADOS")
print("8 - OUTRO")

opcao_tipo = input("Digite o número do tipo: ")

while opcao_tipo not in tipos_evidencia:
    print("ERRO: Tipo de evidência inválido.")
    opcao_tipo = input("Digite uma opção de 1 a 8: ")

tipo_evidencia = tipos_evidencia[opcao_tipo]


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

extensao = os.path.splitext(nome_arquivo)[1]

nome_arquivo_sem_extensao = os.path.splitext(nome_arquivo)[0]

registro = os.path.join(
    "resultado",
    f"{id_evidencia}_{nome_arquivo_sem_extensao}.txt"
)


with open(registro, "w", encoding="utf-8") as arquivo:

    arquivo.write("=== REGISTRO DE ANALISE DE EVIDENCIA DIGITAL ===\n\n")

    arquivo.write(f"ID da evidência: {id_evidencia}\n")
    arquivo.write(f"Tipo da evidência: {tipo_evidencia}\n")
    arquivo.write(f"Arquivo original: {nome_arquivo}\n")
    arquivo.write(f"Extensão: {extensao}\n")
    arquivo.write(f"Caminho original: {caminho}\n")
    arquivo.write(f"Tamanho: {tamanho} bytes\n")
    arquivo.write(f"Data/Hora da análise: {data_hora}\n\n")

    arquivo.write("=== HASHES ===\n")

    arquivo.write(f"MD5: {md5}\n")
    arquivo.write(f"SHA-256: {sha256}\n")
    arquivo.write(f"SHA-512: {sha512}\n")


print("\n=== ANALISE DE INTEGRIDADE ===")
print(f"ID da evidência: {id_evidencia}")
print(f"Arquivo: {caminho}")
print(f"Tipo da evidência: {tipo_evidencia}")
print(f"Tamanho: {tamanho} bytes")
print(f"MD5: {md5}")
print(f"SHA-256: {sha256}")
print(f"SHA-512: {sha512}")
print(f"Data/Hora da análise: {data_hora}")
print(f"\nRegistro salvo em: {registro}")