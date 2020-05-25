# -*- coding: utf-8 -*-
"""ParisRERFilter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xiOTuDoh53n0M_L9PtuahxU6NnL4lZd6
"""

#####Creating Adjacency matrix


#Un tableau d'équivalence nr - nom de station peut être pratique niveau interface

import copy
###INPUT DU METRO DE PARIS
#Lignes de 1 à 14 en incluant 3bis et 7bisS  
Input  = [             
          [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
          [25,26,6,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,20],
          [48,49,50,51,52,53,54,30,55,56,57,58,59,60,61,62,63,64,65,66,67,44,68,69,70],
          [71,72,73,68],
          [74,75,76,77,36,78,79,80,81,62,82,83,14,84,85,86,87,88,89,90,91,92,93,94,95,96,97],
          [98,99,100,101,102,103,104,39,38,78,79,105,65,106,107,108,17,109,110,111,112,113],
          [6,114,115,116,117,118,119,120,121,122,123,90,124,92,93,125,126,127,113,128,129,130,131,132,133,134,135,20],
          [136,137,138,139,140,141,142,38,143,144,79,145,146,147,148,58,149,12,150,14,151,152,153,154,155,156,113,157,158,159,160,161,162,163],
          [143,39,164,165,166,167,168,169],
          [170,171,172,173,174,120,175,176,177,10,178,58,179,180,181,81,65,182,183,184,17,185,186,19,187,133,188,189,190,191,192,193,194,195,196,197,198,199],
          [200,201,202,203,204,205,206,207,208,209,210,116,211,212,8,213,214,215,57,148,179,216,217,81,65,106,218,219,220,221,20,222,223,224,225,226,227],
          [228,229,203,230,231,232,233,234,120,235,236,237,238,239,86,240,241,242,153,110],
          [14,15,243,63,65,244,41,245,246,167,247,71,248],
          [249,250,251,76,252,253,254,34,255,256,257,56,178,10,258,259,260,238,261,262,90,263,123,264,265,266,267,268,269],
          [270,271,272,273,274,275,276,277,278,32,279,56,214,9,177,280,281,236,90,282,283,284,285,286,287,288],
          [56,178,149,14,18,131,289,290,291],

          #RER:
          [292,0,293,294,295,296,297,6,298,299,58,300,14,301,18,20,302],
          [78,303,304,14,305,306,307,308,309,93,310]
          ]
#Frequentation des 292 arrets de Paris
Freq = [50,10,7,6,8,3,17,6,11,4,6,3,10,3,46,11,6,13,75,6,13,7,6,3,6,3,4,4,3,2,6,3,9,4,6,6,9,7,7,6,5,12,3,4,5,2,4,2,5,4,
        4,3,5,3,3,2,47,8,17,2,4,4,6,4,1,18,3,3,7,4,6,4,1,1,8,3,5,7,88,21,4,9,3,18,2,7,6,4,2,3,31,2,2,9,2,5,7,7,8,3,
        4,5,5,4,5,3,5,2,2,1,10,2,1,12,1,2,9,4,9,4,8,3,2,5,2,2,5,3,3,3,3,7,3,5,2,1,6,4,8,4,3,6,2,2,2,4,3,3,7,5,
        2,2,2,5,3,4,4,3,2,3,8,5,4,11,1,1,1,3,1,1,6,2,3,2,3,5,2,6,7,5,7,5,2,2,2,4,3,2,2,3,2,3,3,4,2,2,2,4,5,3,
        5,3,6,5,2,2,2,2,2,4,3,3,4,3,6,4,7,5,3,5,4,3,2,3,5,5,5,8,4,3,2,2,3,5,2,2,4,1,5,2,2,2,2,4,3,3,3,2,5,3,
        3,4,5,3,2,1,3,2,1,2,2,1,2,1,2,4,6,6,4,4,9,7,10,10,9,4,7,5,3,2,1,2,3,3,5,5,4,2,8,6,19,7,
        #RER:
        45,0,0,0,0,0,0,0,0,0,80,0,0,0,7,6,3,0,45]    

Coord=[
       89.2,23.9, 88.6,24.8, 88.5,25.8, 88.1,27.2, 87.7,28.4, 87.6,28.9, 87.3,29.5, 87.2,30, 87,31, 86.8,31.3, 86.7,32.1, 86.5,32.9, 86.3,33.6, 86.1,34.1, 85.7,34.8, 85.7,35, 85.5,36.2, 85.3,36.9, 84.4,37.3, 84.7,38.7, 84.8,39.6, 84.7,41, 84.6,41.9, 84.5,42.8, 84.4,44,    #Line 1: 0-24
       87.1,27.4, 87.2,28.4, 87.8,29.7, 87.9,30.3, 88.0,30.9, 88.0,31.5, 88.1,32.1, 88.3,32.7, 88.3,33.3, 88.3,33.7, 88.3,34.4, 88.4,34.9, 88.4,35.9, 88.4,36.7, 88.3,37, 87.8,37, 87.2,37.7, 86.9,38.1, 86.6,38.4, 86.3,38.7, 85.8,39, 85.6,39.4,  85.1,39.8,            #Line 2: 25-47     
       89.7,28.1, 89.2,28.5, 88.9,28.9, 88.6,29.2, 88.5,29.7, 88.4,30.6, 88.3,31.1, 87.9,32.3, 87.6,32.6, 87.3,32.8, 87.1,33.2, 87,33.6, 86.9,34.1, 86.7,34.8, 86.6,35.2, 86.6,35.6, 86.7,36.2, 86.7,36.4, 86.5,37.5, 86.4,38.1, 86.5,39.8, 86.4,40.9, 86.5,41.7, 87.7,40.6, 87.2,40.4, 86.8,40.1,    #Line3/3bis: 48-73
       89.8,34.4, 89.4,34.7, 89.1,34.9, 88.7,34.9, 88,35.5, 87.7,35.8, 87.2,35.6, 87,35.5, 86.4,34.9, 86.2,34.6, 85.6,34.6, 85.4,34.4, 85.2,33.9, 85.3,33.3, 85.1,33.1, 84.7,32.7, 84.4,32.4, 84.2,32.9, 83.9,33, 83.4,33.2, 83.2,33, 82.8,32.7, 82.3,32.5, 81.6,32,           #Ligne 4 : 74-97
       90.7,44.9, 89.6,42.5,  89.4,41.3, 89.1,40.3, 88.9,39.2, 88.7,38.7, 88.5,37.9, 87.1,36.1, 86.5,36.8, 86,37.2, 85.7,37.1, 84.6,36.7, 84.3,36.4, 83.9,36.1, 83.6,35.9, 83.1,35.5,                    #Ligne 5: 98-113
       87.1,29.3, 86.7,29, 86.3,28.7, 85.8,28.6, 85.4,28.9, 85,29.4, 84.9,29.8, 84.8,30.2, 84.5,31.1, 84.2,31.3, 84.1,32.6, 83.2,33.7, 83.1,34.3, 83,35.1, 83.3,36.2, 83.5,36.8, 83.8,37.4, 84,37.9, 83.9,38.9, 83.9,39.6, 84.1,40.1, 84.5,40.2,         #Ligne 6 : 114-135
       92.1,41, 91.4,40.4, 90.4,39.2, 89.8,38.6, 89.5,38.2, 89,37.7, 88.8,37.4, 88.1,36.5, 87.8,36.2, 87.7,34.9, 87.6,34.3, 87.5,34, 87.3,33.3, 86.6,33.4, 85.9,34.2, 85.3,35.7, 85.1, 36.1, 84.6,35.5, 84.3,35.2, 84.1,35.2, 83.6,35.2, 82.6,35.7, 82.3,35.8, 81.7,36, 81.1,36.2, 80.5,36.4, 79.9,36.6, 79.5,36.8, 88.1,37.4, 87.8,38.1, 88,38.9, 87.7,39.3, 88,39.9, 88.2,39.3,      #Ligne7/7bis: 136-169
       83.7,27.9, 83.9,28.2, 84.1,28.8, 84.3,29.2, 84.5,29.4, 85.4,30.5, 85.7,31, 86.1,31.5, 87,32.5, 87.2,34, 87.2,34.3, 87.1,34.8, 86.3,36.7, 86.1,36.1, 85.8,36.8, 85.1,37.6, 85,38.4, 84.4,39, 83.7,40.3, 83.5,40.6, 83.3,40, 82.8,40.5, 82.5,41, 82.1,41.6, 81.6,42.8, 81.2,43.6, 80.9,43.8, 80.5,43.8, 80,44.2, 79.5,44.4,          #Ligne 8 : 170-199
       83,23.1, 83.2,23.8, 83.4,24.3, 83.8,25.6, 84.3,26, 84.5,26.2, 84.8,26.4, 85.2,26.8, 85.6,27, 85.8,27.4, 86.4,27.8, 86.4,29.4, 86.4,30.1, 87.2,31.1, 87.4,31.6, 87.4,32.1, 87.2,34.3, 87,34.9, 86.2,37.3, 85.8,38, 85.5,38.5, 85.2,38.9, 85.2,40.1, 85.3,40.6, 85.3,41, 85.6,42.4, 85.8,43.6, 86.2,44.2,                       #Ligne 9 200-227
       84.1,22.8, 84.2,23.9, 84.5,26.7, 84.7,27.3, 84.6,27.8, 84.6,28.6, 84.7,29.5, 84.7,30.7, 84.7,31.7, 84.9,32.1, 85.1,32.6, 85.3,33.5, 85.1,34.5, 85,34.9, 84.7,35.1,              #Ligne 10: 228-242
       86.1,35.3, 87,37.1, 87.4,38.5, 87.5,38.9, 87.6,39.9, 88,41.6, 90.7,36.5, 89.8,35.9, 89,36, 89.2,34.4, 89,33.9, 88.4,33.8, 87.9,33.8, 87.6,33.8, 87.6,33.2, 86.1,32, 85.9,32.3, 85.6,32.6, 84.8,32.8, 84.5,32.8, 84.4, 31.7, 84.1,30.8, 83.9,30.1, 83.7,29.6, 83.2,28.8, 82.7,27.9, 82.4,27.3,             #Ligne11/12:  244-269
       93,32, 92.4,32, 91.8,32.1, 91.2,32.2, 90.6,32.3, 90,32.4, 89.5,32.5, 89,32.5, 88.7,32.6, 88,32.7, 85.6,31.5, 85.1,31.4, 83.9,32.2, 83.4,31.8, 83.2,31.4, 82.8,30.4, 82.2,29.8, 81.5,29.7, 81,30.1, 83.4,38.6, 83,37.6, 82.7,36.7,                 #Ligne13/14 :     270-291
       89.6,23, 88.9,24.5, 88.6,25.5, 88.3,26.5, 88,27.5, 87.7,28.5, 87.4,31, 87.3,32, 86.7,33.8, 85.2,36, 85.1,43.3, 87.5,35.4, 86.9,35, 85.8,35, 85.4,35.4, 84.7,34, 84,33.7, 83.6,33.5, 82.1,33.9              #RERA/RERB:  292-310
       ]


#Input = [[0,1,2],
#         [3,1,4]]
print(sum(Freq))
  
NbLines=len(Input)
Length=[len(Input[i]) for i in range (NbLines)]
print(Length)

Len=0
for i in range (NbLines):
  for j in range (len(Input[i])):
    if Input[i][j]>Len:
      Len=Input[i][j]
Len=Len+1
print(Len)
#Freq = [sum(Freq)/Len for i in range(Len)]

##TO DELETE STOPS:
DelStops=[]
for i in range(len(DelStops)):
  for j in range (NbLines):
    if (DelStops[i] in Input[j]):
      Input[j].remove(DelStops[i])
#Freq[14]=0


##WHEN A LINE OR A STATION HAS BEEN DELETED       n² comme complexité, pas de problème
DecreasePerNode=[0 for i in range(Len)]
nbDecrease=0
Input2=copy.deepcopy(Input)
Freq2=copy.deepcopy(Freq)
Coord2=copy.deepcopy(Coord)
LostPass=0
for i in range (Len):
  include=False
  for j in range (NbLines):
    for k  in range (len(Input[j])):
      if (Input[j][k]==i):
        include=True
  if (include==False):
    #print(i)
    LostPass=LostPass+Freq[i]
    for j in range (i-nbDecrease,Len-1):
      Freq2[j]=Freq2[j+1]
      Coord2[2*j]=Coord2[2*j+2]
      Coord2[2*j+1]=Coord2[2*j+3]
    for j in range(i,Len):
      DecreasePerNode[j]=DecreasePerNode[j]+1
    nbDecrease=nbDecrease+1
    for j in range (NbLines):
      for k  in range (len(Input[j])):
        if Input[j][k]>i:
          Input2[j][k]=Input2[j][k]-1
Input=copy.deepcopy(Input2)
Freq=copy.deepcopy(Freq2)
Coord=copy.deepcopy(Coord2)
Len=Len-nbDecrease
print(Len)
print(LostPass,"Disconnected Passengers")


Adj=[[[0 for i in range(Len)]for j in range(Len)]for k in range (NbLines)]
for i in range(NbLines):
  for j in range(len(Input[i])-1):
    I1=Input[i][j]
    I2=Input[i][j+1]
    Adj[i][I1][I2]=1
    Adj[i][I2][I1]=1

SumFreq=0
for i in range (Len):
  SumFreq=SumFreq+Freq[i]
print(SumFreq)

###Degree Centrality
#A voir si je définis comme: nombre de métro qui parte ou nombre de diretion dans laquelle je peux partir
import matplotlib.pyplot as plt

DC=[0 for i in range (Len)]
degmax=0
TotalDeg=0
for j in range(Len):
  deg=0
  for i in range(NbLines):
    for k in range(Len):
      if Adj[i][j][k]==1:
        deg=deg+1
        TotalDeg=TotalDeg+1
  DC[j]=deg
  if (deg>degmax):
    degmax=deg
    nodemax=j
print(DC)
print("stop: ",nodemax,"has maximal degree of: ", degmax)
print("The average degree centrality is: ",TotalDeg/Len)

DCdistr=[0 for i in range(14)]
Cnt14=[i for i in range(14)]
for i in range(Len):
  DCdistr[DC[i]]=DCdistr[DC[i]]+1

plt.plot(Cnt14,DCdistr)

#####################################
##### Closeness Centrality #########
#####################################



###Calcul de la matrice de plus court chemin pour Closeness Centrality
###Based on dijkstra algorithm
#Aide : buckets = [[0 for col in range(5)] for row in range(10)]


import time
import queue


def DijkstraForNode(Mat, stop):
  Help = queue.PriorityQueue()
  marked = [[False for i in range (NbLines)] for j in range (Len)]
  Help.put([0,stop,0])      #Only the first node doesn't need to have a specific line
  node=Help.get()
  for i in range (NbLines):
    marked[node[1]][i]=True
    for j in range(Len):
      if Adj[i][node[1]][j]==1:     
        Mat[stop][j][i]=1
        Help.put([node[0]+1,j,i])
        for k in range (NbLines):
          if (j in Input[k] and Mat[stop][j][k]>3):# and j!=14):
            Mat[stop][j][k]=3
            Help.put([3,j,k])

  while (Help.empty()==False):
    node=Help.get()
    if (marked[node[1]][node[2]]==False):            #Permet de limiter le nombre d'itération de la boucle à len
      marked[node[1]][node[2]]=True
      #Adjacent nodes on the same line
      for j in range(Len):
        if Adj[node[2]][node[1]][j]==1 and Mat[stop][j][node[2]]>node[0]+1:       #Il manque un truc pour vérifier si c'est pas déja dans la pq mais pas sur que nécessaire
          Mat[stop][j][node[2]]=Mat[stop][node[1]][node[2]]+1
          Help.put([node[0]+1,j,node[2]])

          #Different Lines on same node
          for k in range (NbLines):
            if (j in Input[k] and Mat[stop][j][k]>node[0]+3):# and j!=14):
              Mat[stop][j][k]=node[0]+3
              Help.put([node[0]+3,j,k])
  return Mat

t1=time.time()

MinDis=[[1000 for i in range(Len)]for j in range(Len)]
MinDisBis=[[[1000 for i in range (NbLines)] for j in range (Len)]for k in range (Len)]
           
for i in range(Len):
  MinDis[i][i]=0
  for j in range (NbLines):
    MinDisBis[i][i][j]=0


#Main Loop
for i in range(Len):  
  MinDis=DijkstraForNode(MinDisBis,i)

for i in range (Len):
  for j in range (Len):
    MinDis[i][j]=min(MinDisBis[i][j])


t2=time.time()
print("Computation time is: ",t2-t1,"seconds")

####Second Part of Closeness Centrality to have less execution time 

import matplotlib.pyplot as plt

Centrality=[0 for i in range (Len)]
ECC=[0 for i in range (Len)]
AvgCentrality=0
for i in range (Len):
  for j in range (Len):
    Centrality[i]=Centrality[i]+(MinDis[i][j])/((Len-1))   #distance moyenne pour normaliser       
    if MinDis[i][j]>ECC[i]:
      ECC[i]=MinDis[i][j]
for i in range (Len):
  AvgCentrality=AvgCentrality+Centrality[i]

print("Closeness Centrality", Centrality)
print("AvgCentrality",AvgCentrality)
print("AvgLength",AvgCentrality/Len)

Best=0
CenBest=100000
for i in range (Len):
  if Centrality[i]<CenBest:
    Best=i
    CenBest=Centrality[i]
#for i in range (int(Len/8)):
#  print (8*i, Centrality[8*i],"     ",8*i+1,Centrality[8*i+1],"     ",8*i+2, Centrality[8*i+2],"     ",8*i+3,Centrality[8*i+3],"      ",
#         8*i+4, Centrality[8*i+4],"     ",8*i+5,Centrality[8*i+5],"     ",8*i+6, Centrality[8*i+6],"     ",8*i+7,Centrality[8*i+7])
print(Best)
print(CenBest)

cnt30=[i for i in range(30)]
distrCC=[0 for i in range(30)]
for i in range (Len):
  distrCC[int(Centrality[i])]=distrCC[int(Centrality[i])]+1
londresCC=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 18, 29, 28, 15, 19, 19, 17, 14, 15, 12, 10, 9, 8, 4, 4, 3, 2, 2, 1]
plt.plot(cnt30,distrCC,'C1', label='Paris')
plt.plot(cnt30,londresCC,'C2',label='London')
plt.legend()
plt.grid(True)
print(distrCC)
print(sum(londresCC))

