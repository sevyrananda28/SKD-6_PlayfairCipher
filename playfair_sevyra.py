key=input("Enter key : ") #masukkan kunci yang akan digunakan
key=key.replace(" ", "")
key=key.upper()
def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    
result=list()
for c in key: #untuk menyimpan kunci
    if c not in result:
        if c=='J':
            result.append('I')
        else:
            result.append(c)
flag=0
for i in range(65,91): #untuk menyimpan karakter lainnya
    if chr(i) not in result:
        if i==73 and chr(74) not in result:
            result.append("I")
            flag=1
        elif flag==0 and i==73 or i==74:
            pass    
        else:
            result.append(chr(i))
k=0
matrix_sev=matrix(5,5,0) # untuk inisialisasi matriks
for i in range(0,5): #untuk membuat matriks
    for j in range(0,5):
        matrix_sev[i][j]=result[k]
        k+=1

def locindex(c): #Fungsi untuk mendapat lokasi dari karakter
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(matrix_sev):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt():  #Enkripsi
    msg=str(input("Masukkan Teks anda: "))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("Cipher Text:",end=' ')
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(matrix_sev[(loc[0]+1)%5][loc[1]],matrix_sev[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(matrix_sev[loc[0]][(loc[1]+1)%5],matrix_sev[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(matrix_sev[loc[0]][loc1[1]],matrix_sev[loc1[0]][loc[1]]),end=' ')    
        i=i+2
    return encrypt
                 
def decrypt():  #Dekripsi
    msg=str(input("masukkan Cipher Text: "))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    print("Plain Text: ",end=' ')
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(matrix_sev[(loc[0]-1)%5][loc[1]],matrix_sev[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(matrix_sev[loc[0]][(loc[1]-1)%5],matrix_sev[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(matrix_sev[loc[0]][loc1[1]],matrix_sev[loc1[0]][loc[1]]),end=' ')    
        i=i+2              
    return decrypt
      

def main():
    print("--------------- PLAYFAIR CHIPER ---------------")
    encrypted_msg = encrypt()
    print(encrypted_msg)
    decrypted_msg = decrypt()
    print(decrypted_msg)


if __name__ == "__main__":
    main()