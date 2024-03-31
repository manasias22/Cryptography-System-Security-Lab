#define function to finding multiplication key
def decrypt(a,b):
    a=a%b
    for x in range (1,b):
        if((a*x)%b==1):
            return x
    return 1

enc=""
dec=""
letters="abcdefghijklmnopqrstuvwxyz"
k1=int(input("Enter the Addition key: "))
k2=int(input("Enter the Mult. key: "))
get_MultKey=decrypt(k1,26)
msg=str(input("Enter Message: "))

#encrypting msg
for i in msg:
        if i == " ":
            enc=enc+i
        else:
            enc=enc+letters[(letters.find(i)*k1+k2)%26]
print("Encrypted Message: ", enc)

#decrypting msg
for i in enc:
    if i==" ":
        dec=dec+i
    else:
        dec=dec+letters[((letters.find(i)-k2)*get_MultKey)%26]

print("Decrypted Message: ", dec)
        
        
'''
output:

Enter the Addition key: 7
Enter the Mult. key: 6
Enter Message: vipul bhoir
Encrypted Message:  xkhqf ndakv
Decrypted Message:  vipul bhoir
'''
