#!/usr/bin/env python
# encoding: utf-8

import sys
import numpy as np
from scipy import spatial
from sklearn import preprocessing

#####
cn_we = {}
lines = open('/home/asd/cdminer/naacl/corpus_data/w2v/englishembedding_0207.txt').read().split('\n')
cnt = 0
for line in lines[:]:
    ls = line.split()
    if(len(ls)==151):
        vec = [ float(ls[x]) for x in range(1,151) ]
        cn_we[ls[0]] = vec
        cnt +=1
        if(cnt%1000==0):
            print(cnt,'/',len(lines)-1)
print("Done Loading Chinese Embeddings")

en_we = {}
lines = open('/home/asd/cdminer/naacl/corpus_data/w2v/chineseembedding_0207.txt').read().split('\n')
cnt = 0
for line in lines[:]:
    ls = line.split()
    if(len(ls)==151):
        vec = [ float(ls[x]) for x in range(1,151) ]
        en_we[ls[0]] = vec
        cnt +=1
        if(cnt%1000==0):
            print(cnt,'/',len(lines)-1)
print("Done Loading English Embeddings")

import json
trans = json.load(open('/home/asdf/slang/trans_en.json'))
cn_set = dict()
for e in trans:
    for c in trans[e]:
        c = c.encode('utf8')
        if(c not in cn_set):
            cn_set[c] = []
        cn_set[c].append(e)

trans = cn_set


def ScoreEn(en,title):
    res = []
    for dim in trans[en]:
        if(dim not in cn_we):
            continue
        res.append(1-spatial.distance.cosine(cn_we[title],cn_we[dim]))
    if(len(res)==0):
        return 0
    return sum(res)/len(res)
def GetMostSimilar(cn):
    allres = []
    if cn not in cn_we:
        return allres
    en_ranks = []
    for en in trans.keys():
        en_ranks.append((en,ScoreEn(en,cn)))
    en_ranks.sort(key = lambda x:x[1],reverse=True)
    final_res = [x[0] for x in en_ranks]

    return final_res[:5]
import os

from scipy import spatial
import numpy as np

en_emd = dict()
def loadEMD():
    # lines = open('/home/asdfg/2.14/Validgoogleword2vec.txt').read().split('\n')
    lines = open('/home/asd/cdminer/naacl/corpus_data/w2v/chineseembedding_0207.txt').read().split('\n')
    cnt = 1
    print('loading')
    for line in lines:
        ls = line.split()
        if len(ls)==151:
            en_emd[ls[0]] = np.array([float(k) for k in ls[1:151]])
            cnt += 1
            if cnt%10000==0:
                print(str(cnt)+'/'+str(len(lines)))
loadEMD()

def calcAvgSim(a_list,b_list):
    sim = 0.0
    sim_cnt = 0
    for a  in a_list:
        for b in b_list:
            a = a.lower()
            b = b.lower()
            if a not in en_emd:
                sim_cnt +=1
                continue
            if b not in en_emd:
                continue
            sim += 1 - spatial.distance.cosine(en_emd[a],en_emd[b])
            sim_cnt += 1

    if(sim_cnt==0):
        return 0.0
    return sim/sim_cnt

cnt = 1
google_res = 0.0
bing_res = 0.0
baidu_res = 0.0
cc_res = 0.0
soc_res = 0.0

for line in open('EN_OOV.tsv','r').read().split('\n'):
    ls = line.split('\t')

    if(len(ls)>=3):
        title = ls[0]
        if(title not in cn_we):
            continue
        print title
        # google = ls[1]
        # bing = ls[2]
        # baidu = ls[3]
        # cc = ls[4]
        truth = ls[2]
        soc_list = GetMostSimilar(title)
        print ' '.join(soc_list)
        # google_res += calcAvgSim(google.strip().split(),truth.strip().split())
        # bing_res += calcAvgSim(bing.strip().split(),truth.strip().split())
        # baidu_res += calcAvgSim(baidu.strip().split(),truth.strip().split())
        # cc_res +=  calcAvgSim(cc.strip().split(),truth.strip().split())
        soc_res += calcAvgSim(soc_list ,truth.strip().split())
        cnt += 1

print(google_res , bing_res , baidu_res , cc_res , soc_res)