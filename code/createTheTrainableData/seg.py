
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
        pairs = []
        strs = line.split('\t')
        labels.append(strs[0])
        pairs.append(strs[1])
        pairs.append(strs[2])
        pairslist.append(pairs)

    return labels, pairslist

def getFeature(src, susp):
    src = src.replace('[', '').replace(']', '')
    susp = susp.replace('[', '').replace(']', '')

    src_items = src.split(', ')
    susp_items = susp.split(', ')

    features = {}
    items = ['r', 'd', 'v', 'nz', 'u', 'n', 'f', 'w', 't', 'y', 'ad', 'vn', 'm', 'p', 'a', 'j', 'b', 'an', 'q', 'c', 's', 'Ng', 'i', 'nr', 'Tg', 'Vg', 'j', 'l', 'nx', 'z', 'vd', 'n]', 'Ag', 'ns', 'k', 'Mg', 'o', 'Bg', 'nt', 'Dg', 'h', 'e']
    index = 0
    featuresMatrix = []
    for i in range(len(items)*2):
        featuresMatrix.append(0)
    for item in items:
        features[item] = index
        index += 1
        features['_'+item] = index
        index += 1

    for src_item in src_items:
        src_word = src_item.split('/')[0]
        src_tag = src_item.split('/')[1]
        if not (features.__contains__(src_tag)):
            continue
        index = features[src_tag]
        sign = 1
        for susp_item in susp_items:
            susp_word = susp_item.split('/')[0]
            susp_tag = susp_item.split('/')[1]
            if src_item == susp_item:
                featuresMatrix[index] += 1
                sign = 0
        featuresMatrix[index+1] += sign
    return featuresMatrix

def getFeatures(pairslist):
    for pairs in pairslist:
        src = pairs[0]
        susp = pairs[1]




ori_trainPath = '/home/cks/PycharmProjects/ATEC/data/seg.txt'
train_labels, train_pairslist = getTheOriginData(ori_trainPath)

with open('/home/cks/PycharmProjects/ATEC/data/segFeature.txt', 'w') as fs:
    for i in range(len(train_pairslist)):
        pairlist = train_pairslist[i]
        label = train_labels[i]
        src = pairlist[0]
        susp = pairlist[1]
        fs.write(label+'\t'+str(getFeature(src, susp))+'\n')