#####################################
##### Betweeness Centrality #########
#####################################

#Remarque: Le dernier du chemin est toujours pris dans Dis, pas le premier, par symmétrie ca met tout le monde sur pied d'égalité

import time
import queue
import numpy
from random import randint

def FillDis(StopA, StopB, NewVal, EdgeTo):
  Dis[StopA][StopB].append(NewVal)
  #print("hehe",StopB,NewVal)
  if (NewVal[0]!=StopA):
    FillDis(StopA,StopB,EdgeTo[NewVal[0]][NewVal[1]],EdgeTo)


def DijkstraForNode(Mat, stop):
  Help = queue.PriorityQueue()
  NodeTo2 = [[[] for i in range(NbLines)]for j in range (Len)]               #(Previous Node, Line in the connexion)
  NodeTo = [[] for i in range (Len)]               #(Previous Node, Line in the connexion)
  marked = [[False for i in range (NbLines)] for j in range (Len)]

  Help.put([0,stop,0,0])      #Only the first node doesn't need to have a specific line (priority, node, line , previous node)
  node=Help.get()

  for i in range (NbLines):
    marked[node[1]][i]=True
    for j in range(Len):
      if Adj[i][node[1]][j]==1:     
        Mat[stop][j][i]=1
        Help.put([node[0]+1,j,i,stop])
        NodeTo2[j][i]=[stop,i]
        for k in range (NbLines):
          if (j in Input[k] and Mat[stop][j][k]>Penalty):# and j!=14):
            Mat[stop][j][k]=Penalty
            Help.put([Penalty,j,k,stop])
            NodeTo2[j][k]=[stop,i]

  while (Help.empty()==False):
    node=Help.get()
    if (marked[node[1]][node[2]]==False):
      marked[node[1]][node[2]]=True
      
      #Adjacent nodes on the same line
      for j in range(Len):
        if Adj[node[2]][node[1]][j]==1 and Mat[stop][j][node[2]]>node[0]+1:      #Il manque un truc pour vérifier si c'est pas déja dans la pq mais pas sur que nécessaire
          Mat[stop][j][node[2]]=Mat[stop][node[1]][node[2]]+1
          Help.put([node[0]+1,j,node[2],node[1]])
          NodeTo2[j][node[2]]=[node[1],node[2]]
          for k in range (NbLines-2):
            if (j in Input[k] and Mat[stop][j][k]>node[0]+Penalty):# and j!=14):
              Mat[stop][j][k]=node[0]+Penalty
              Help.put([node[0]+Penalty,j,k,node[1]])
              NodeTo2[j][k]=[node[1],node[2]]
          for k in range (NbLines-2,NbLines):
            if (j in Input[k] and Mat[stop][j][k]>node[0]+Penalty*2):# and j!=14):
              Mat[stop][j][k]=node[0]+Penalty*2
              Help.put([node[0]+Penalty*2,j,k,node[1]])
              NodeTo2[j][k]=[node[1],node[2]]
  for i in range(Len):
    if (stop!=i):
      a=1001
      for j in range(len(MinDisBis[stop][i])):
        if (MinDisBis[stop][i][j]<a):
          a=MinDisBis[stop][i][j]
          k=j
      FillDis(stop, i,NodeTo2[i][k], NodeTo2)
  return Mat

