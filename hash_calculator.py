import hashlib

arquivo = "evidencias/evidencia_001.txt"

with open(arquivo, "rb") as f:
    conteudo = f.read()

md5 = hashlib.md5(conteudo).hexdigest()
sha256 = hashlib.sha256(conteudo).hexdigest()

print("=== ANALISE DE INTEGRIDADE ===")
print()
print(f"Arquivo: {arquivo}")
print(f"Tamanho: {len(conteudo)} bytes")
print()
print(f"MD5:    {md5}")
print(f"SHA-256: {sha256}")