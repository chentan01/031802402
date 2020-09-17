# 031802402


题目：论文查重

描述如下：

设计一个论文查重算法，给出一个原文文件和一个在这份原文上经过了增删改的抄袭版论文的文件，在答案文件中输出其重复率。

原文示例：今天是星期天，天气晴，今天晚上我要去看电影。
抄袭版示例：今天是周天，天气晴朗，我晚上要去看电影。

要求输入输出采用文件输入输出，规范如下：

从命令行参数给出：论文原文的文件的绝对路径。
从命令行参数给出：抄袭版论文的文件的绝对路径。
从命令行参数给出：输出的答案文件的绝对路径。

我们提供一份样例，可以在群文件里下载，使用方法是：orig.txt是原文，其他orig_add.txt等均为抄袭版论文。

注意：答案文件中输出的答案为浮点型，精确到小数点后两位

主要算法：
      首先当然是利用jieba进行分词，关键词提取！*✧⁺˚⁺ପ(๑･ω･)੭ु⁾⁾ 
      接着就是利用gensim下面的corpora，similarities进行语料库建立，模型TF-IDF算法，稀疏矩阵相似度分析

主要代码：
  1、读取文件并分词
```python
test_1 = open(test1, encoding='utf-8').read()
test_2 = open(test2, encoding='utf-8').read()
data1 = jieba.cut(test_1)
data2 = jieba.cut(test_2)
```
  2、合并分词
```python
doc1 = [data_1, data_2]
t1 = [[word for word in doc.split()] for doc in doc1]
```
  3、建立词典语料库
```python
t1 = [[word for word in doc.split()] for doc in doc1]
# corpora语料库建立字典
dictionary = corpora.Dictionary(t1)
```
```python
# 通过doc2bow把文件变成一个稀疏向量
new_vec = dictionary.doc2bow(new_doc.split())
# 对字典进行doc2bow处理，得到新语料库
new_corpor = [dictionary.doc2bow(t3) for t3 in t1]
tfidf = models.TfidfModel(new_corpor)
```
  4、利用模型tfidf算法、稀疏矩阵相似度分析
```python
index = similarities.SparseMatrixSimilarity(tfidf[new_corpor], num_features=featurenum)
sims = index[tfidf[new_vec]]
# sims[0]和sims[1]分别为文1文2与总文本的相似度
# 相除之后得两文本之间相似度
if (sims[1]<sims[0]):
    ans = sims[1]/sims[0]
else:
    ans = sims[0]/sims[1]
```
主要的话：
  虽然代码还没优化完，但俺还在学习，争取做到更好٩(*Ӧ)و
