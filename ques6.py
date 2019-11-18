def password_checker (passwd):

    sp_char = ( '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '_', '-', '{', '}',
'[', ']', ':', ';', '”', '’', '?', '<', '>', ',', '.' )
    psd = True
    if len(passwd) < 6:
        print(" length should be atleast 6 ")
        psd = False
    if len(passwd) > 24:
        print(" length should not be greater than 24 ")
        psd = False
    if not any(char.isdigit() for char in passwd):   
        print(" Password should have atleast one numeral ")    
        psd = False
    if not any(char.isupper() for char in passwd):
        print(" Password should have atleast one UpperCase Letter ")  
        psd = False 
    if not any(char.islower() for char in passwd):      
        print(" Password should have atleast one LowerCase Letter ")
        psd = False
    if not any(char in sp_char for char in passwd):
        print(" Password should have atleast one Special Character ")
        psd = False
    if psd:
        return psd

def main():
        passwd = str(input(" Enter your Password "))
        if(password_checker(passwd)):
           print(" Passwor is Valid ")
        else:
           print(" Invalid Password!!! ")  
main()             