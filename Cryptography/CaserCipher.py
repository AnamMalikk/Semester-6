# Implement Caeser cipher substitution operation.

def main():
    print("WELCOME TO CAESER CIPHER")
    choice = int(input("1. Encryption\n2. Decryption\nSelect 1 or 2 : "))

    if choice ==1:
        text = input("Enter the Plain text : ")
        k = int(input("Enter the key value : "))
        print("CIPHER: "+ encrypt_func(text,k))
    elif choice ==2:
        text = input("Enter the Plain text : ")
        k = int(input("Enter the key value : "))
        k = 26-k
        print("CIPHER: "+ decrypt_func(text,k))
    else:
        print("Wrong Choce!")
       
       
def encrypt_func(text,k):
    result=""
   
    #traverse the plain text
    for i in range(len(text)):
        char=text[i]
       
        # for uppercase letter
        if(char.isupper()):
            result += chr((ord(char)+k-65)%26+65)
           
        # for lowercase letter
        else:
            result += chr((ord(char)+k-97)%26+97)
           
    return result


def decrypt_func(text, k):
    result=""
   
    #traverse the plain text
    for i in range(len(text)):
        char=text[i]
       
        # for uppercase letter
        if(char.isupper()):
            result += chr((ord(char)+k-65)%26+65)
           
        # for lowercase letter
        else:
            result += chr((ord(char)+k-97)%26+97)
           
    return result


       
   
if __name__ == "__main__":
    main()
