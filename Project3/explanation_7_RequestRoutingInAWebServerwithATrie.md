## Requirements
Implement a typical web server routing mechanism using the Trie data structure. The router should be able to:
- Add routes with their associated handlers.
- Lookup routes to find the corresponding handler based on a given path.

## Approach
1. **RouteTrieNode**: 
   - Represents a node in the Trie. It contains:
     - A dictionary of children nodes.
     - A handler for the route (if it exists).

2. **RouteTrie**: 
   - Manages the root node and provides methods to insert new routes and find handlers for given paths.
   - The `insert` method adds a new route by traversing the Trie according to the parts of the path.
   - The `find` method retrieves the handler for a given path, returning `None` if the path does not exist.

3. **Router**: 
   - Uses the `RouteTrie` to manage the routing.
   - The `add_handler` method splits the path into parts and inserts the route with its handler into the Trie.
   - The `lookup` method retrieves the handler for a path or returns a not-found handler if the path doesn't exist.
   - The `split_path` method processes the incoming path to break it into components.
