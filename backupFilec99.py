import os
import shutil

sourcepath= input('Enter your folders souce path: ')
destinationfile= input('Enter place where you have to pub lish file: ')

sourcepath=sourcepath+'/'
destinationfile=destinationfile+'/'

listdirectry=os.listdir(sourcepath)

for bat in listdirectry:
    shutil.copy((sourcepath+bat),destinationfile)