import math

def check1():
    msg="vidyavardhinis college vasai"
    key=8
    enc=encrypt(key,msg)
    print(enc)

def encrypt(key,msg):
    enc=[""]*key
    for col in range(key):
        col_index=col
        while col_index < len(msg):
            enc.append(msg[col_index])
            col_index+=key
    return "".join(enc)

check1()


def check2():
    msg="vdoaihlsdilayneiaigvsea  rcv"
    key=8
    dec=decrypt(key,msg)
    print(dec)

def decrypt(key,msg):
    dec=[""]*key
    ncol=math.ceil(len(msg)/key)
    nrow=key
    nbox=ncol*nrow-len(msg)
    col=0
    row=0
    for x in range (len(msg)):
        index=x
        while index < 12 and x != ncol-1 :
            dec.append(msg[index])
            index+=ncol
    return "".join(dec)

check2()

