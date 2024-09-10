def caesar_cipher(plaintext, shift, da):
    res = ""
    shift_direction = shift if da == 'e' else -shift

    for char in plaintext:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            res += chr((ord(char) - start + shift_direction) % 26 + start)
        else:
            res += char
    return res

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    da = input("Select E for Encryption or D for Decryption: ").lower()

    while da not in ['e', 'd']:
        da = input("Invalid input. Select E for Encryption or D for Decryption: ").lower()

    res = caesar_cipher(message, shift, da)
    print(f"Message: {res}")

if __name__ == "__main__":
    main()
