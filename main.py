import os.path
import time
import zj_toolkit
import wget

allpath = os.getcwd()
down = 'https://i-440.wwentua.com:446/01202000159054184bb/2024/01/20/c306a13e928748f57503d5b25475698c.7z?st=Ah3UANe4Ji7FlOw8Y1uK6Q&e=1705757596&b=Ax5aCQhlVDAAPF5mBCYOf1VuD31QZgt3&fi=159054184&pid=223-88-51-79&up=2&mp=0&co=0'
colist=["ls","wget","askzj"]


filenum = 0
mfile = ["zj_toolkit", "toolkit.py","__pycache__"]
path = os.getcwd()
for i in range(len(mfile)):
    if mfile[i] in os.listdir(path):
        print("Found_" + path+r"\"" +mfile[i])
        filenum += 1
        time.sleep(1)
time.sleep(2)
for i in range(10):
    print("creat_")
    for i in range(5):
        zj_toolkit.printProgress(i + 1, 5, "Creating", "room", 0, 30)

        i += 1
        time.sleep(0.1)
    print(zj_toolkit.hexman(100000000, 9999999999))
print('\n')
time.sleep(2)
os.system('cls')
print("Hello World!")
time.sleep(2)
zj_toolkit.cicon(False, 0)
time.sleep(2)
print("Let's start")
time.sleep(2)

while True:
    user = input(os.getcwd() + ">>>:").split()

    if len(user) >= 1 and user[0]=="ls":
        print(os.listdir())



    elif len(user) == 0:
        continue

    elif user[0]=="clear":
        os.system('cls')

    elif user[0] == "askzj":
        print('ls\ntimenow\nwget\ncd\ncolor\n')

    elif user[0] == "wget":
        try:
            wget.download(user[1], allpath)
        except Exception as e:
            print(f'An error occurred: {e}')

    else:
        print("War.!Unknow command please ask for zj or input askzj")
