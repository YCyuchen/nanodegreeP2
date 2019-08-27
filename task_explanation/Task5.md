# Task5
Autocomplete with Tries

## Solution
First we declare our TrieNode class attributes including a default dictionary from Python to store our child nodes, an is_word boolean to confirm our node is the last node of that branch, and a word_list list to store our words.
The suffixes() method will take in a prefix parameter and we set current as our self referencing node. Iterating over our current children keys, we check if char in our keys is not present, which we break, add or concat that to our suffix empty string and set current to our new node.

Then calling suffixes_recursive() method will first check to make sure our node is not at the end, to which we append our suffix to our word_list list. Then we iterate over key, and value of our current node's children items and call our suffixes_recursive method passing in our value, and our suffix plus or concatenating our key.

Time complexity is $O(M*N)$, N is the number of strings in Trie and M is the longest string length in Trie.
Space complexity is O(N), N is number of keys in Trie