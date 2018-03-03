import csv, math
from operator import itemgetter

def loadFile(fileName):
    result = []
    with open(fileName,'rb') as csvfile:
        read = csv.reader(csvfile, delimiter=',')
        next(read)
        for row in read:
            result.append([float(i) for i in row])
    return result

def euclide(dataTrain, dataTest):
    jarak = 0
    i = 1
    while (i < len(dataTrain) - 1):
        jarak += (dataTrain[i] - dataTest[i]) ** 2
        i += 1
    return math.sqrt(jarak)

def classify(k, dataTrain, dataTest):
    distance = []
    for data in dataTrain:
        resultEuc = euclide(data, dataTest)
        label = data[4]
        distance.append([resultEuc, label])
    distSorted = sorted(distance, key=itemgetter(0))[:k]
    hoax = 0
    nohoax = 0
    for data in distSorted:
        if (data[1]) == 1:
            hoax += 1
        else:
            nohoax += 1
    return 1 if hoax > nohoax else 0

with open('ResultTesting.csv', 'wb') as csvfile:
    read = csv.writer(csvfile, delimiter=',')
    read.writerow(['Like', 'Provokasi', 'Komentar', 'Emosi', 'Hoax', 'Berita'])
    dataTrain = loadFile("A.csv")
    dataTest = loadFile("DataTest.csv")

    k = 223
    j = 1
    for data in dataTest:
        result = classify(k, dataTrain, data)
        rowData = list(data)
        rowData.append(result)
        rowData.append(j)
        j += 1
        read.writerow(rowData)
        print rowData