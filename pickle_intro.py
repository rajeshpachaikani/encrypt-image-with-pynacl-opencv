import pickle

x = b'some random data'

with open('pickle.bin', 'wb') as f:
    obj = pickle.dumps(x)
    print(obj)
    f.write(obj)

with open('pickle.bin', 'rb') as f:
    new_obj = f.read()
    print(new_obj)

print(pickle.loads(new_obj))