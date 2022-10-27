import requests
import os

dir_path = os.path.join(os.getcwd(),'image')
os.mkdir(dir_path)

for i in range(30000,60001):
    url = (f'http://gnioterp.com:155/Photo/{str(i)}.jpg')
    print(url)
    res = requests.get(url)
    if res.status_code == 200:
        with open(os.path.join(dir_path,f"{str(i)}.jpg"),"wb") as img:
            print(f"downloading file {str(i)}.jpg")
            for packet in res.iter_content(chunk_size=1024):
                img.write(packet)

print("success!!!")


