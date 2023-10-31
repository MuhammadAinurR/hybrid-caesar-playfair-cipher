import caesar_cipher as cc
import playfair_cipher_decrypt as pd
import playfair_cipher_encrypt as pe


caesar_key = 3
playfair_key = 'victory'
message = 'indonesia merdeka'

def final_enc(caesar_key, playfair_key, message):
    return pe.final(playfair_key, cc.enc(caesar_key, message))

def final_dcr(caesar_key, playfair_key, enc_message):
    return cc.dcr(caesar_key, pd.final(playfair_key, enc_message))


print(message)

enc_message = final_enc(caesar_key, playfair_key, message)
print(enc_message)

dcr_message = final_dcr(caesar_key, playfair_key, enc_message)
print(dcr_message)