t1=time.time()

Penalty=3
MinDisBis=[[[1000 for i in range (NbLines)] for j in range (Len)]for k in range (Len)]
Dis=[0 for i in range(Len)]           
for i in range(Len):
  for j in range (NbLines):
    MinDisBis[i][i][j]=0
  Dis[i]=[[] for i in range(Len)]


for i in range(Len):
  DijkstraForNode(MinDisBis,i)

t2=time.time()
print("execution time: ",t2-t1)

### Deuxième partie pour Betweeness Cenntrality 


BetwCentrality=[0 for i in range (Len)]
BetwCentralityLine=[0 for i in range (NbLines)]
NbPassLine=[0 for i in range(NbLines)]
BetwCentralityEdge=[[0 for i in range(NbLines)] for j in range (Len)]
NbConnections=[[0,i] for i in range (Len)]
weightEdges=[[0 for i in range(Len)]for j in range (Len)]
for i in range(Len):
  for j in range(Len):
    Adder=Freq[i]*Freq[j]/(SumFreq-Freq[i])
    NbPassLineBis=[False for i in range(NbLines)]
    for k in range(len(Dis[i][j])):
      Current = Dis[i][j][k][0]
      Current2 = Dis[i][j][k][1]
      BetwCentrality[Current]=BetwCentrality[Current]+Adder
      BetwCentralityLine[Current2]=BetwCentralityLine[Current2]+Adder
      BetwCentralityEdge[Current][Current2]=BetwCentralityEdge[Current][Current2]+Adder
      if k==len(Dis[i][j])-1:
        NbPassLineBis[Current2]=True

    for k in range (NbLines):
      if NbPassLineBis[k]==True:
        NbPassLine[k]=NbPassLine[k]+Adder
    for k in range(len(Dis[i][j])-1):
      if (Dis[i][j][k][1]!=Dis[i][j][k+1][1]):
        NbConnections[Dis[i][j][k][0]][0]=NbConnections[Dis[i][j][k][0]][0]+1*Freq[i]*Freq[j]/(SumFreq-Freq[i])
      weightEdges[Dis[i][j][k][0]][Dis[i][j][k+1][0]]=weightEdges[Dis[i][j][k][0]][Dis[i][j][k+1][0]]+Freq[i]*Freq[j]/(SumFreq-Freq[i])
      weightEdges[Dis[i][j][k+1][0]][Dis[i][j][k][0]]=weightEdges[Dis[i][j][k][0]][Dis[i][j][k+1][0]]
    if len(Dis[i][j])>0:
      weightEdges[j][Dis[i][j][0][0]]=weightEdges[j][Dis[i][j][0][0]]+Freq[i]*Freq[j]/(SumFreq-Freq[i])
      weightEdges[Dis[i][j][0][0]][j]=weightEdges[j][Dis[i][j][0][0]]
