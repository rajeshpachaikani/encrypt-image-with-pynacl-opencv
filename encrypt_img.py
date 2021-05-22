import pickle
import cv2
import nacl.secret
import nacl.utils

img = cv2.imread('1_16.bmp')
cv2.imshow('Input image',img)
pickled_img = pickle.dumps(img)

def get_key():
    with open('secret.bin', 'rb') as f:
        key = f.read()
        print(key)
    return key

key = get_key()
box = nacl.secret.SecretBox(key)
encrypted = box.encrypt(pickled_img)

with open('img.bin', 'wb') as f:
    f.write(encrypted)

with open('img.bin', 'rb') as f:
    data_from_file = f.read()


decrypted_data = box.decrypt(data_from_file)

img_decrypted = pickle.loads(decrypted_data)

print(img_decrypted)
print(type(img_decrypted))
cv2.imshow('Decrypted', img_decrypted)
cv2.waitKey(0)
