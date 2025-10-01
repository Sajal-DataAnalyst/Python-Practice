# a=open('main.py')
# print(a.read())

# a=open('love.txt','a')
# a.write(" Hi i am Sajal. I am from Pune. And i am writing inside this file, and now i am appending some content isnside the file")

# a.close()

from pathlib import Path
import os
def readfileandfolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f'{i+1} : {items}')

def createfile():
    try:
        readfileandfolder()
        name = input('Please tell your file name :- ')
        p=Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data=input("What you want to write in this file")
                fs.write(data)
            print(f'File created successfully')  
        else:
            print(' This file already exist')
    except Exception as err:
        print(f' An error occured as {err}')

def readfile():
    try:

        readfileandfolder()
        name=input('Which file you want to read')  
        p=Path(name)
        if p.exists() and p.is_file:
            with open(p,'r') as fs:
                data=fs.read()
                print(data)
            print("Readed successfullyy")
        else:
            print('file do not exist')
    except Exception as err:
        print(f' An error occured as err')
          
def updatefile():
    try:
        readfileandfolder()
        name=input('Tell which file you want to update ')
        p=Path(name)
        if p.exists() and p.is_file:
            print(f'Press 1 for changing name of file ')
            print(f'Press 2 for overwriting the data of your file ')
            print(f'Press 3 for appending some content in your file')

            res=int(input('Tell your response'))
            if res==1:
                name2=input('Tell your new file name :- ')
                p2 = Path(name2)
                p.rename(p2)
            if res==2:
                with open(p,'w') as fs:
                    data=input("Tell what you want to write this overwrite the data")
                    fs.write(data)
            if res==3:  
                with open(p,'a') as fs:
                    data=input("Tell what you want to append to the data")
                    fs.write(" "+data)      
    except Exception as err:
        print('an error occured as {err}')

def deletefile():
    try:
        readfileandfolder()
        name=input('Which file you want to delete ')
        p=Path(name)

        if p.exists() and p.is_file():
            os.remove(p)

            print(' file removed successfully ')
        else:
            print('No such file exist ')
    except Exception as err:
        print(f' An error occured as {err}')

print('Press 1 for reading file ')
print(' Press 2 for reading file ')
print(' Press 3 for updating file ')
print(' Press 4 for deleting file ')

check = int(input(' Please enter your response '))

if check ==1:
    createfile()

if check ==2:
    readfile()

if check ==3:
    updatefile()

if check ==4:
    deletefile()

