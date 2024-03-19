# tree.py

class Node:
    def __init__(self, tag_name, node_id, text_content, children=None):
        self.tag_name = tag_name
        self.id = node_id  # Add id attribute
        self.text_content = text_content
        self.children = children or []

class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, target_id):
        if self.root is None:
            return None
        
        # Depth-first traversal
        # return self._dfs(self.root, target_id)
        
        # Breadth-first traversal
        return self._bfs(target_id)
    
    def _dfs(self, node, target_id):
        if node.id == target_id:
            return node
        
        for child in node.children:
            result = self._dfs(child, target_id)
            if result:
                return result
        
        return None
    
    def _bfs(self, target_id):
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            if node.id == target_id:
                return node
            
            queue.extend(node.children)
        
        return None
