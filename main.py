import jieba
import sys
from gensim import corpora, models, similarities
from collections import defaultdict
# 定义文件目录
test1 = sys.argv[1]
test2 = sys.argv[2]
test3 = sys.argv[3]
# 读取文件内容
test_1 = open(test1, encoding='utf-8').read()
test_2 = open(test2, encoding='utf-8').read()
# jieba 进行分词
data1 = jieba.cut(test_1)
data2 = jieba.cut(test_2)
data_1 = ""
# 获取分词内容
for i in data1:
    data_1 += i + " "
data_2 = ""
# 获取分词内容
for i in data2:
    data_2 += i + " "
doc1 = [data_1, data_2]
# print(doc1)
t1 = [[word for word in doc.split()] for doc in doc1]
# corpora语料库建立字典
dictionary = corpora.Dictionary(t1)
data_3 = data_1+data_2
new_doc = data_3
# print(new_doc)
# doc2bow把文件变成一个稀疏向量
new_vec = dictionary.doc2bow(new_doc.split())
# 对字典进行doc2bow处理，得到新语料库
new_corpor = [dictionary.doc2bow(t3) for t3 in t1]
tfidf = models.TfidfModel(new_corpor)
# 特征数
featurenum = len(dictionary.token2id.keys())
# similarities 相似之处
# SparseMatrixSimilarity 稀疏矩阵相似度
idx = similarities.SparseMatrixSimilarity(tfidf[new_corpor], num_features=featurenum)
sims = idx[tfidf[new_vec]]
# sims[0]和sims[1]分别为文1文2与总文本的相似度
# 相除之后得两文本之间相似度
if (sims[1]<sims[0]):
    ans = sims[1]/sims[0]
else:
    ans = sims[0]/sims[1]
print(ans)
with open(test3, "w+", encoding='UTF-8') as fp:
    fp.write(str(ans))