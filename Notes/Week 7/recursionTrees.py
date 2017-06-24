# recursionTrees.py

'''
recursion and trees

    tress are a natural enviroment for
    using recursion.
    
    idea: iterate over the branches,
    dealing with each branch recursively
'''

numsTree = [1,2,[3,[4,5],6,7],[8,[9]],10]

# depth first traversal of a tree
def traverse( tree, depth=0 ):
    ''' print all items in a nested list '''

    if type(tree)!=list:  # a leaf
        print(depth*' ',tree)
    else: # is a list
        for branch in tree:
            traverse(branch,depth+1)

'''
>>> traverse( numsTree )
  1
  2
   3
    4
    5
   6
   7
   8
    9
  10
'''


def total( tree ):
    ''' return total of all items in
nested list tree '''

    if type(tree)!=list:
        return tree # tree is a number
    else:
        ans = 0
        for branch in tree:
            ans+=total(branch)
        return ans

def flatten( tree ):
    ''' convert a nested list to a non-nested list'''

    if type(tree)!=list:
        return [tree]
    else:
        ans = []
        for branch in tree:
            ans+=flatten(branch)
        return ans
            










            
        
    
