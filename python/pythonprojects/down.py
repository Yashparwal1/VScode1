import requests
import os

# dir_path = os.path.join(os.getcwd(),'image')
# os.mkdir(dir_path)

# for i in range(30000,60001):
#     url = (f'http://gnioterp.com:155/Photo/{str(i)}.jpg')
#     print(url)
#     res = requests.get(url)
#     if res.status_code == 200:
#         with open(os.path.join(dir_path,f"{str(i)}.jpg"),"wb") as img:
#             print(f"downloading file {str(i)}.jpg")
#             for packet in res.iter_content(chunk_size=1024):
#                 img.write(packet)

# print("success!!!")

# dir_path = os.path.join(os.getcwd(),'pdfs')
# os.mkdir(dir_path)
# for i in range(110100,110200):
#     url = (f'https://jespublication.com/upload/2020-{i}.pdf')
#     res = requests.get(url)
#     if res.status_code == 200:
#         with open(os.path.join(dir_path,f"2022-{str(i)}.pdf"),"wb") as file:
#             print(f"downloading file 2022-{str(i)}.pdf")
#             for packet in res.iter_content(chunk_size=1024):
#                 file.write(packet)

# print("success!!!")

import requests
baseurl="https://jespublication.com/upload/"
def filename():
    for i in range(110100,110200):
        fname=f"2020-{i}.pdf"
        get_url(fname)
def get_url(fname):
    fullurl=baseurl+fname;
    res=requests.get(baseurl)
    scode=res.status_code
    if scode != 404:
        print("Downloading file...")
        get_file(res,fname)
    else:
        print(scode)
def get_file(res,fname):
    f=open(fname,"wb")
    f.write(res.content)
    f.close
if __name__ == '__main__':
    filename()

