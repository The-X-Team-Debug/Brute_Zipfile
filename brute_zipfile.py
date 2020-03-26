import zipfile
from tqdm import tqdm

sora = "word.txt"
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
            print("Pw ketemu cukk!!????:",TheX.decode().strip())
            exit(0)
print("Pw gk ketemu")


