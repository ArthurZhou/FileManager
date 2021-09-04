# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
 fileSYSTEM 2.0
 By Arthur Zhou
"""


# setup
conFig = './config.txt'
with open(conFig, 'r') as f:
    way = f.read()

# import block
import os
import sys
import time


# def function
def edit():
    global way
    global f
    wrFl = input("File name:")
    true = str(os.path.exists(os.getcwd() + "/" + wrFl))
    if true == "False":
        print("No such file or dictionary...")
    else:
        if true == "True":
            with open(os.getcwd() + "/" + wrFl, 'r') as f:
                print("\n-----\n", f.read(), "\n\n-----")
            wrTxt = input("New version:")
            file_handle = open(os.getcwd() + "/" + wrFl, mode='w')
            file_handle.write(wrTxt)
            file_handle.close()
            print("Success!")
    main()


def openF():
    global way
    global f
    print(" a.file \n b.folder ")
    ff = input("File or folder:")
    if ff == "a":
        opFl = input("File name:")
        true = str(os.path.exists(os.getcwd() + "/" + opFl))
        if true == "False":
            print("No such file or dictionary...")
        else:
            if true == "True":
                with open(os.getcwd() + "/" + opFl, 'r') as f:
                    print("\n-----\n\n", f.read(), "\n\n-----\n")
    if ff == "b":
        folder = input("Folder name:(without Folder-)")
        true = str(os.path.exists(os.getcwd() + "/Folder-" + folder))
        if true == "False":
            print("No such file or dictionary...")
        else:
            os.chdir(way + "/Folder-" + folder)
    main()


def delete():
    global way
    fldIn = input("File name:")
    true = str(os.path.exists(os.getcwd() + "/" + fldIn))
    if true == "False":
        print("No such file or dictionary...")
    else:
        if true == "True":
            print("Do you want to delete ", fldIn, "?")
            yon = input("Enter 'y' to continue:")
            if yon == "y":
                os.remove(os.getcwd() + "/" + fldIn)
                print("Success!")
    main()


def create():
    global way
    cho = input(' a.file \n b.folder:')
    if cho == 'a':
        fled = input('File name:')
        file = open(os.getcwd() + '/' + fled, 'w')
        file.write('New file...')
        file.close()
        print('Success!')
    if cho == 'b':
        fled = input('Folder name:')
        os.mkdir('Folder-' + fled)
        print('Success!')
    main()


def listFile():
    # file list
    print("\nLocation:", os.getcwd(), ";")
    print("\nFile:\n")
    inCld = os.listdir()
    for index in range(len(inCld)):
        print("- ", inCld[index])


def loginTime():
    # login time block
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    print("login at", now)


# def main
def main():
    global way
    listFile()
    # print and choose function block
    print("\n a.edit file \n b.open \n c.delete \n d.create \n e.back \n f.quit ")
    fInput = input("function:")

    if fInput == "a" or "b" or "c" or "d" or "e":
        if fInput == "a":
            edit()

        if fInput == "b":
            openF()

        if fInput == "c":
            delete()

        if fInput == "d":
            create()

        if fInput == "e":
            way2 = (os.path.abspath(os.path.join(os.getcwd(), "..")))
            os.chdir(way2)
            main()

        if fInput == "f":
            sys.exit(0)

    else:
        main()


loginTime()
os.chdir(way)
main()
