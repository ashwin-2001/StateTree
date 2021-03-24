# Tic-Tae-Toe 3x3 Matrix

import numpy as np
import random
import matplotlib.pyplot as plt


class player:
  def __init__(self,setup=None,sym=None):
    self.setup = setup
    self.sym=sym
    self.boardHash=0

  def place(self,x,y):
    if self.setup[x][y]==0:self.setup[x][y]=self.sym
    return self.setup

class Board:
  def __init__(self,sym1=1,sym2=3):
    setup = np.zeros((3,3))
    self.board=setup
    self.sym1=sym1
    self.sym2=sym2
    self.reward=0
    self.game_states=[]
    self.drive=0

  def possibilities(self): 
    board=self.board
    l = [] 
      
    for i in range(len(board)): 
        for j in range(len(board)): 
              
            if board[i][j] == 0: 
                l.append((i, j)) 
    return(l) 

  def check(self,sym=0):
    zero=[]
    for u in range(0,3):
      column=[]
      for p in range(0,3):
        jk = int(self.board[p][u])
        if jk==sym:column.append(sym)
        if jk==0:zero.append(0)
        if len(column)==3:return zero,True

    for p in range(0,3):
      row=[]
      for u in range(0,3):
        jk = int(self.board[p][u])
        if jk==sym:row.append(sym)
        if jk==0:zero.append(0)
        if len(row)==3:
          return zero,True

    diag_sum1 = [self.board[i][i] for i in range(3)]
    diag_sum2 = [self.board[i][ 3 - i - 1] for i in range(3)]

    diag_sum1=sum([y for y in diag_sum1 if y==sym])
    diag_sum1=sum([y for y in diag_sum2 if y==sym])
    if diag_sum1 == 3*sym or diag_sum2 == 3*sym:
      return zero,True
    
    return zero,False
  
  def Outcome(self,r,c,lolo):
     if lolo==1:
       self.drive=random.randint(1,2)
     if self.drive==1:
       p1 = player(self.board,self.sym1)
       try:
          pup=random.choice(self.possibilities())
          self.board=p1.place(pup[0],pup[1])
       except:pass
       lep=self.board.reshape(9)
       lep=lep.tolist()
       self.game_states.append(lep)

       p2 = player(self.board,self.sym2)
       try:
         pp=random.choice(self.possibilities())
         self.board=p2.place(pp[0],pp[1])
       except:pass
       lep=self.board.reshape(9)
       lep=lep.tolist()
       self.game_states.append(lep)
     
     else:
       p2 = player(self.board,self.sym2)
       try:
         pp=random.choice(self.possibilities())
         self.board=p2.place(pp[0],pp[1])
       except:pass
       lep=self.board.reshape(9)
       lep=lep.tolist()
       self.game_states.append(lep)

       p1 = player(self.board,self.sym1)
       try:
          pup=random.choice(self.possibilities())
          self.board=p1.place(pup[0],pup[1])
       except:pass
       lep=self.board.reshape(9)
       lep=lep.tolist()
       self.game_states.append(lep)


     zero,o1 = self.check(self.sym1)
     zero2,o2 = self.check(self.sym2)
     
     if o2:reward=-200
     elif o1:reward=400
     else: reward=-3
     self.reward=reward
     
     if o1 or o2:
       #print(self.board)
       #print(f"Player 1 : {o1} ----Player 2 : {o2}")
       return True
     elif len(zero)==0 or len(zero2)==0:
       #print("draw")
       ;return True
  def reset_list(self,lol):
    if lol==1:self.game_states=[0]
    else:self.game_states=[]
  def reward_func(self):
    return self.reward
  
  def getlist(self):
        return self.game_states

  def display(self):
    print(self.board)

import pickle

tree = MAGT([0,0,0,0,0,0,0,0,0])
lol=0
for a in range(2000):
  tp = Board()
  steps=0
  lol+=1
  lolo=0
  tp.reset_list(lol)
  while True:
   lolo+=1
   steps+=1
   action=random.randint(0,8)
   def rnc(post=action):
            if post==0:row=0;col=0
            if post==1:row=0;col=1
            if post==2:row=0;col=2
            if post==3:row=1;col=0
            if post==4:row=1;col=1
            if post==5:row=1;col=2
            if post==6:row=2;col=0
            if post==7:row=2;col=1
            if post==8:row=2;col=2
            return row,col
   r,c= rnc()
   process=tp.Outcome(r,c,lolo)
   if process :# print(steps)
      break
   
  states= tp.getlist()
  #print(states)
  if states is not None:tree.states_to_tree(states)

print(len(tree.Node.children))
#print(tree.Node.children)
#tree.Node.printtree()

for i in tree.Node.children:
   print(i.data)
   e=[]
   c=0
   for u in i.children:
     c+=1
     e.append(u)
print(c)
for k,el in enumerate(e):
  print(el.data,k)
print("-=-=---=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-\n\n")
