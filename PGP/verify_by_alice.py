from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA

mailPath = r"C:\\Users\\Home\\PycharmProjects\repl.it\\PGP\\mail.txt"
signaturePath = r"C:\\Users\\Home\\PycharmProjects\repl.it\\PGP\\signature.txt"
mailFile = open(mailPath, 'rb')  # 'rb'
sigFile = open(signaturePath, 'rb')
key = RSA.import_key(open('private.pem').read())
h = SHA256.new(b'mailFile')
signature = pkcs1_15.new(key).sign(h)

try:
    pkcs1_15.new(key).verify(h, signature)
    print('Signature verified')

except:
    print('Signature not valid')











# >>> key = RSA.import_key(open('public_key.der').read())
# # >>> h = SHA.new(message)
# # >>> try:
# # >>>     pkcs1_15.new(key).verify(h, signature)
# # >>>     print "The signature is valid."
# # >>> except (ValueError, TypeError):
# # >>>    print "The signature is not valid.