#for i in range (Len):
#  BetwCentrality[i]=BetwCentrality[i]/(Len-1)
#  NbConnections[i][0]=NbConnections[i][0]/Len
NbConnections.sort(reverse=True)
print("Number of weighted connections per stop is ", NbConnections)
for i in range (NbLines):
  BetwCentralityLine[i]=int(BetwCentralityLine[i])
  NbPassLine[i]=int(NbPassLine[i])
print("Betweeness Centrality Line is ", BetwCentralityLine)
print("The number of passengers per line is : ",NbPassLine)
print("Betweeness Centrality" ,BetwCentrality)
HELP=[[BetwCentrality[i],i] for i in range(Len)]
HELP.sort(reverse=True)
print("Betweeness Centrality Trié par arrêt",HELP)
Best=0
CenBest2=0
for i in range (Len):
  if BetwCentrality[i]>CenBest2:
    Best=i
    CenBest2=BetwCentrality[i]
#for i in range (int(Len/8)):
#  print (8*i, BetwCentrality[8*i],"     ",8*i+1,BetwCentrality[8*i+1],"     ",8*i+2, BetwCentrality[8*i+2],"     ",8*i+3,BetwCentrality[8*i+3],"      ",
#         8*i+4, BetwCentrality[8*i+4],"     ",8*i+5,BetwCentrality[8*i+5],"     ",8*i+6, BetwCentrality[8*i+6],"     ",8*i+7,BetwCentrality[8*i+7])
avgBC=0
for i in range(Len):
  avgBC=avgBC+BetwCentrality[i]
