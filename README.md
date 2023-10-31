# Hybrid Caesar and Playfair Cipher
This is a Python implementation of a hybrid Caesar and Playfair cipher. A hybrid cipher is a cipher that combines two or more existing ciphers to create a more secure cipher.

## How it works:

The hybrid Caesar and Playfair cipher works by first encrypting the message with the Caesar cipher and then encrypting the encrypted message with the Playfair cipher. This makes the message more difficult to decrypt, as an attacker would need to break both ciphers in order to read the message.

## To use:

To use the hybrid Caesar and Playfair cipher, simply pass the message and the keys for the Caesar cipher and Playfair cipher to the **final_enc()** function. To decrypt the message, pass the encrypted message and the keys for the Caesar cipher and Playfair cipher to the **final_dcr()** function.

## Code Breakdown:

### Imports:
    import caesar_cipher as cc
    import playfair_cipher_decrypt as pd
    import playfair_cipher_encrypt as pe

### Variables:
    caesar_key = 3
    playfair_key = 'victory'
    message = 'indonesia merdeka'
    
<br>You are declaring three variables:
- caesar_key: This is the key for the Caesar cipher.
- playfair_key: This is the key for the Playfair cipher.
- message: This is the message that you want to encrypt and decrypt.

### Functions:
    def final_enc(caesar_key, playfair_key, message):
        return pe.final(playfair_key, cc.enc(caesar_key, message))

    def final_dcr(caesar_key, playfair_key, enc_message):
        return cc.dcr(caesar_key, pd.final(playfair_key, enc_message))

<br>You are defining two functions:

- final_enc(): This function encrypts the message using the hybrid Caesar and Playfair cipher. It takes the Caesar cipher key, the Playfair cipher key, and the message as input and returns the encrypted message as output.
- final_dcr(): This function decrypts the message encrypted with the hybrid Caesar and Playfair cipher. It takes the Caesar cipher key, the Playfair cipher key, and the encrypted message as input and returns the decrypted message as output.

### Main code:
      print(message)

      enc_message = final_enc(caesar_key, playfair_key, message)
      print(enc_message)

      dcr_message = final_dcr(caesar_key, playfair_key, enc_message)
      print(dcr_message)

In the main code, you are first printing the message to the console. Then, you are encrypting the message using the final_enc() function and printing the encrypted message to the console. Finally, you are decrypting the encrypted message using the final_dcr() function and printing the decrypted message to the console.

Output Example :
<br> ![img1](https://github.com/MuhammadAinurR/hybrid-caesar-playfair-cipher/blob/main/output%20hybrid/output1.png)
<br> ![img2](https://github.com/MuhammadAinurR/hybrid-caesar-playfair-cipher/blob/main/output%20hybrid/output2.png)
