import hashlib 
print("**************PASSWORD CRACKER ******************") 
pass_found = 0 # To check if the password  found or not
input_hash = input("Enter the hashed password:")
pass_doc = input("\nEnter passwords filename including path(root / home/): ")
pass_file = open(pass_doc, 'r')                
  
for word in pass_file:  # comparing the input_hash with the hashes of the words in password file
    enc_word = word.encode('utf-8')   
    hash_word = hashlib.md5(enc_word.strip())    
    digest = hash_word.hexdigest()  # digesting that hash into a hexa decimal value
    if digest == input_hash:  
        print("Password found.\nThe password is:", word)  # comparing hashes
        pass_found = 1
        break

if not pass_found:
    print("Password is not found in the", pass_doc, "file")    
    print('\n') 
print("*****************  Thank you  **********************")
