from collections import Counter
from random import randint


def ceasarCipher(cipherText, shift):
    cipher = ''
    for char in cipherText:
        if char.isalpha():
            char = char.upper()
            cipher += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher += char
    return cipher


# inputText = 'Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm
# aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba.'.upper()
inputText = input('Enter the cipher text: ').upper()

# testShift = randint(0, 25)

# inputText = ceasarCipher(inputText, testShift)

british_english_frequencies = {
    'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31,
    'N': 6.95, 'S': 6.28, 'R': 6.02, 'H': 5.92, 'D': 4.32,
    'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30,
    'Y': 2.11, 'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49,
    'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10,
    'Z': 0.07
}

minDifference = float('inf')
bestShift = None

for key in range(26):
    inputCipher = ceasarCipher(inputText, key)
    freqInput = Counter(inputCipher)
    print('Iteration: ', key)
    print('Input Text: ', inputText)
    print('Cipher Text: ', inputCipher)
    diff = []
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        diff.append(abs(british_english_frequencies[char] - freqInput[char]) / 26)
    sumOfDifferences = sum(diff)
    if sumOfDifferences < minDifference:
        minDifference = sumOfDifferences
        bestShift = key
    print(f'Difference: {sumOfDifferences}')
    print('-' * 50)
print('Best Shift: ', bestShift)
print('Min Difference: ', minDifference)
print('Decrypted Text: ', ceasarCipher(inputText, bestShift))
# print('Test Shift: ', testShift)