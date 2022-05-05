import os, shutil
import filecmp
import time
from datetime import datetime


def copytree(src, dst, nrfisiere2, FisiereMinus, FisirePlus):
    ok="false"
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if ok=="false" :
            if nrfisiere2 < len(os.listdir(src)):
                FisirePlus = FisirePlus + 1
                print(str(datetime.now())+ "A number of " + str(FisirePlus) + " files have been added")
                ok="true"
            if nrfisiere2 > len((os.listdir(src))):
                FisiereMinus = FisiereMinus + 1
                print(str(datetime.now()) + " number of " + str(FisiereMinus) + " files have been removed")
                ok="true"
            if os.path.isdir(s):  # daca e folder
                shutil.copytree(s, d)  # copiere foldere
            else:
                shutil.copy2(s, d)  # copiere file uri


def run():
    folder1 = input("Please enter the location of thefolder that needs to be periodicly duplicated :")
    folder2 = input("Please enter the replica folder of 'folder 1' :")
    fisiereMinus = int(0)
    fisierePlus = int(0)
    nrfisiere2 = len(os.listdir(folder1))
    while True:
        time.sleep(1.0)
        copytree(folder1,folder2,nrfisiere2,fisiereMinus,fisierePlus)
        nrfisiere2 = len(os.listdir(folder1))
        for item in os.listdir(folder2):
            h = os.path.join(folder2, item)
            ok2 = "false"
            numar = 0
            for item2 in os.listdir(folder1):
                z = os.path.join(folder1, item2)
                if filecmp.cmp(str(h), str(z)):
                    ok2 = "true"
            if ok2 == "false":
                os.remove(h)


run()


