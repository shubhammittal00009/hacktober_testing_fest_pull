# Affine Cipher

def egcd(a, b): 
    x,y, u,v = 0,1, 1,0
    while a != 0: 
        q, r = b//a, b%a 
        m, n = x-u*q, y-v*q 
        b,a, x,y, u,v = a,r, u,v, m,n 
    gcd = b 
    return gcd, x, y 

def modularInverse(a, m):
    new_temp = 5
    gcd, x, y = egcd(a, m) 
    if gcd != 1: 
        return None
    else: 
        return x % m 

def affine_encrypt(text, key):
    ''' 
    C = (a*P + b) % 26 
    '''
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) 
                + ord('A')) for t in text.upper().replace(' ', '') ]) 


def affine_decrypt(cipher, key): 
    ''' 
    P = (a^-1 * (C - b)) % 26 
    '''
    return ''.join([ chr((( modularInverse(key[0], 26)*(ord(c) - ord('A') - key[1])) 
                    % 26) + ord('A')) for c in cipher ]) 


text = str(input("Enter Text : "))
key = [17, 20]

affine_encrypted_text = affine_encrypt(text, key) 
print("Encrypted Text: " + affine_encrypted_text) 

decryptedText = affine_decrypt(affine_encrypted_text, key)
print("Decrypted Text: " +  decryptedText) 
