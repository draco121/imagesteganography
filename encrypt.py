# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 23:20:43 2020

@author: rajee
"""

from PIL import Image
import numpy as np
import keyscheduler as ks
from os import system, name 


def strToBinary(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8)) 
def binToString(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
def addZeros(strr, n): 
    for i in range(n): 
        strr = "0" + strr 
    return strr 
  
# Function to return the XOR 
# of the given strrings 
def getXOR(a, b): 
  
    # Lengths of the given strrings 
    aLen = len(a) 
    bLen = len(b) 
  
    # Make both the strrings of equal lengths asd
    # by inserting 0s in the beginning 
    if (aLen > bLen): 
        b = addZeros(b, aLen - bLen) 
    elif (bLen > aLen): 
        a = addZeros(a, bLen - aLen) 
  
    # Updated length 
    lenn = max(aLen, bLen); 
  
    # To store the resultant XOR 
    res = "" 
    for i in range(lenn): 
        if (a[i] == b[i]): 
            res += "0"
        else: 
            res += "1"
  
    return res 

    
def embed(im,xparams,yparams,message):
    seedx = xparams[2]
    seedy = yparams[2]
    indexx = seedx%xparams[4]
    indexy = seedx%yparams[4]
    istraversed =[]
    im[indexx][indexy]=len(message)//255
    seedx = (seedx*xparams[0]+xparams[1])%xparams[2]
    seedy = (seedy*yparams[0]+yparams[1])%yparams[2]
    indexx = seedx%xparams[4]
    indexy = seedy%yparams[4]
    im[indexx][indexy]= len(message)%255
    i = 0
    print(len(message))
    while i<len(message):
        seedx = (seedx*xparams[0]+xparams[1])%xparams[2]
        seedy = (seedy*yparams[0]+yparams[1])%yparams[2]
        indexx = seedx%xparams[4]
        indexy = seedy%yparams[4]        
        if (indexx,indexy) not in istraversed:
            if (message[i]=='0') and (im[indexx][indexy]% 2 != 0):     
                    if im[indexx][indexy] == 255:
                        im[indexx][indexy] -= 1
                        #im[indexx][indexy] = 0
                    else:
                        im[indexx][indexy] +=1
                        #im[indexx][indexy] = 0
                      
            elif (message[i]== '1') and (im[indexx][indexy]% 2 == 0): 
                 if im[indexx][indexy] ==0:
                        im[indexx][indexy] +=1
                        #im[indexx][indexy] = 0
                 else:
                     im[indexx][indexy] -=1
                     #im[indexx][indexy] = 0
            i +=1
            istraversed.append((indexx,indexy))
            
                    
def encrypt(key,message,image):
    plaintextbin = strToBinary(message) 
    keybin= strToBinary(key)
    whitemessage = getXOR(plaintextbin,keybin)
    im = np.array(Image.open(image,'r').convert("L"))
    params = ks.keyscheduler(keybin)
    xparams,yparams = params[0],params[1]
    xparams.append(im.shape[0])
    yparams.append(im.shape[1])
    embed(im, xparams, yparams, whitemessage)
    img = Image.fromarray(im)
    imagename = "newimage1.png"
    img.save(imagename)
    print("image is ready as:" + imagename)
    
       
# Driver Code 
if __name__ == '__main__': 
    key =input('enter the 32 characters secret key:')
    data = input("enter the message to embedd :")
    image = input("enter the path of image file :")
    encrypt(key,data,image)
