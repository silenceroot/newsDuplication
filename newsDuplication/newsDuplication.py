# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 09:22:38 2018

@author: AITC
"""
import time
start=time.time()                 #compute run time
import simhash
import json
data_dict={}                       #{ID1:{simhashcode:64-bit,groupID:group-id}}
with open('map_polylinePa020170101-00.json','r',encoding='UTF-8') as f:
    data=json.load(f)
    for i in data:
        hashcode=simhash.content_simhash(i['content'])
        newsid=i['newsID']
        data_dict[newsid]={'simhashcode':hashcode,'groupID':newsid}
hashcode_dict={}                  #{16-bit:[ID1,...IDn]}
for i in data_dict:
    A=data_dict[i]['simhashcode'][0:16]
    B=data_dict[i]['simhashcode'][16:32]
    C=data_dict[i]['simhashcode'][32:48]
    D=data_dict[i]['simhashcode'][48:64]
    for j in (A,B,C,D):
        if j in hashcode_dict:
            hashcode_dict[j].add(i)
        else:
            hashcode_dict[j]={i}
for i in data_dict:
    A=data_dict[i]['simhashcode'][0:16]
    B=data_dict[i]['simhashcode'][16:32]
    C=data_dict[i]['simhashcode'][32:48]
    D=data_dict[i]['simhashcode'][48:64]
    for j in (A,B,C,D):
        for k in hashcode_dict[j]:
            if simhash.hamming_distance(data_dict[i]['simhashcode'],data_dict[k]['simhashcode'])<=3:
                data_dict[i]['groupID']=min(i,k)
Sorted_data=sorted(data_dict.items(),key=lambda x:x[1]['groupID'])
#print(Sorted_data)
#print(len(Sorted_data))
end=time.time()
print(end-start)