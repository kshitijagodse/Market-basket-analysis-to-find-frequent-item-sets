import itertools
from collections import Counter
from collections import defaultdict
from random import randint

import sys
l1=sys.argv

def recFuction(i, j, aa, SpportBucket):
    # print "----------------Inside rec function-------------------------"
    if (aa > 0 and SpportBucket.keys()[i][aa] == SpportBucket.keys()[j][aa]):
        # print SpportBucket.keys()[i][aa]
        # print SpportBucket.keys()[j][aa]
        aa -= 1
        recFuction(i, j, aa, SpportBucket)
    if (aa == 0 and SpportBucket.keys()[i][aa] == SpportBucket.keys()[j][aa]):
        # print SpportBucket.keys()[i][aa]
        # print SpportBucket.keys()[j][aa]
        newTuple = SpportBucket.keys()[i] + SpportBucket.keys()[j]
        # print newTuple
        newTuple = set(newTuple)
        return newTuple

mainCount = 0
data = [line.strip().split(",") for line in open(l1[1],'r')]
countData = float(len(data))
# print "-----------------------hi-----------------------------"
# print countData

minSupport =int(l1[2])
randomNumber = 10
iteration = 1
while mainCount < 100:

    # randomNumber = (randint(0,len(data)))

    fraction = float(randomNumber)
    # p = fraction/countData
    p = 1/fraction
    # print p
    sampleData = itertools.islice(data, fraction)
    sampleSupport = 0.8* minSupport * p
    # print sampleSupport
    sampleD = list()
    for x in sampleData:
         sampleD.append(x)


    # sampleData = list(sampleData)
    #print "----------------------------This is a Sample Data-----------------------------------------------"
    #print sampleD
    merged = list(itertools.chain.from_iterable(sampleD))
    #print merged
    distinct = list(set(merged))

    singleton = Counter(merged)
    # print singleton
    frequents =[]
    negativeBorder=[]
    SingletonBucket = defaultdict(lambda: 0)
    negatives = defaultdict(lambda: 0)
    for s in singleton.keys():
        if (singleton[s] >= sampleSupport):
            SingletonBucket[s] = singleton[s]
            # else:
            # print "this is elsee"
        else:
            negatives[s] = singleton[s]
            # print negatives

    #frequents = SingletonBucket.keys()
    #To Come out of loop if no new frequent items are returned
    #l = len(SingletonBucket)
    if len(SingletonBucket) == 0:
        continue

    for x in SingletonBucket.keys():
        frequents.append(tuple(x))
    for x in negatives.keys():
        negativeBorder.append(tuple(x))


    # print SingletonBucket
    # print frequents
    # print negativeBorder
    # ---------------------------------------------------------------------------------------------------------------------------
    bucks3 = defaultdict(lambda: 0)
    pass2Bucket = SingletonBucket.keys()
    # print "this is pass 2 bucket----------------------"
    # print pass2Bucket
    j = itertools.combinations(pass2Bucket, 2)

    for v in j:
        for x in sampleD:
            if set(v).issubset(x):
                bucks3[v] += 1
                    #  print "this is mod function"
                    # print modFunction

    # print "---------------------This Tuple with counts in data file-----------------------------------------------------------"
    # print bucks3

    SpportBucket = defaultdict(lambda: 0)
    for s in bucks3.keys():
        if (bucks3[s] >= sampleSupport):
            SpportBucket[s] = bucks3[s]
            # else:
        else:
           Ng = itertools.combinations(s, len(s) - 1)
           for k in Ng:

                if set(k).issubset(set(frequents)):
                    flag = 1
                else:
                    flag = 0
                    break

           if flag == 1:
                 negativeBorder.append(s)




            # print "this is elsee"
    # print "------------this is supportBucket after pruning----------------------------------------------"
    # print SpportBucket
    # ---------------------------------------------------------------------------------------------------------------------------
    if len(SpportBucket) != 0:

        for x in SpportBucket.keys():
            frequents.append(x)



        passNo = 3
        while True:

            newTuple1 = list()
            aa = (passNo - 2) - 1
            # print "---------------------------------Inside While loop 1------------------------------------------"
            # print aa
            for i in range(0, len(SpportBucket)):
                # print SpportBucket.keys()[i]
                for j in range(i + 1, len(SpportBucket)):
                    newTuple1.append(recFuction(i, j, aa, SpportBucket))
                    # print newTuple1
                    newTuple1 = filter(None, newTuple1)



            # Making Dictionary with sample data
            d11 = defaultdict(lambda: 0)
            for var in newTuple1:
                for dataVar in sampleD:
                    if (var).issubset(dataVar):
                        d11[tuple(var)] += 1

            # print "----------------------------HI d11------------------------------------------------------------------"
            # print  d11
            # print "-----------------------------------------------------------------------------------------------"

            #Adding the value to frequent list and negative list
            SpportFinalB = defaultdict(lambda: 0)
            forNeg = defaultdict(lambda: 0)
            for s in d11.keys():
                if (d11[s] >= sampleSupport):
                    SpportFinalB[s] = d11[s]
                    # else:
                    # print "this is elsee"
                else:
                    Ng = itertools.combinations(s, len(s) - 1)
                    for k in Ng:

                        if set((k,)).issubset(set(frequents)):
                            flag = 1
                        else:
                            flag = 0
                            break

                    if flag == 1:
                        negativeBorder.append(s)

            #To break from the loop if frequent list is empty

            if len(SpportFinalB) == 0:
                 break


            SpportBucket = SpportFinalB
            for l in SpportFinalB.keys():
                frequents.append(l)
            passNo += 1


    # print negativeBorder
    # print frequents
    goToMainWhile = 0
    NegCheck = defaultdict(lambda: 0)

    for var in negativeBorder:
        for dataVar in data:
            if (set(var)).issubset(set(dataVar)):
                NegCheck[tuple(var)] += 1

    TestNeg = defaultdict(lambda: 0)
    for s in NegCheck.keys():
        if (NegCheck[s] >= minSupport):
            goToMainWhile = 1
            randomNumber += 5
            iteration += 1
            break



    if goToMainWhile == 1:
        continue
    else:
        break









    # Print the final frequent list if the no new smapling is required

finalFrequents = list()

FreqCheck = defaultdict(lambda: 0)
for k in frequents:
    for dataVar in data:
        if (set(k)).issubset(dataVar):
            FreqCheck[tuple(k)] += 1

for r in FreqCheck.keys():
    if (FreqCheck[r] >= minSupport):
        finalFrequents.append(r)

# print "Final Results"
# print sorted(finalFrequents)
print iteration
print p
maxsize=max(sorted([len(list(a)) for a in (finalFrequents)]))
finalsorted= sorted([list(a) for a in (finalFrequents)])
for i in range(1,maxsize+1):
    l=[]
    for x in finalsorted:
        if (len(x)==i):
            l.append(x)
    print l
    print





