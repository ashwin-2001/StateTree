class Node:
    def __init__(self,data):
        self.data=data
        self.children = []
    def add_child(self,data):
        self.children.append(Node(data))

        return self.children
    def printtree(self):
        print(self.children)
    def __repr__(self):
      return f"{len(self.children)}"
    
        
   
class MAGT:
    def __init__(self,N):
        self.states=None
        self.Node=Node(N)
        self.child=self.Node
        self.childlist=[]
    def states_to_tree(self,states):
        for j in range(0,len(states)):
            if j<len(states)-1:
                self.add_node(states[j],states[j+1])
        self.childlist=[]
        self.child =self.Node
        return self.childlist
    def add_node(self,st,s2):
        #print("_+_+__+__+_+_+")
        #print("Child :",self.child.data,len(self.child.children))
        if len(self.child.children)==0:
            self.child.add_child(s2)
            for ele in self.child.children:
              if ele==s2:self.child=ele
        else:
            resp=[e.data for e in self.child.children]
            for item in self.child.children :
                    if item.data == st  and st!=s2:
                        self.child = item  #if node in children[] ,set child as node
                        if st!=s2:
                          self.add_node(s2, s2)
                          break

                    elif st not in resp and st!=s2:
                        self.child.add_child(st)
                        for a in self.child.children:
                             if a.data==st:
                               self.child = a
                               break
                          
                    
                        
 
                       # self.child = item
 
        return self.Node

tree=MAGT(0)
lst=[0,2,3,4,5]
lst2=[2,3,8,5,4]
lst3=[2,3,8,5,4]
tree.states_to_tree(lst)
tree.states_to_tree(lst2)
tree.states_to_tree(lst3)
tree.Node.printtree()
print(len(tree.Node.children))
for i in tree.Node.children:
  for p in i.children:
    #print(p)
    pass
