#Caesar's Cipher

#Global list letters used to encrypt and decrypt
global letters

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Function used for encryption
def encrypt():

    global letters
    
    #Getting message and key from user
    message = input("Enter your message:\n")

    key = int(input("Enter the key number (1-26)\n"))

    new_string = ""

    #Iterates through each character in the string 
    for char in message:
        
        #Finds the new letter in the letters list (if it is present in the list) and adds the key to get the new letter
        if char in letters:
            
            letter_index = letters.index(char)

            new_letter = letters[(letter_index + key) % 52]
        
        #If the character is not in the alpahbet, the new letter is just the character
        else:

            new_letter = char
        
        #Appending each new character to the new string
        new_string += new_letter

    
    print("Your translated text is:")
    
    print(new_string)


#Function used for decryption
def decrypt():

    #This function applies the same logic as the encrypt function, only this time the key is subtracted from the character in the message to get the 
    #decrypted character
    global letters
    
    message = input("Enter your message:\n")

    key = int(input("Enter the key number (1-26)\n"))

    new_string = ""

    for char in message:
        
        if char in letters:
            
            letter_index = letters.index(char)

            new_letter = letters[(letter_index - key) % 52]
        
        else:

            new_letter = char
        
        
        new_string += new_letter

    
    print("Your translated text is:")
    
    print(new_string)
    
#Function used to brute force an encrypted message
def brute_force():

    global letters
    
    #Getting the encrypted message from the user
    message = input("Enter your message:\n")

    print("Your translated text is: ")

    #Iterates through all possible values of the key
    for key in range(1,26):
        
        new_string = ""

        #Iterates through each character in the message
        for char in message:
            
            #if a character in the alphabet is found in the message, 
            # the key is subtracted from the character's index in the list of letters in order to get the decrypted letter
            if char in letters:
            
                letter_index = letters.index(char)

                new_letter = letters[(letter_index - key) % 52]

            #characters not in the alphabet do not change
            else:

                new_letter = char
        

            #appending each new character to the decrypted string
            new_string += new_letter

        #Outputting the key along with each decrypted message it produces
        print(f"{key} {new_string}")


#Main function      
def main():
    operation = input("Would you like to encrypt, decrypt or brute force a message?\n")

    if operation.lower() == "encrypt":
        
        encrypt()
    
    elif operation.lower() == "decrypt":
       
        decrypt()
    
    elif operation.lower() == "brute":
        
        brute_force()
    
    else:
        
        print("invalid option.")
        main()
        


main()
