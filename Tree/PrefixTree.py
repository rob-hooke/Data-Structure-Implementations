# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 17:57:49 2019

@author: nemesisBR
"""
#ref =https://www.topcoder.com/community/data-science/data-science-tutorials/using-tries/


class TrieNode:
    
    def __init__(self,x):
        self.word = x
        self.isword = 0
        self.prefixes = 0
        self.ref = [None] * 26
        
        
        
def addWord(root,let):
    if let == '':
        root.isword += 1
        return
    else:
        root.prefixes += 1
        l = let[0]
        
        if root.ref[ord(l) % 97] == None:
            root.ref[ord(l) % 97] =  TrieNode(l)
        
        let = let[1:]
        addWord(root.ref[ord(l) % 97],let)



def check(root,val):
    
    for char in val:
        if root.ref[ord(char) % 97] == None:
            return False
        else:
            root = root.ref[ord(char) % 97]
    
    return True
    
    
def uniquePrefix(root,string):
        count = 0
        for char in string:
            root = root.ref[ord(char) % 97]
            
            if root.prefixes == 1:
                break
            else:
                count += 1
        
        return count + 1
    
    
                
    
if __name__ == '__main__':
    
    parent = TrieNode('')
    arr = ['zebra','dog','duck','dove']
    res = list()
    
    for i in arr:
        addWord(parent,i)
    
    for i in arr:
        ind =  uniquePrefix(parent,i)
        res.append(i[:ind])
        
    print(res)
    
    
    
    
    
        
        