avgBC=avgBC/Len
print("Average BC is: ",avgBC)
print(Best)
print("maximum BC is: ",CenBest2)

print("Total number of connections is" , sum([NbConnections[i][0]for i in range(Len)]))

print(sum(BetwCentralityLine))

#Betweeness Centrality of the edges sorted
Aux=[]
for i in range(Len):
  for j in range (NbLines):
    if (BetwCentralityEdge[i][j] != 0):
      Aux.append([BetwCentralityEdge[i][j],i,j])
Aux.sort(reverse=True)
print(Aux)

###Tentative d'implémentation du Salience filter:
###Partie 1
SalienceNumbers=[[0 for i in range (Len)] for j in range (Len)]
for i in range(Len):
  UsedEdges=[[False for i in range (Len)] for j in range (Len)]   #False
  for j in range(Len):
    Runner=j
    for k in range(len(Dis[i][j])):
      Previous=Runner
      Runner = Dis[i][j][k][0]
      UsedEdges[Previous][Runner]=True #True
      UsedEdges[Runner][Previous]=True #True
  for j in range(Len):
    for k in range(Len):
      if (UsedEdges[j][k]==True):         #==True
        SalienceNumbers[j][k]=SalienceNumbers[j][k]+1     #+1

###Partie 2
AuxSal=[]
EdgesLeftSalience=[]
for i in range(Len):
  for j in range (i,Len):
    if (SalienceNumbers[i][j] > 310 and SalienceNumbers[i][j]>0):
      AuxSal.append([SalienceNumbers[i][j],i,j])
      EdgesLeftSalience.append([i,j])
