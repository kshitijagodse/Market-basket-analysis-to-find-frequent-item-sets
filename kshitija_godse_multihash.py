import itertools
from collections import Counter
from collections import defaultdict

import sys
l1=sys.argv
# f = open('/home/kgodse/PycharmProjects/DataMining/input.txt','r')
# v = f.read().splitlines()
# print v
# l = list()
# a = l.insert(v)
# print "---------------------------------------------------------------------------------------------"
data = [line.strip().split(",") for line in open(l1[1],'r')]


# data = map(int, data)
# wordlist = list(data)
#print data
merged = list(itertools.chain.from_iterable(data))
#print merged
distinct = list(set(merged))
# print "---------------------------------------------------------------------------------------------"
# print distinct
sort = sorted(distinct)
#print sort
backtoList = list(sort)
#print "this is list"
#print backtoList
listKey = list(range(1,len(backtoList)+1))
#print listKey
# d = dict()
d = zip(backtoList,listKey)
d = dict(d)
#print "this is dictionary"
#print d
#print d['a']
#print "---------------------------------------------------------------------------------------------"
indivisualSupport = Counter(merged)
#print indivisualSupport
# print Counter(merged)

# itertools.combinations([a,b,c],2)
# print support['a']

bucketSize = int(l1[3])
minSupport = int(l1[2])

bucks1=defaultdict(lambda :0)
bucks2=defaultdict(lambda :0)

def hashTable1(buckets,bucketSize):
    for i in buckets:

        v = itertools.combinations(i,2)
        for j in v:
           # print j
            numerator = 0
            for k in j:

                numerator = numerator + d[k]
          #  print numerator
            modFunction = numerator%bucketSize
          #  print "this is mod function"
           # print modFunction
            bucks1[modFunction]+=1
            modFunction=0
    print
    print dict(bucks1)

#hashTable1(data,bucketSize)

def functionBit1():
    biti = {}

    for i in range(0, bucketSize):
        if (bucks1[i] >= minSupport):
            biti[i] = 1
        else:
            biti[i] = 0

    return biti


def hashTable2(buckets,bucketSize):

    for i in buckets:

        v = itertools.combinations(i,2)
        # print v
        # print "combinationsmbinations"
        for j in v:
            # print j
            numerator = 0
            for k in j:

                numerator = numerator + d[k]
            # print numerator
            modFunction = (numerator+15)%bucketSize
          #  print "this is mod function"
           # print modFunction
            bucks2[modFunction]+=1
            modFunction=0
    print dict(bucks2)

#hashTable2(data,bucketSize)

def functionBit2():
    biti2 = {}

    for i in range(0, bucketSize):
        if (bucks2[i] >= minSupport):
            biti2[i] = 1
        else:
            biti2[i] = 0

    return biti2


def functionBitnew2(kpas):
    biti2 = {}

    for i in range(0, bucketSize):
        if (kpas[i] >= minSupport):
            biti2[i] = 1
        else:
            biti2[i] = 0

    return biti2

copySupport=defaultdict(lambda :0)
for s in indivisualSupport.keys():
    if (indivisualSupport[s]>=minSupport):
        copySupport[s] = indivisualSupport[s]
    # else:
        # print "this is elsee"
#print copySupport

bucks3=defaultdict(lambda :0)
pass2Bucket = copySupport.keys()


print sorted(pass2Bucket)

hashTable1(data,bucketSize)

hashTable2(data,bucketSize)

j = itertools.combinations(pass2Bucket, 2)
y = functionBit1()
z = functionBit2()
for v in j:
    numerator = 0
    for k in v:
        numerator = numerator + d[k]
        # print numerator
    modFunction1 = (numerator)%bucketSize
    modFunction2 = (numerator+15)%bucketSize
    if (y[modFunction1]==1 and z[modFunction2]==1):
        for x in data:
            if set(v).issubset(x):
                bucks3[v] += 1
      #  print "this is mod function"
       # print modFunction


