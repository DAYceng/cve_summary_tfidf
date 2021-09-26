from sklearn.feature_extraction.text import TfidfVectorizer
from utils.segWord import SegWord

def tfidf_feature(train_doc,test_doc):
    tfidf_list = []
    tv = TfidfVectorizer(use_idf=True, smooth_idf=True, stop_words='english',norm='l2') # 实例化tf实例
    tv_fit = tv.fit_transform(train_doc) # 训练，构建词汇表以及词项idf值，并将输入文本列表转成VSM矩阵形式
    sparse_result = tv.transform(train_doc) # 输出TFIDF矩阵中有计算值的项并标明位置和具体的数值
    vocab_name = tv.get_feature_names() # 查看一下构建的词汇表
    vocab_VSMarray = tv_fit.toarray() # 查看输入文本列表的VSM矩阵

    sg = SegWord(load_inner=False)
    test_sg = sg.tokenize_no_space(test_doc[0].lower())

    test_fit = tv.transform(test_doc)
    testvocab_name = tv.get_feature_names()
    testvocab_VSMarray = test_fit.toarray()
    vocabdict = dict(zip(testvocab_name, testvocab_VSMarray[0]))
    # 去除字典中值为0的元素
    for v in list(vocabdict.keys()):   #对字典a中的keys，相当于形成列表list
        if vocabdict[v] == 0:
            del vocabdict[v]

    for word in test_sg:
        for k in list(vocabdict.keys()):
            if k == word:
                tfidf_list.append(vocabdict[k])
                flag = 1
                break
            else:
                flag = 0
    if flag == 0:
        tfidf_list.append(0) #若为停用词，直接将其tfidf值设为0
    return tfidf_list,test_sg