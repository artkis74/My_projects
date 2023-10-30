import pyAesCrypt


password = input('Введите пароль для шифрования файла:')

# #encryption
pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)


#decryption
pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)
