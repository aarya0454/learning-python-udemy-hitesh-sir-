def encrypt(message,key):
    result = ''
    for char in message:
         if char.isalpha():
             base = ord('A') if char.isupper() else ord('a')
             shifted  = (ord(char) - base + int(key)) % 26  + base
             result += chr(shifted)
         else:
             result += char
    return result
        
    

def decrypt(message,key):
     return encrypt(message,-int(key))
print("your secret text")
name = input("please enter E to incrypt or D to decrypt").strip().lower()
if name == 'e':
    try:
         message = input("Enter the text to encrypt")
         key = input("Please enter the key between 1 to 25:  ")
         encrypted = encrypt(message,key)
         print("your encrypted text")
         print(encrypted)
    except ValueError:
        print("key error ")
elif name == 'd':
    try:
         message = input("Enter the text to decrypt")
         key = input("Please enter the key between 1 to 25:  ")
         decrypted = decrypt(message,key)
         print("your encrypted text")
         print(decrypted)
    except ValueError:
        print("key error ")
