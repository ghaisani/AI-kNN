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

dataTrain = loadFile("A.csv")
dataTest = loadFile("B.csv")

k = 233
correct = 0
inCorrect = 0
i = 1
ac = []

for data in dataTest:
    result = classify(k, dataTrain, data)
    if (result == data[4]):
        correct += 1
    else:
        inCorrect += 1
    print "Berita-",i," = fact : ",int(data[4]), ", predict : ", result
    i += 1
akurasi = float(correct) / (correct + inCorrect) * 100
ac.append([k,akurasi])
print "Akurasi = ", akurasi , "%"