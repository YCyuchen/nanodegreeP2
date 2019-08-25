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

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        current = self
        suffix = ""

        for char in current.children.keys():
            if not current.children[char]:
                break

            suffix += char
            current = current.children[char]

        self.suffixes_recursive(current, suffix)

        for letters in self.word_list:
            print(letters)

    def suffixes_recursive(self, current, suffix):
        if current.is_word:
            self.word_list.append(suffix)

        for k, v in current.children.items():
            self.suffixes_recursive(v, suffix + k)


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
        "anthology", "antagonist", "antonym", "ant", "anno",
        "fun", "function", "factory", "apple", "trie", "trigger", "trigonometry", "tripod"]

    for word in wordList:
        MyTrie.insert(word)

    prefixNode = MyTrie.find("an")
    print((prefixNode.suffixes()))
