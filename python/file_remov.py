import os

path = "F:\insta\demo"
name_list = os.listdir(path)
# print(name_list)
for name in name_list:
    # if os.path.isfile(name):
    if name.endswith(".mp4"):
        continue
    else:
        os.remove(name)
