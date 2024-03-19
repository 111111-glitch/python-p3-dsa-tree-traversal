# get_element_by_id_test.py

from tree import Node, Tree

def test_get_element_by_id():
    # Create a sample tree structure
    node1 = Node(tag_name='h1', node_id='heading1', text_content='Title 1')
    node2 = Node(tag_name='h2', node_id='heading2', text_content='Title 2')
    node3 = Node(tag_name='h3', node_id='heading3', text_content='Title 3')

    node1.children = [node2]
    node2.children = [node3]

    # Create a Tree instance with the root node
    tree = Tree(root=node1)

    # Test the get_element_by_id method
    result = tree.get_element_by_id('heading2')
    assert result.text_content == 'Title 2'
