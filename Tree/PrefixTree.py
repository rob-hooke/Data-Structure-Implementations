# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 17:57:49 2019

@author: nemesisBR
"""
#ref =https://www.topcoder.com/community/data-science/data-science-tutorials/using-tries/


class TrieNode:
    
    def __init__(self,x):
        self.word = x
        self.prefixes = 0
        self.ref = [None] * 26
        
        
        
def addWord(root,let):
    if let == '':
        return
        #root.word += 1
    else:
        root.prefixes += 1
        l = let[0]
        
        if root.ref[ord(l) % 19] == None:
            root.ref[ord(l) % 19] =  TrieNode(l)
        
        let = let[1:]
        addWord(root.ref[ord(l) % 19],let)



def check(root,val):
    
    for char in val:
        if root.ref[ord(char) % 19] == None:
            return False
        else:
            root = root.ref[ord(char) % 19]
    
    return True
    
    
if __name__ == '__main__':
    
    parent = TrieNode('')
    
    inp = 'bob'
    
    addWord(parent,inp)
    
    print(check(parent,'boby'))
    
    
    
    
    
        
        
