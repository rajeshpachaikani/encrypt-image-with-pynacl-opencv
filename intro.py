import nacl.utils
import nacl.secret


def generate_key():
    with open('secret.bin', 'wb') as f:
        key = (nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE))
        f.write(key)


def get_key():
    with open('secret.bin', 'rb') as f:
        key = f.read()
        print(key)
    return key


key = get_key()
box = nacl.secret.SecretBox(key)

data = b'Secret info'
print("Original Data::", data)

encrypted_data = box.encrypt(data)
print("Encrypted data::", encrypted_data)

decrypted_data = box.decrypt(encrypted_data)
print("Decrypted data::", decrypted_data)
