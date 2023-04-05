import sqlite3
import hashlib

conn = sqlite3.connect('users-challenge (1).db')

c = conn.cursor()
hashes = []
found = 0
currLine = 0
for row in c.execute('SELECT * FROM users'):
    hashes.append(row)

# open file rockyou.txt and real all lines
with open('rockyou.txt', 'rb') as f:
    for line in f:
        line = line.strip()

        hashed = hashlib.md5(line).hexdigest()
        hashed2 = hashlib.sha1(line).hexdigest()
        hashed3 = hashlib.sha224(line).hexdigest()
        hashed4 = hashlib.sha256(line).hexdigest()
        hashed5 = hashlib.sha384(line).hexdigest()
        hashed6 = hashlib.sha512(line).hexdigest()
        hashed7 = hashlib.sha3_224(line).hexdigest()
        hashed8 = hashlib.sha3_256(line).hexdigest()
        hashed9 = hashlib.sha3_384(line).hexdigest()
        hashed10 = hashlib.sha3_512(line).hexdigest()
        hashed11 = hashlib.blake2b(line).hexdigest()
        hashed12 = hashlib.blake2s(line).hexdigest()

        for user in hashes:
            currLine += 1
            if hashed in user[3] or hashed2 in user[3] or hashed3 in user[3] or hashed4 in user[3] or hashed5 in user[
                3] or hashed6 in user[3] or hashed7 in user[3] or hashed8 in user[3] or hashed9 in user[
                3] or hashed10 in user[3] or hashed11 in user[3] or hashed12 in user[3]:
                found += 1
                print(f'Password found: {line, user[3]} user: {user[1]}')
                continue
            if found == 25:
                break
            continue

print(f'Passwords found: {found}')
