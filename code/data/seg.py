from pyhanlp import *
# get the origin data
def getTheOriginData(path):
    with open(path) as file_object:
        contents = file_object.read()
    ##split the data by line
    lines = contents.split('\n')
    ##the labels
    labels = []
    ##the pairslist which is store the pairs
    pairslist = []
    ##get the pairs and the labels
    for line in lines:
        if len(line) == 0:
            continue
        line = line.replace(' ', '').replace('﻿','')
        pairs = []
        strs = line.split('\t')
        labels.append(strs[3])
        pairs.append(strs[1])
        pairs.append(strs[2])
        pairslist.append(pairs)

    return labels, pairslist

def seg(pairslists):
    segLists = []
    for pairslist in pairslists:
        segList = []
        src = pairslist[0]
        susp = pairslist[1]
        segList.append(analyzer.seg(src))
        segList.append(analyzer.seg(susp))
        segLists.append(segList)
    return segLists


PerceptronLexicalAnalyzer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')
analyzer = PerceptronLexicalAnalyzer()

##get the data
##get the train data
ori_trainPath = '/home/cks/PycharmProjects/ATEC/data/atec_nlp_sim_train.csv'
train_labels, train_pairslist = getTheOriginData(ori_trainPath)

segLists = seg(train_pairslist)
with open('/home/cks/PycharmProjects/ATEC/data/seg.txt', 'w') as fs:
    for i in range(len(segLists)):
        segList = segLists[i]
        label = train_labels[i]
        src = segList[0]
        susp = segList[1]
        fs.write(label+'\t'+str(src)+'\t'+str(susp)+'\n')



# tagedFile = '/home/cks/PycharmProjects/ATEC/data/tagged.txt'
# writeTagedContent(train_pairslist,tagedFile)
# ['r', 'd', 'v', 'nz', 'u', 'n', 'f', 'w', 't', 'y', 'ad', 'vn', 'm', 'p', 'a', 'j', 'b', 'an', 'q', 'c', 's', 'Ng', 'i', 'nr', 'Tg', 'Vg', 'j', 'l', 'nx', 'z', 'vd', 'n]', 'Ag', 'ns', 'k', 'Mg', 'o', 'Bg', 'nt', 'Dg', 'h', 'e']