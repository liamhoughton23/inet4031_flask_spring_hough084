# inspiration code for Python Unit Testing Project

from cmath import pi
import math

def surfaceArea():  
    pass

def volume(rad):
    cube = rad * rad * rad
    volume = (4/3) * pi * cube
    return volume

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME AND SURFACE AREA OF SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))

if __name__ == '__main__':
    prompt()
