## Original version done by - Vishnu Kumar a.k.a Victor_2134

import numpy as np
from numpy.linalg import inv
np.set_printoptions(suppress=True)

#Function to get Encryption matrix from the given file
def SetEncryptionMatrix():
    M = char[3].replace('[','').replace(',','').replace("'",'').replace(']','')
    M = np.fromstring(M,dtype = int,sep = ' ')
    M = np.reshape(M,(4,4))
    M = np.round(M,)
    return M

## Function to create a Dictionary from the given characters used for encryption
def CharList(x):
    Tx = x[1]       # Line in which the characters used are present
    y = { }         # Creating a dictionary to store the characters used for encryption
    for i in range(len(Tx)):
        y[Tx[i]] = i         #Key - Character ; Value - Number
        y[i] = Tx[i]         #Key - Number ; Value - Character
    return y

## Function to find the inverse mod of the given number by iterative method
def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

## Function to find the inverse of the given Encryption matrix by using the formula
## A^-1 = {([det(A)]%ChLen)^-1 * [adj(A)%ChLen]}%ChLen
## Where, ChLen is the number of characters used for encryption
def FindInverse(x,mod):
    xdet = np.round(np.linalg.det(x)) % mod
    a = modInverse(xdet,mod)
    y = inv(x)*np.linalg.det(x)     # A^-1 = (det(A))^-1 * adj(A)  => adj(A) = A^-1 * det(A)
    y = np.mod(y,mod)
    y = y*a
    y = np.mod(y,mod)
    return y.round()

##  Decryption function - Converts each Encrypted char to int based on their index in the given character list.
##  After convertion,they are grouped as "blocks",whose size is determined by the number of columns in the encryption matrix,
##  and stored in a NumPy array.This matrix is passed to the convert function
def Decrypt(x):
    c = 0       # count the characters
    k = 0       # for array index
    Block = EnMat.shape[1]
    Blocks = np.zeros(Block,dtype = int)   # Making a empty array to store the character index from the encrypted file
    for i in x:                            # x - encrypted file ; i - individual lines in the file
        for j in i:                        # j - character in each line
            c+=1
            Blocks[k] = EnChar[j]          # Store the character index to the multplication matrix
            k+=1
            if c % Block == 0:
                convert(Blocks)
                k = 0

##  The given block matrix is multiplied with the decryption matrix(dot product) and the result is taken modulus of
##  <length of the used characters>. The numbers in the result matrix is the index of the characters after decryption,
##  Hence the respective characters are then written into the file
def convert(x):
    DCchar = (DCmat @ x) % len(char[1])
    for i in DCchar:
        DCfile.write(EnChar[i])
        
## Driver code
ECfile = open("Encrypted_File.txt")
DCfile = open("Decrypted.txt","w")
char = ECfile.readlines()
EnChar = CharList(char)                    # Dictionary where the characters used for encryption is stored
EnMat = SetEncryptionMatrix()
DCmat = FindInverse(EnMat,len(char[1]))    # Decryption matrix = inverse of Encryption Matrix 
Decrypt(char[5:])                          # Passing lines after 5 because the encrypted file starts from line 6
ECfile.close()
DCfile.close()
