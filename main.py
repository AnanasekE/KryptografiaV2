from collections import Counter
from random import randint

plainText = 'Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol ' \
            'slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba.'.upper()
cipherText = ''


def caesarCipher(plainText, shift):
    cipher = ''
    for char in plainText:
        if char.isalpha():
            char = char.upper()
            cipher += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher += char
    return cipher


minDifference = float('inf')
bestShift = None
for iteration in range(26):
    cipherText = caesarCipher(plainText, iteration)
    freqPlain = Counter(plainText)
    freqCipher = Counter(cipherText)
    print('Iteration: ', iteration)
    print('Plain Text: ', plainText)
    print('Cipher Text: ', cipherText)
    print('Plain Text Frequency: ', freqPlain)
    print('Cipher Text Frequency: ', freqCipher)
    diff = []
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        diff.append(abs(freqCipher[char] / len(cipherText) - freqPlain[char]))
    sumOfDifferences = sum(diff)
    if sumOfDifferences < minDifference:
        minDifference = sumOfDifferences
        bestShift = iteration
    print(f'Difference: {sumOfDifferences}')
    print('-' * 50)
print('Best Shift: ', bestShift)
print('Min Difference: ', minDifference)
