from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA

mailPath = r"C:\\Users\\Home\\PycharmProjects\repl.it\\PGP\\mail.txt"
signaturePath = r"C:\\Users\\Home\\PycharmProjects\repl.it\\PGP\\signature.txt"
mailFile = open(mailPath, 'rb')  # 'rb'
sigFile = open(signaturePath, 'wb')

key = RSA.import_key(open('private.pem').read())

h = SHA256.new(b'f')
signature = pkcs1_15.new(key).sign(h)

sigFile.write(signature)
sigFile.close()
mailFile.close()

print(key)
print(mailFile)
print(sigFile)

