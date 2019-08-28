# Task7
HTTPRouter using a Trie

## Solution
First we declare the RouteTrieNode class attributes including a default dictionary from Python to store our child nodes and a handler to store our URL handle.

Our RouteTrie class will also have a handler denoted by the "/" root slash as in a root directory and a self root referencing a RouteTrieNode class storing our root handler. The insert() takes in parts of the URL path and our handler name. We iterate over the parts and with an if conditional, ask if our current node's children already has this "part" in their node key. If not, we will set that child's key to a new node else, we will declare current as our newly created node with item as its key and finally call current node's handler attribute with the handler parameter.

The RouteTrie class will also have a find() method that will iterate over the URL path parts and return the node's handler.  Similarly, we check if that part is in the current node's children. If so, we set current to that node's key else return None. Finally return the current node's handler.

Time complexity:
For Insert() and Find(), Time complexity is O(M), M is the longest string length

Space complexity:
For insert(), we will create a new nodes in the trie based on the input string elements.

For find(), we will judge if the value of split path is in RouteTrieNode's children. current.children will have O(M*N) complexity,  M is the longest string length, N is the number of string in Trie.

Time complexity is $O(M*N)$, N is the number of strings in Trie and M is the longest string length in Trie.
Space complexity is O(K*N), K is the key length, N is number of keys in Trie
