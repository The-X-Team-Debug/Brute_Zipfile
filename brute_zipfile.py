import zipfile
import subprocess
from tqdm import tqdm

subprocess.call('figlet Brute_ZipFile',shell=True)
print('Aut = The X Kuhaku')
print('Yt = Kuhaku Termux')

sora=input"worldlist.txt"
shiro=input"file yg ingin di brute.zip"

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
print("Silahkan isi worldlist nya dengan pw yg tepat :)")


