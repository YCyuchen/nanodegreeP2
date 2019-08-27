# Task7
HTTPRouter using a Trie

## Solution
First we declare the RouteTrieNode class attributes including a default dictionary from Python to store our child nodes and a handler to store our URL handle.

Our RouteTrie class will also have a handler denoted by the "/" root slash as in a root directory and a self root referencing a RouteTrieNode class storing our root handler. The insert() takes in parts of the URL path and our handler name. We iterate over the parts and with an if conditional, ask if our current node's children already has this "part" in their node key. If not, we will set that child's key to a new node else, we will declare current as our newly created node with item as its key and finally call current node's handler attribute with the handler parameter.

The RouteTrie class will also have a find() method that will iterate over the URL path parts and return the node's handler.  Similarly, we check if that part is in the current node's children. If so, we set current to that node's key else return None. Finally return the current node's handler.

Time complexity is $O(M*N)$, N is the number of strings in Trie and M is the longest string length in Trie.
Space complexity is O(N), N is number of keys in Trie
