## Requirements
Implement an autocomplete feature using a Trie data structure. For example, if our Trie contains the words `["fun", "function", "factory"]` and we query for suffixes from the node representing the letter `f`, we expect to receive `["un", "unction", "actory"]`.

## Approach
The Trie is a tree-like data structure that efficiently stores words and allows for quick prefix matching. The implementation includes methods for inserting words, finding prefixes, checking for word existence, and retrieving all words associated with a given prefix.

### Key Components
1. **TrieNode**:
   - Contains a dictionary of child nodes and a boolean flag to indicate if it marks the end of a word.
   - Provides methods to insert characters and collect suffixes from the node.

2. **Trie**:
   - Contains a root node and methods to insert words, find nodes by prefix, check for word existence, and retrieve all words matching a given prefix.
   - The `insert` method builds the Trie from the root down, creating nodes for each character in the word.
   - The `find` method locates the node corresponding to the end of the prefix.
   - The `prefix_words` method collects all words that start with a given prefix by leveraging the suffixes collected from the Trie nodes.

### Complexity Analysis
**Time Complexity**:
- **Insert**: `O(n)` where `n` is the length of the word being inserted.
- **Find**: `O(s)` where `s` is the length of the prefix being searched.
- **Prefix Words**: `O(t)` where `t` is the total number of nodes in the Trie. In the worst case, if the search string is empty, all nodes might need to be visited to compile the list of words.

**Space Complexity**:
- **Insert**: `O(n)` where `n` is the total number of nodes in the Trie. The space required grows linearly with the number of words, but can decrease due to shared prefixes.
- **Prefix Words**: `O(n)` where `n` is the number of nodes visited during the search.