AuxSal.sort(reverse=True)
print("AuxSal ",AuxSal)
print("Number of edges kept from the original 372 is ",len(AuxSal))           #346 normal, 207 core

NbLeftLine=[0 for i in range(NbLines)]
for i in range (len(AuxSal)):
  nb1=AuxSal[i][1]
  nb2=AuxSal[i][2]
  for j in range(NbLines):
    for k in range(len(Input[j])-1):
      if Input[j][k]==nb1 and Input[j][k+1]==nb2:
        NbLeftLine[j]=NbLeftLine[j]+1
      if Input[j][k+1]==nb1 and Input[j][k]==nb2:
        NbLeftLine[j]=NbLeftLine[j]+1
VertLine=[Length[i]-1 for i in range (NbLines)]
PercLeft=[int(100*NbLeftLine[i]/VertLine[i]) for i in range(NbLines)]
print("Nb edge per line +1   ", VertLine)

SalLine=[0 for i in range (NbLines)]
for i in range (NbLines):
  for j in range(len(Input[i])-1):
    SalLine[i]=SalLine[i]+SalienceNumbers[Input[i][j]][Input[i][j+1]]
print("Min Nb edge left      ", [4, 2, 9, 0, 6, 7, 0, 14, 2, 17, 9, 2, 1, 9, 16, 3, 4, 1])
print("Nb edge left per lines", NbLeftLine)
print("Percentage Left :", PercLeft)
print("Sum of numbers per Line", SalLine)

