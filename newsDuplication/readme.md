利用Simhash对相似新闻文本进行去重
===
Simhash对于去重效果比较好，也就是两篇新闻文本有着大量的重复内容，比如说转载等方式，但对于语义相似的两篇文本效果不是很好。在文章长度比较长时效果要好，对于短文本不太适用。<br>
Simhash算法分为以下五个步骤：（1）对文本进行分词，得到文档的TF-IDF（2）对每个词频hash，得到每个词的hash值（3）根据每个词的权重进行hash加权（4）把文章的每个词频的加权的hash值进行相加合并（5）降维，根据相加的结果将一篇文档转化为64位二进制数来表示<br>