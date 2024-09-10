import re

def checker(pass):
    length = len(pass) >= 8
    up = bool(re.search(r'[A-Z]',pass))
    lp = bool(re.search(r'[a-z]',pass))
    num = bool(re.search(r'[0-9]',pass))
    sp = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', pass))
    
    if length and up and lp and num and sp:
        return "Strong pass"
    else:
        feedback = "Weak pass \n"
        if not length:
            feedback = feedback + "pass length is less than 8 \n"
        if not up:
            feedback = feedback + "pass does not contain the uppercase \n"
        if not lp:
            feedback = feedback + "pass does not contain the lowercase \n"
        if not num:
            feedback = feedback + "pass does not contain the num \n"
        if not sp:
            feedback = feedback + "pass does not contain the special character \n"
        return feedback

def main():
    pass = input("Enter the pass: ")
    result = checker(pass)
    print(result)

if __name__ == "__main__":
    main()
