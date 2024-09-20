import re

def checker(password):     
    length = len(password) >= 8     
    up = bool(re.search(r'[A-Z]', password))     
    lp = bool(re.search(r'[a-z]', password))     
    num = bool(re.search(r'[0-9]', password))     
    sp = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))      
    
    if length and up and lp and num and sp:         
        return "Strong password"     
    else:         
        feedback = "Weak password\n"         
        if not length:             
            feedback += "Password length is less than 8 characters\n"         
        if not up:             
            feedback += "Password does not contain an uppercase letter\n"         
        if not lp:             
            feedback += "Password does not contain a lowercase letter\n"         
        if not num:             
            feedback += "Password does not contain a number\n"         
        if not sp:             
            feedback += "Password does not contain a special character\n"         
        return feedback

def main():     
    password = input("Enter the password: ")     
    result = checker(password)     
    print(result)

if __name__ == "__main__":     
    main()
