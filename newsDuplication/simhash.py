# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 10:10:28 2018

@author: AITC
"""

import jieba
import jieba.analyse
import numpy as np
TOPK=30                                  #The topk keywords of content accroding to TF-IDF
#compute the 64-bit hash value of a word
def string_hash(source):
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** 128 - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            x = bin(x).replace('0b', '').zfill(64)[-64:]
            return str(x)
#compute the 64-bit simhash value of a content
def content_simhash(content):
    content_withweight=[]
    keywords=jieba.analyse.extract_tags(content,topK=TOPK,withWeight=True)
    for word,wight in keywords:
        word=string_hash(word)
        wight=TOPK*wight
        temp=[]
        for i in word:
            if i=='1':
                temp.append(wight)
            else:
                temp.append(-wight)
        content_withweight.append(temp)
    content_list=np.sum(np.array(content_withweight),axis=0)
    simhash=''
    for i in content_list:
        if i>0:
            simhash+='1'
        else:
            simhash+='0'
    return simhash
def hamming_distance(cont_simhash1,cont_simhash2):
    st1='0b'+cont_simhash1
    st2='0b'+cont_simhash2
    n=int(st1,2)^int(st2,2)
    i=0
    while n:
        i+=1
        n&=(n-1)
    return i
if __name__=='__main__':
    s='近日，中国能建辽宁康平光伏发电项目一期工程并网发电，至此，现东北地区最大的光伏电站正式投入商业运行。据了解，辽宁康平光伏发电项目由中国能建集团投资公司全资投资建设。项目位于辽宁省沈阳市康平县三台子水库，规划装机总容量为200兆瓦，分两期建设。项目一期建设120兆瓦，投资额约9亿元人民币，年均发电量可达15625万千瓦时。本工程紧跟光伏领跑者技术标准进行规划设计，基本实现了数据采集、传输、存储、查询自动化；状态监测、故障诊断、故障报警、光功率预测智能化，基本达到了少人值守、智能化运维智能化光伏电站标准。该项目的建成将对调整和优化辽宁省能源结构起到巨大的推动作用，具有良好的社会效益和经济效益。'
    t='近日，由福建省计量院国家光伏产业计量测试中心负责起草的福建省地方计量校准规范《太阳电池量子效率测试仪校准规范》通过了专家组审定。据介绍，太阳电池量子效率测试仪被广泛应用于太阳电池生产企业、研发和测试机构，是太阳电池研发和太阳电池标准片定标过程中重要的测量设备，为太阳能电池效率提升研究、电池失效分析以及标准太阳电池片量值传递提供重要的测量数据，对太阳电池的准确定标和贸易结算具有重要影响。该校准规范的制定为国内首次，填补了国内该类设备校准方法的空白。规范中制定的校准项目和方法覆盖了太阳电池量子效率测试仪的主要特征参数。同时，该校准规范的制定为光伏电池量子效率测试系统测量结果的准确可靠提供技术保障，为新型太阳电池的研制提供技术支持，具有较大的社会和经济效益。'
    con1=content_simhash(s)
    con2=content_simhash(t)
    print(hamming_distance(con1,con2))