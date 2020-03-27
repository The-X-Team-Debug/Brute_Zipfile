import zipfile
from tqdm import tqdm

# Tarus sekumpulan file yg sudah diisi dengan password ber ektensi txt
sora = "word.txt"
# Disini adalah file yg ingin di brute ingat taruh file nya di folder ini
shiro = "TheXTools.zip"

shiro = zipfile.ZipFile(shiro)
kuhaku = len(list(open(sora, 'rb')))
print("Total pw yg di coba:", kuhaku)

with open(sora, 'rb') as sora:
    for TheX in tqdm(sora, total=kuhaku, unit="list"):
        try:
            shiro.extractall(pwd=TheX.strip())
        except:
            continue
        else:
            print("Pw ketemu !!:",TheX.decode().strip())
            exit(0)
print("Pw gk ketemu:")
print("Silahkan isi worldlist nya dengan keyakinan anda :)")


