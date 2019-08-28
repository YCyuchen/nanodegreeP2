# Task5
Autocomplete with Tries

## Solution
First we declare our TrieNode class attributes including a default dictionary from Python to store our child nodes, an is_word boolean to confirm our node is the last node of that branch, and a word_list list to store our words.

`function: suffixes(self, cur=None, suffix='', word_list=None)`
The suffixes() method will takes in current TrieNode, suffix and word_list. We recursively go deeper on the input current TrieNode, if we find it's a word the we call by reference of word_list and append the suffix in it. It's a DFS recursion function.
Time complexity is $O(M*N)$, N is the number of strings in Trie and M is the longest string length in Trie.

Space complexity:
For word_list, Space complexity is O(N), N is number in word list.
For TrieNode, Space complexity is O(N), N is the keys in Trie