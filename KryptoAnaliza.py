import pandas as pd
from collections import Counter


def getMatches(data, checks=100_000):
    matches = {}
    for index, row in data.iterrows():
        cipher = row['cipher'].split(' ')
        sentence = row['sentence'].split(' ')
        for i in range(8):
            matches[cipher[i]] = sentence[i]
        print(f'Iteration: {index}')
        if index >= checks:
            print('Loaded')
            break
    print('-' * 50)
    return matches


def decode(matches, toDecode, decoded):
    timesReplaced = []
    for k, v in matches.items():
        if k in toDecode.split(' ') and k not in timesReplaced:
            toDecode = toDecode.replace(k, v)
            timesReplaced.append(v)
    if toDecode == decoded:
        return True
    return False, toDecode


def CheckCorrect(matches, checks):
    isCorrectList = []
    for x in range(checks):
        print(f'Iteration: {x}')
        isCorrect = decode(matches, list(matches.keys())[-x], list(matches.values())[-x])
        if isCorrect:
            isCorrectList.append(True)
        else:
            isCorrectList.append(False)
            print(f'Failed at {x}')
            print(list(matches.keys())[-x], list(matches.values())[-x])
    return isCorrectList


def ManualCheck(matches, checks, test1):
    isCorrectList = []
    for x in range(checks):
        print(f'Iteration: {x}')
        isCorrect = decode(matches, test1[x], test1[x])
        if isCorrect:
            isCorrect = isCorrect[1]
        isCorrectList.append(isCorrect)
    return isCorrectList


# name the .csv file as data.csv
data = pd.read_csv('data.csv')

matches = getMatches(data, 50_000)

test1 = ['YIR OPYAIPL HUDBYRXNPF OYWXFL SVWPB DMQUI BEVYTL BQXOJIYD',
         'IITXIO AIDBRJJ RCTVYXIOT FJMXMOM BIEFJNTX WHDSTMF NWUGTL ZRPWT',
         'IIB LJX GJTQJJ BIUOM WSPQXOEV RVNHYE UFTKTX AFZY',
         'JVBINNYGUUFB GJHORZ GIHFP AJQ SOWDHH NWUTTYD GI VSEJ',
         'OSB LDST KVJNK IQO HPOTJLL FQMEMATL BBFVKTX MJCNBM',
         'XVELIIY UVCSWT SYLDATLFE BOKWCN XZO NMSZITUL STWFTQFXZAS ZFGF']

# uncomment the next line for checking if the matches are correct in the data.csv file
# print(Counter(CheckCorrect(matches, 100)))
#
# # uncomment the next 6 lines for checking if the matches are correct in the test1 list
list1 = ManualCheck(matches, 6, test1)

print('-' * 50)

for x in list1:
    print(x)
