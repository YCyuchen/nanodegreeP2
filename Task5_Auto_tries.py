#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/8/25 3:14 PM 
# @Author : Yuchen 
# @File : Task5_Auto_tries.py 
# @Software: PyCharm
from collections import defaultdict


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = defaultdict(TrieNode)
        self.word_list = list()

    def insert(self, char):
        # Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix='', cur=None, word_list=None):
        # Recursive function that collects the suffix for
        # all complete words below this point

        if word_list == None:
            word_list = self.word_list
            cur = self

        if cur.is_word == True:
            word_list.append(suffix)

        for char in cur.children.keys():
            self.suffixes(suffix + char, cur.children[char], word_list)

        return word_list


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie

        current_node = self.root

        for char in word:
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            # print('char in prefix: ',char)
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]

        return current_node


if __name__ == '__main__':
    MyTrie = Trie()
    wordList = [
        "anthology", "antagonist", "antonym", "ant",
        "fun", "function", "factory", "apple", "trie", "trigger", "trigonometry", "tripod"]

    for word in wordList:
        MyTrie.insert(word)


    def f(prefix):
        if prefix != '':
            prefixNode = MyTrie.find(prefix)
            # print('prefixNode: ', prefixNode)
            if prefixNode:
                print(prefixNode.suffixes())
            else:
                print(prefix + " not found")
        else:
            print(str(MyTrie))
            print('')


    # Test1 edge test, prefix not exit
    f("1")
    print("---------------")
    # Test2
    f("a")
    print("---------------")
    # Test3 edge test, prefix not exit
    f("ann")
