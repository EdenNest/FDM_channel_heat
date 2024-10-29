#                                                          FAKHTE TAGHI SHOKRGOZAR 96108442

#                                                          IMPORT LIBRARIES
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#                                                        ASKING FOR DELTA X AND INSIDE TEMPERATURE
deltax =0 
Tin=0
while not (deltax ==0.01 or deltax == 0.005):
    try:
        deltax=float(input('please write ONLY 0.005 or 0.01 for delta x:'))
    except:
        print('\n'*4)
        print(' !!!!!!!!!!!   ONLY 0.005 or 0.01 !!!!!!!!')
        print('\n'*4)
    else:
        if not (deltax ==0.01 or deltax == 0.005)  :
            
            print('\n'*4)
            print('!          !!!!!!!    ONLY 0.005 or 0.01  !!!!!')
            print('\n'*4)
while not ( Tin==600 or Tin==500 or Tin==700):
    try:
        Tin=float(input('please write 500 or 600 or 700 for T inside:'))
    except:
        print('\n'*4)
        print(' !!!!!!!!!!!   ONLY 500 or 600 or 700 !!!!!!!!')
        print('\n'*4)
    else:
        if not ( Tin==600 or Tin==500 or Tin==700)  :
            print('\n'*4)
            print(' !!!!!!!!!!!   ONLY 500 or 600 or 700 !!!!!!!!')
            print('\n'*4)
       
#                                                     GIVEN DATA 
k=1
h=50
Bi=h*deltax/k
xout=0.06
xin=0.02
t_inf=300
#                                                        DEFINING NODES BASED ON DELTA X
up=int(0.03/deltax)+1
left=int(0.02/deltax)+1
nodes=int((up+up-left+1)*(left)/2)
Cnodes=[[0 for i in range(nodes)] for j in range(nodes)]   #this is the coefficient matrix
B=[0 for i in range(nodes)]                             #this is  constant vector   :   Cnodes*Ans=B
#                                                      building  coefficient of nots for upper surface
for i in range(up-1):                           
    Cnodes[i][i]=h*deltax/k+2
    Cnodes[i+1][i+2]=-0.5
    Cnodes[i+1][i]=-0.5
    Cnodes[i][up+i]=-1
    B[i]=h*deltax*t_inf/k
    B[i+1]=h*deltax*t_inf/k
Cnodes[up-1][up-2]=-1
Cnodes[up-1][up]=0
Cnodes[up-1][up-1]=h*deltax/k+1
Cnodes[0][1]=-1
#                                                     building  coefficient of nots for middle nots
for j in range(up-1):
    i=j+up
    if i!=nodes-(up-left+1)-1:
        Cnodes[i][i-up]=Cnodes[i][i+up-1]=Cnodes[i][i-1]=Cnodes[i][i+1]=1
    else:
       Cnodes[i][i-up]=Cnodes[i][i-1]=Cnodes[i][i+1]=1 
    Cnodes[i][i]=-4
Cnodes[up][up+1]=Cnodes[i][i-1]=Cnodes[i][i-j-2]=2
Cnodes[up][up-1]=Cnodes[i][i+1]=0
if i!=nodes-(up-left+1)-1:
    Cnodes[i][i+up-1]=0
   
if left>3:
    x=up-1
    for j in range(up-2):
        i=j+2*up-1
        Cnodes[i][i-x]=Cnodes[i][i+x-1]=Cnodes[i][i-1]=Cnodes[i][i+1]=1
        Cnodes[i][i]=-4
    Cnodes[2*up-1][2*up-1+1]=Cnodes[i][i-1]=Cnodes[i][i-j-2]=2
    Cnodes[2*up-1][2*up-1-1]=Cnodes[i][i+1]=Cnodes[i][i+x-1]=0
    x=up-2
    for j in range(up-3):
        i=j+3*up-3
        if i!=nodes-(up-left+1)-1:
            Cnodes[i][i-x]=Cnodes[i][i+x-1]=Cnodes[i][i-1]=Cnodes[i][i+1]=1
        else:
            Cnodes[i][i-x]=Cnodes[i][i-1]=Cnodes[i][i+1]=1
        Cnodes[i][i]=-4
    Cnodes[3*up-3][3*up-3+1]=Cnodes[i][i-1]=Cnodes[i][i-j-2]=2
    Cnodes[3*up-3][3*up-3-1]=Cnodes[i][i+1]=0

#                                                               lower nots with coefficient of 1 (because we know them!!)
for j in range(up-left+1):
    i=j+nodes-(up-left+1)
    Cnodes[i][i]=1
    B[i]=Tin
#                                                       SOLVING SYSTEM OF LINEAR EQUATIONS
Cnodes = np.array(Cnodes)
B= np.array(B)
Ans  = np.linalg.solve(Cnodes,B)    
#                                                     CALCULATING Q
w=0
for i in range(1,up-1):
    w+=Ans[i]    
w+=(Ans[0]+Ans[up-1])/2
s=2*np.pi/(0.93*np.log(3)-0.05)
qsf=abs(w/(up-1)-Tin)*(s)*k
w=w-300*(up-1)
q=h*(deltax)*(abs(w))*8
print('\n'*2)
#                                                   SHOWING THE RESULT IN A CATCHY WAY !
Ans=list(map(lambda x : str(int(x)) , list(Ans)))
ANS=[]
b=0
for i in range(left):
    a=b
    b=(i+1)*up-int((i+2)*(i+1)/2)+i+1
    ANS.append(list(map(lambda x : int(x) , list(Ans[a:b]))))
    print('                 ' ,'   '.join(Ans[a:b]))
    print('\n')
print('\n'*3)
print( '                 q only this upper part  =' , q/8)
print('\n')
print( '                 q total per unit lenght =' , q)
print( '                 q total shape factor =' , qsf)
#                                                                         PLOTTING          
q=int(0.01/deltax)
def z(x,y):
    x=int(x)
    y=int(y)
    if abs(x)<q and abs(y)<q:
        return Tin
    if x>=0 and y>=0 and x<=y:
        return ANS[int(left+q-1-y)][x]
    elif x<0 or y<0:
        x=abs(x)
        y=abs(y)
        if x>y:
            return ANS[int(left+q-1-x)][y]
        else:
            return ANS[int(left+q-1-y)][x]
    else:
        return ANS[int(left+q-1-x)][y]
print('\n'*2)
print('                 Show the plot? Yes: enter 1   No: enter 2'            )     
xx=np.linspace(-(up-1), up-1 , 2*up-1)
yy=np.linspace(-(left+q-1), (left+q-1) , 2*(left+q-1)+1)
zz = [1,2,3]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(xx, yy)
zs = np.array([z(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)
ax.plot_surface(X, Y, Z)
ax.set_xlabel('X')
ax.set_ylabel('Y ')
ax.set_zlabel('TEMPRATURE')
print('\n'*5)
qq=int(input('                    ' ))
if qq==1:
    plt.show()   
