def strToBinary(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
def binaryToDecimal(n): 
    return int(n,2) 
def getXOR(a, b): 
    res = "" 
    for i in range(len(a)): 
        if (a[i] == b[i]): 
            res += "0"
        else: 
            res += "1"
  
    return res 
def keyscheduler(key):
    xkey = key[:128]
    ykey = key[128:256]
    xparams=[]
    yparams=[]
    for i in range(0,128,32):
        xparams.append(binaryToDecimal(xkey[i:i+32]))
        yparams.append(binaryToDecimal(ykey[i:i+32]))
    return [xparams,yparams]
           

#if __name__ == '__main__': 
    #key = input("enter the secret key :")
    #binkey=strToBinary(key)
    #cp = keyscheduler(binkey)
    #for i in range(4):
        #print(binaryToDecimal(cp[i]))
        #print("\n")
        
        
    