###Tentative d'implémentation du Disparity filter:
###Faut que je décides si je prends la moyenne ou le max des deux valeurs pour chaque arrête, je penses que ca change quand même pas mal
#weight=[[0 for i in range(Len)]for j in range (Len)]
weight2=[[0 for i in range(Len)]for j in range (Len)]
weightF=[[0 for i in range(Len)]for j in range (Len)]

for i in range (Len):
  sumWeight=sum(weightEdges[i])
  for j in range(Len):
    weight2[i][j]=weightEdges[i][j]/sumWeight

for i in range(Len):
  for j in range (Len):
    if weight2[i][j]!=0:
      weightF[i][j]=1-(1-weight2[i][j])**(DC[i]-1)


AuxDis=[]
EdgesLeftDisp=[]
for i in range(Len-1):
  for j in range (i+1,Len):
    weightF[i][j]=max(weightF[i][j],weightF[j][i])#/2
    weightF[j][i]=weightF[i][j]
    if (weightF[i][j] > 0.5 and weightF[i][j]>0):
      AuxDis.append([weightF[i][j],i,j])
      EdgesLeftDisp.append([i,j])
AuxDis.sort(reverse=True)
print("AuxDis ",AuxDis)
print("Number of edges kept from the original 372 is ",len(AuxDis))           #346 normal, 207 core

NbLeftLineDis=[0 for i in range(NbLines)]
for i in range (len(AuxDis)):
  nb1=AuxDis[i][1]
  nb2=AuxDis[i][2]
  for j in range(NbLines):
    for k in range(len(Input[j])-1):
      if Input[j][k]==nb1 and Input[j][k+1]==nb2:
        NbLeftLineDis[j]=NbLeftLineDis[j]+1
      if Input[j][k+1]==nb1 and Input[j][k]==nb2:
        NbLeftLineDis[j]=NbLeftLineDis[j]+1
PercLeft=[int(100*NbLeftLineDis[i]/VertLine[i]) for i in range(NbLines)]
print("Nb edge per line   ", VertLine)
#print("Min Nb edge left      ", [10, 2, 9, 0, 6, 7, 0, 14, 2, 17, 9, 2, 1, 9, 16, 3])
print("Nb edge left per lines", NbLeftLineDis)
print("Percentage Left :", PercLeft)

###Weight Treshold
AuxDisW=[]
EdgesLeftWeightTresh=[]
for i in range(Len-1):
  for j in range (i+1,Len):
    if (weightEdges[i][j] > 60 and weightEdges[i][j]>0):
      AuxDisW.append([weightEdges[i][j],i,j])
      EdgesLeftWeightTresh.append([i,j])