# print "----------------------this is hashed bucket in pass 2-------------------------------------------------------------"
# print bucks3

SpportBucket=defaultdict(lambda :0)
for s in bucks3.keys():
    if (bucks3[s]>=minSupport):
        SpportBucket[s] = bucks3[s]
    # else:
        # print "this is elsee"
# print "------------this is supportBucket----------------------------------------------"

print sorted(SpportBucket.keys())
print

def recFuction(i,j,a,SpportBucket):
    if (a > 0 and SpportBucket.keys()[i][a] == SpportBucket.keys()[j][a]):
        # print SpportBucket.keys()[i][a]
        # print SpportBucket.keys()[j][a]
        a -= 1
        recFuction(i,j,a,SpportBucket)
    if (a==0 and SpportBucket.keys()[i][a] == SpportBucket.keys()[j][a]):
        newTuple = SpportBucket.keys()[i] + SpportBucket.keys()[j]
        # print newTuple
        newTuple = set(newTuple)
        return newTuple



passNo= 3
while True:
    finalBucks = defaultdict(lambda: 0)
    finalBucks1 = defaultdict(lambda: 0)
    for i in range(0,bucketSize):
        finalBucks[i]=0
        finalBucks1[i]=0
    newTuple1 = list()
    a = (passNo - 2)-1
    # print a
    for i in range(0,len(SpportBucket)):
        # print SpportBucket.keys()[i+1]
        for j in range(i+1, len(SpportBucket)):
            newTuple1.append(recFuction(i, j, a, SpportBucket))
            newTuple1 = filter(None, newTuple1)

    for x in newTuple1:
        ahe=1
        # print "this is x"
        # print list(x)
        Ng = itertools.combinations(list(x), len(list(x)) - 1)
        # list(Ng)
        # print "this is ng"
        a21 = [c for c in Ng]
        for k11 in a21:
            # print "this is k"
            # print k11

            if tuple(k11) not in (list(SpportBucket.keys())):
                ahe=0
                break

        if ahe==0:
            newTuple1.remove(x)

    if not newTuple1:

        # print newTuple1
        break




        # newTuple = SpportBucket.keys()[i]+SpportBucket.keys()[j]
    # print newTuple1

    for i in data:

        v = itertools.combinations(i, passNo)
        # print v
        # print "combinationsmbinations"
        for j in v:
            # print j
            numerator = 0
            for k in j:
                numerator = numerator + d[k]
            # print numerator
            modFunction = (numerator) % bucketSize
            #  print "this is mod function"
            # print modFunction
            finalBucks1[modFunction] += 1
            modFunction = 0
    # print "-9---------------------this is hash function final-------------------------------------------------------------"
    print dict(finalBucks1)

    bit1= functionBitnew2(finalBucks1)

    for i in data:

        v = itertools.combinations(i, passNo)
        # print v
        # print "combinationsmbinations"
        for j in v:
            # print j
            numerator = 0
            for k in j:
                numerator = numerator + d[k]
            # print numerator
            modFunction = (numerator + 15) % bucketSize
            #  print "this is mod function"
            # print modFunction
            finalBucks[modFunction] += 1
            modFunction = 0
    # print "----------------------this is hash function final-------------------------------------------------------------"
    print dict(finalBucks)

    bit2= functionBitnew2(finalBucks)
    d11=defaultdict(lambda: 0)
    for var in newTuple1:
        m1=sum([d[x] for x in var])
        if bit1[m1%bucketSize]==1 and bit2[(m1+15)%bucketSize]==1:
            for dataVar in data:
                if (var).issubset(dataVar):
                    d11[tuple(var)]+=1


    SpportFinalB = defaultdict(lambda: 0)
    for s in d11.keys():
        if (d11[s] >= minSupport):
            SpportFinalB[s] = d11[s]
            # else:
            # print "this is elsee"
    SpportBucket = SpportFinalB

    print sorted(SpportBucket.keys())
    print
    passNo += 1


