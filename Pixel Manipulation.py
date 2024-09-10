from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pix = img.load()

    wid, he = img.size

    for i in range(wid):
        for j in range(he):
            r, g, b = pix[i, j]

            # swapping red and blue channels
            encrypted_pixel = (b, g, r)

            pix[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pix = img.load()

    wid, he = img.size

    for i in range(wid):
        for j in range(he):
            r, g, b = pix[i, j]

            # swapping red and blue channels back
            decrypted_pixel = (b, g, r)

            pix[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")

 # image path
input_image = r"D:\Wallpapers\Earth.jpg"
encrypted_image = r"D:\Wallpapers\Earth.jpg"
decrypted_image = r"D:\Wallpapers\Earth.jpg"

try:
    n = int(input("Enter 1 to encrypt or 2 to decrypt: "))
    if n == 1:
        encrypt_image(input_image, encrypted_image, key = None)
    elif n == 2:
        decrypt_image(encrypted_image, decrypted_image, key = None)
    else:
        print("Invalid input. Please enter 1 or 2.")
except ValueError:
    print("Invalid input. Please enter a number.")