AuxDisW.sort(reverse=True)
print("AuxDisW ",AuxDisW)
print("Number of edges kept from the original 372 is ",len(AuxDisW))           #346 normal, 207 core

NbLeftLineDis=[0 for i in range(NbLines)]
for i in range (len(AuxDisW)):
  nb1=AuxDisW[i][1]
  nb2=AuxDisW[i][2]
  for j in range(NbLines):
    for k in range(len(Input[j])-1):
      if Input[j][k]==nb1 and Input[j][k+1]==nb2:
        NbLeftLineDis[j]=NbLeftLineDis[j]+1
      if Input[j][k+1]==nb1 and Input[j][k]==nb2:
        NbLeftLineDis[j]=NbLeftLineDis[j]+1
PercLeft=[int(100*NbLeftLineDis[i]/VertLine[i]) for i in range(NbLines)]
print("Nb edge per line   ", VertLine)
#print("Min Nb edge left      ", [10, 2, 9, 0, 6, 7, 0, 14, 2, 17, 9, 2, 1, 9, 16, 3])
print("Nb edge left per lines", NbLeftLineDis)
print(PercLeft)

import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
for i in range(NbLines):
  G.add_nodes_from(Input[i])
  for j in range(len(Input[i])-1):
    G.add_edge(Input[i][j],Input[i][j+1])
print(G.number_of_nodes())

#options = {    'node_color': 'black',    'node_size': 100,    'width': 3}
 

pos =	{i: (Coord[2*i+1],Coord[2*i]) for i in range (Len)}

plt.figure(figsize=(15,10))

TotalPass=[]
for i in range (Len):
  TotalPass.append([NbConnections[i][0]+2*Freq[NbConnections[i][1]],NbConnections[i][1]])

NodeSize=[5 for i in range(Len)]
NodeColor=['black' for i in range(Len)]
for i in range (Len):
  j=TotalPass[i][1]
  #NodeSize[j]=TotalPass[i][0]

nx.draw_networkx_nodes(G, pos,node_color=NodeColor,node_size=NodeSize,alpha=0.8)
ColorLine=['gold','b','olive','lightskyblue','magenta','darkorange','lightgreen','pink','palegreen','plum','y','peru','brown','darkgreen','lightblue','darkviolet','red','dodgerblue']
ColorLine=['black' for i in range (NbLines)]

he=0
for i in range(NbLines):
  for j in range(len(Input[i])-1):
    if [Input[i][j],Input[i][j+1]] in EdgesLeftDisp or [Input[i][j+1],Input[i][j]] in EdgesLeftDisp:
      nx.draw_networkx_edges(G, pos,edgelist=[(Input[i][j],Input[i][j+1])],width=3, alpha=1,edge_color=ColorLine[i])
      he=he+1
    elif [Input[i][j],Input[i][j+1]] in EdgesLeftSalience or [Input[i][j+1],Input[i][j]] in EdgesLeftSalience:
      nx.draw_networkx_edges(G, pos,edgelist=[(Input[i][j],Input[i][j+1])],width=3, alpha=1,edge_color=ColorLine[i])
      he=he+1
    elif [Input[i][j],Input[i][j+1]] in EdgesLeftWeightTresh or [Input[i][j+1],Input[i][j]] in EdgesLeftWeightTresh:
      nx.draw_networkx_edges(G, pos,edgelist=[(Input[i][j],Input[i][j+1])],width=3, alpha=1,edge_color=ColorLine[i])
      he=he+1
    else:
      nx.draw_networkx_edges(G, pos,edgelist=[(Input[i][j],Input[i][j+1])],width=3, alpha=0.05,edge_color=ColorLine[i])
print('Nbextractededges is ',he)

RankingWithLine=[]
#for i in range (len(AuxDisW)):
#  BC=AuxDisW[i][0]/20
#  n1=AuxDisW[i][1]
#  n2=AuxDisW[i][2]
#  for j in range(NbLines):
#    for k in range(len(Input[j])-1):
#      if Input[j][k]==n1 and Input[j][k+1]==n2:
#        nx.draw_networkx_edges(G, pos,edgelist=[(n1,n2)],width=BC, alpha=1, edge_color=ColorLine[j])
#        RankingWithLine.append([AuxDisW[i][0],AuxDisW[i][1],AuxDisW[i][2],j])
#      if Input[j][k]==n2 and Input[j][k+1]==n1:
#        nx.draw_networkx_edges(G, pos,edgelist=[(n2,n1)],width=BC, alpha=1, edge_color=ColorLine[j])
#        RankingWithLine.append([AuxDisW[i][0],AuxDisW[i][1],AuxDisW[i][2],j])
#print(RankingWithLine)
plt.show()

