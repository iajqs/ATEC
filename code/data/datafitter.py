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
        pairs = []
        strs = line.split('\t')
        labels.append(strs[3])
        pairs.append(strs[1])
        pairs.append(strs[2])
        pairslist.append(pairs)

    return labels, pairslist
import re

def getTaglist(pairslist):
    tagList = []
    regex = "^[[]"

    for pair in pairslist:

        src = pair[0].replace(' ', '').replace('/','')

        susp = pair[1].replace(' ', '').replace('/','')
        src = analyzer.analyze(src)

        susp = analyzer.analyze(susp)
        for word in str(src).strip().split():
            tag = word.split("/")[1]
            if (tag in tagList):
                continue
            else:

                tagList.append(tag)
        for word in str(susp).strip().split():
            tag = word.split("/")[1]
            if (tag in tagList):
                continue
            else:

                tagList.append(tag)
    return tagList

# get the tagList
def word_tagedList(pairslist):
    tagList = []
    regex = r'^[[].+[]$]'

    for pair in pairslist:

        src = pair[0].replace(' ', '').replace('/','')

        susp = pair[1].replace(' ', '').replace('/','')
        src = analyzer.analyze(src)
        susp = analyzer.analyze(susp)
        if re.search(r'^[[].+[\]$]', str(src)):
            newWord = re.match(r'^[[].+[]$]', str(src)).group()
            newWord,number = re.subn(r'[[]|[/]+.+[ $]|[/]+.+[]$]', "", newWord)

            src, number = re.subn(r'^[[].+[\]$]',newWord,str(src))
            print(src)
        if re.search(r'^[[].+[\]$]', str(susp)):
            newWord = re.match(r'^[[].+[]$]', str(susp)).group()
            newWord,number = re.subn(r'[[]|[/]+.+[ $]|[/]+.+[]$]', "", newWord)

            susp, number = re.subn(r'^[[].+[\]$]',newWord,str(susp))
            print(susp)
            print()
    return tagList

# def writeTagedContent(pairslist, path):
#     tagList = []
#     regex = "^[[]"
#         for pair in pairslist:
#             src = pair[0].replace(' ', '').replace('/','')
#             susp = pair[1].replace(' ', '').replace('/','')
#             src = analyzer.analyze(src)
#             susp = analyzer.analyze(susp)



PerceptronLexicalAnalyzer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')
analyzer = PerceptronLexicalAnalyzer()


# print(analyzer.analyze("我的花呗是以前的手机号码，怎么更改成现在的支付宝的号码手机号"))
# str1 = '[双*/j **/j]/nt 零时/t 花呗/n 额度/n'
# print(re.search(r'^[[].+[]$]', str1))
# print(re.match(r'^[[].+[]$]', str1).group())
# str1 = re.subn(r'^[[].+[]$]', "haha", str1)
# print(str1)



##get the data
##get the train data
ori_trainPath = '/home/cks/PycharmProjects/ATEC/data/atec_nlp_sim_train.csv'
train_labels, train_pairslist = getTheOriginData(ori_trainPath)

tagList = word_tagedList(train_pairslist)
print(tagList)

# tagedFile = '/home/cks/PycharmProjects/ATEC/data/tagged.txt'
# writeTagedContent(train_pairslist,tagedFile)
# ['r', 'd', 'v', 'nz', 'u', 'n', 'f', 'w', 't', 'y', 'ad', 'vn', 'm', 'p', 'a', 'j', 'b', 'an', 'q', 'c', 's', 'Ng', 'i', 'nr', 'Tg', 'Vg', 'j', 'l', 'nx', 'z', 'vd', 'n]', 'Ag', 'ns', 'k', 'Mg', 'o', 'Bg', 'nt', 'Dg', 'h', 'e']
