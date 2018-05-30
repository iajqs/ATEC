# get the seg data
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
        strs = line.split('\t')
        labels.append(strs[0])
        pairslist.append(strs[1])

    return labels, pairslist

ori_trainPath = '/home/cks/PycharmProjects/ATEC/data/segFeature.txt'
train_labels, train_pairslist = getTheOriginData(ori_trainPath)

