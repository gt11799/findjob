#! /usr/bin/env python

'''
To organize father topic and subtopic with Tree
via: zhihu
'''

class TreeNode:
    
    def __init__(self, value):
        self.children = []
        self.value = value
        
    def add_child(self, *child):
        self.children += child
        
    def show(self, layer):
        print "  " * layer + self.value
        map(lambda child: child.show(layer+1), self.children)
        
def test_TreeNode():
    a1 = TreeNode("a-1")
    b1 = TreeNode("b-1")
    b2 = TreeNode("b-2")
    c1 = TreeNode("c-1")
    d2 = TreeNode("d-1")
    i8 = TreeNode("i-8")
    
    a1.add_child(b1, b2)
    i8.add_child(TreeNode("r-8"))
    b2.add_child(c1, TreeNode("c-2"))
    c1.add_child(TreeNode("c-3"), TreeNode("c-4"), TreeNode("c-5"))
    a1.add_child(TreeNode("y-6"))
    b1.add_child(i8)
    
    a1.show(0)
    
class TreePoc(object):
    '''
    basic tree class from coursera (Principle of Computer)
    '''
    def __init__(self, value, children):
        
        self._value = value
        self._children = children
        
    def __str__(self):
        ans = "["
        ans += str(self._value)
        
        for child in self._children:
            ans += ", "
            ans += str(child)
        return ans + "]"
        
    def all_nodes(self):
        '''
        return all nodes in tree
        '''
        ans = set([])
        ans.add(self._value)
        for child in self._children:
            ans.update(child.all_nodes())
        return ans
        
    def add_node(self, father_node, sub_node):
        '''
        given father_node and sub_node, add it in tree
        if father_node in the tree, then add the sub_node
        if father_node not in the tree, then 
        '''
        if father_node in self.all_nodes():
            sub_tree = TreePoc(sub_node, [])
        
    def get_value(self):
        '''
        Getter for node's value
        '''
        return self._value
        
    def children(self):
        '''
        Generator for return children
        '''
        for child in self._children:
            yield child
            
    def num_nodes(self):
        '''
        compute number of nodes in the tree
        '''
        ans = 1
        for child in self._children:
            ans += child.num_nodes()
        return ans
        
    def num_leaves(self):
        '''
        Count number of leaves in tree
        '''
        if len(self._children) == 0:
            return 1
            
        ans = 0
        for child in self._children:
            ans += child.num_leaves()
        return ans
        
    def height(self):
        '''
        Compute height of a tree rooted by self
        '''
        height = 0
        for child in self._children:
            height = max(height, child.height()+1)
        return height
        
def test_TreePoc():
    tree_a = TreePoc("a", [])
    tree_b = TreePoc("b", [])
    tree_c = TreePoc("c", [tree_a, tree_b])
    tree_d = TreePoc("d", [tree_c])
    tree_a = TreePoc("a", [TreePoc("po",[])])
    print("test TreePoc:\ntree: %s\nheight: %s\nall nodes: %s" \
        %(tree_d, tree_d.height(), tree_d.all_nodes()))
        
if __name__ == '__main__':
    #test_TreeNode()
    test_TreePoc()