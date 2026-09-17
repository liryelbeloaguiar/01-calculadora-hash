import hashlib
import os
from datetime import datetime


def calcular_hashes(caminho):
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()
    sha512 = hashlib.sha512()

    with open(caminho, "rb") as arquivo:
        while bloco := arquivo.read(4096):
            md5.update(bloco)
            sha256.update(bloco)
            sha512.update(bloco)

    return {
        "MD5": md5.hexdigest(),
        "SHA-256": sha256.hexdigest(),
        "SHA-512": sha512.hexdigest()
    }


def verificar_integridade(caminho, hash_registrado):
    hashes_atuais = calcular_hashes(caminho)

    hash_atual = hashes_atuais["SHA-256"]

    if hash_atual == hash_registrado:
        return True, hash_atual

    return False, hash_atual


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


def buscar_hash_registrado(id_evidencia):

    arquivos = os.listdir("resultado")

    for arquivo in arquivos:

        if arquivo.startswith(id_evidencia + "_") and arquivo.endswith(".txt"):

            caminho_registro = os.path.join("resultado", arquivo)

            with open(caminho_registro, "r", encoding="utf-8") as registro:

                for linha in registro:

                    if linha.startswith("SHA-256:"):

                        return linha.split(":", 1)[1].strip()

    return None


def executar_verificacao():

    print("\n=== VERIFICAÇÃO DE INTEGRIDADE ===")

    id_evidencia = input("Digite o ID da evidência: ")

    caminho = input("Digite o caminho atual do arquivo: ")

    if not os.path.exists(caminho):

        print("\nERRO: O arquivo informado não existe.")

        return

    hash_registrado = buscar_hash_registrado(id_evidencia)

    if hash_registrado is None:

        print("\nERRO: Evidência não encontrada.")

        return

    integridade, hash_atual = verificar_integridade(
        caminho,
        hash_registrado
    )

    print(f"\nID da evidência: {id_evidencia}")
    print(f"Hash registrado: {hash_registrado}")
    print(f"Hash atual:      {hash_atual}")

    if integridade:

        print("\nRESULTADO: INTEGRIDADE PRESERVADA")

    else:

        print("\nRESULTADO: ALTERAÇÃO DETECTADA")


def executar_nova_analise():

    print("\n=== NOVA ANÁLISE ===")

    caminho = input("Digite o caminho do arquivo: ")

    if not os.path.exists(caminho):

        print("\nERRO: O arquivo informado não existe.")

        return

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

    hashes = calcular_hashes(caminho)

    md5 = hashes["MD5"]
    sha256 = hashes["SHA-256"]
    sha512 = hashes["SHA-512"]

    tamanho = os.path.getsize(caminho)

    data_hora = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )

    nome_arquivo = os.path.basename(caminho)

    extensao = os.path.splitext(nome_arquivo)[1]

    nome_arquivo_sem_extensao = os.path.splitext(
        nome_arquivo
    )[0]

    registro = os.path.join(
        "resultado",
        f"{id_evidencia}_{nome_arquivo_sem_extensao}.txt"
    )

    with open(
        registro,
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(
            "=== REGISTRO DE ANALISE DE EVIDENCIA DIGITAL ===\n\n"
        )

        arquivo.write(
            f"ID da evidência: {id_evidencia}\n"
        )

        arquivo.write(
            f"Tipo da evidência: {tipo_evidencia}\n"
        )

        arquivo.write(
            f"Arquivo original: {nome_arquivo}\n"
        )

        arquivo.write(
            f"Extensão: {extensao}\n"
        )

        arquivo.write(
            f"Caminho original: {caminho}\n"
        )

        arquivo.write(
            f"Tamanho: {tamanho} bytes\n"
        )

        arquivo.write(
            f"Data/Hora da análise: {data_hora}\n\n"
        )

        arquivo.write("=== HASHES ===\n")

        arquivo.write(
            f"MD5: {md5}\n"
        )

        arquivo.write(
            f"SHA-256: {sha256}\n"
        )

        arquivo.write(
            f"SHA-512: {sha512}\n"
        )

    print("\n=== ANÁLISE CONCLUÍDA ===")

    print(f"ID da evidência: {id_evidencia}")
    print(f"Arquivo: {nome_arquivo}")
    print(f"Tipo: {tipo_evidencia}")
    print(f"Tamanho: {tamanho} bytes")
    print(f"MD5: {md5}")
    print(f"SHA-256: {sha256}")
    print(f"SHA-512: {sha512}")
    print(f"Data/Hora: {data_hora}")

    print(f"\nRegistro salvo em: {registro}")


def menu_principal():

    while True:

        print("\n")
        print("=" * 40)
        print("   ANALISADOR DE EVIDÊNCIAS DIGITAIS")
        print("=" * 40)

        print("\n1 - Nova análise")
        print("2 - Verificar integridade")
        print("3 - Consultar evidência")
        print("4 - Listar evidências")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            executar_nova_analise()

        elif opcao == "2":

            executar_verificacao()

        elif opcao == "3":

            print("\nFuncionalidade ainda não implementada.")

        elif opcao == "4":

            print("\nFuncionalidade ainda não implementada.")

        elif opcao == "5":

            print("\nEncerrando o programa...")

            break

        else:

            print("\nERRO: Opção inválida.")


menu_principal()

