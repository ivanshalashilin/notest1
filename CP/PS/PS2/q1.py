#LU decomposition

from numpy import matmul
from numpy.linalg import inv
import numpy as np
import matplotlib.pyplot as plt

mat = 1/6*np.array(
    [
        [5,4,3,2,1],
        [4,8,6,4,2],
        [3,6,9,6,3],
        [2,4,6,8,4],
        [1,2,3,4,5],
]
)

vecB = np.array(
        [1,2,3,4,5]
)

matI = np.linalg.inv(mat)

def MultiplyRowCol(MatA,MatB, RowA, ColB):
    if len(MatB) != len(MatA):
        pass
    
    return np.dot(MatA[RowA],MatB[:,ColB])



MultiplyRowCol(mat, matI, 0,0)



def LUDecomp(mat):
    if len(mat[:,0]) != len(mat[0]):
        pass
    Lower = np.identity(len(mat[0]))
    Upper = np.zeros(np.shape(mat))
    for j in range(len(mat[0])):#for a particular row
        for i in range(j+1):#for a particular column
            if i == 0:
                Upper[i][j] = mat[i][j]#/Lower[i][i]#(==1)
            else:
                Upper[i][j] = mat[i][j]
                for k in range(i):
                    Upper[i][j]-=Lower[i][k]*Upper[k][j]#/Lower[i][i]#(==1)
        #find l in a column
        for i in range(j+1,len(mat[0])):
            if j == 0:
                Lower[i][j] = mat[i][j]/Upper[j][j]#(!=1)
            else:
                Lower[i][j] = mat[i][j]/Upper[j][j]
                for k in range(j):
                    Lower[i][j]-= Lower[i][k]*Upper[k][j]/Upper[j][j]
    
    if np.trace(np.matmul(Lower,Upper) - mat) <1:
        #print("it works")
        return Upper, Lower
    print("nah")

def ForwardSub(Lower, vecB):
    vecU = np.zeros(len(Lower[0]))
    for j in range(len(vecB)):
        if j == 0:
            vecU[j] = vecB[j]/Lower[j][j]
        else:
            vecU[j] =vecB[j]/Lower[j][j]
            for i in range(j):
                vecU[j] -= Lower[j][i]*vecU[i]/Lower[j][j]
    return np.transpose(vecU) 


def BackwardSub(Upper, vecU):
    vecX = np.zeros(len(Upper[0]))
    for j in range(len(vecX)):
        r = len(vecX)-1-j
        if j == 0:
            vecX[r] = vecU[r]/Upper[r][r]
        else:
            vecX[r] = vecU[r]/Upper[r][r]
            for i in range(j):
                k = len(vecX)-1-i
                vecX[r] -= Upper[r][k]*vecX[k]/Upper[r][r]
    
    
    return np.transpose(vecX) 


Upper, Lower = LUDecomp(mat)
vecU = ForwardSub(Lower, vecB)
vecX = BackwardSub(Upper, vecU)


'''
Find inverse by setting B to the identity
(bottom of page 18)
'''
def InvertMat(mat):
    #get the inverse, identity, upper and lower mats
    matInverse = np.zeros([len(mat),len(mat)])
    Identity = np.identity(len(mat[0]))
    Upper, Lower = LUDecomp(mat)
    #compute x for b = 'identity vector'
    #via LU -> FB sub
    for i in range(len(mat[0])):
        VecIdentity = Identity[:,i] #'identity vector'
        Vec_Y_Inverse = ForwardSub(Lower, VecIdentity)
        Vec_col_Inverse = BackwardSub(Upper, Vec_Y_Inverse)
        matInverse[:,i] = Vec_col_Inverse
    return matInverse

def ResdiualVector(vecX,matA,vecB):
    #find '0' vector
    ErrorVec = np.dot(matA, vecX) - vecB
    #sum the components
    sum = 0
    for i in range(len(ErrorVec)):
        sum +=np.abs(ErrorVec[i])
    return sum/len(ErrorVec)

def ResidualMat(mat):
    #get the inverse (benchmark function)
    matInverse = InvertMat(mat)
    #subtract from the identity
    RMatrix = np.matmul(matInverse,mat)-np.identity(len(mat))
    #sum the entries
    sum = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            sum += np.abs(RMatrix[i][j])
    return sum/(len(mat)**2)

RVec = ResdiualVector(vecX,mat, vecB)
RMat = ResidualMat(mat)

def GeneralMat(n=5):
    #Upper
    Upper = np.zeros([n,n])
    for j in range(n):
        for i in range(n-j-1):
            k = n-i-1
            Upper[j][k]= (j+1)*(i+1)
    #Lower
    Lower = np.zeros([n,n])
    for j in range(n):
        k = n-j-1
        for i in range(n-j):
            Lower[k][i]= (j+1)*(i+1)
    return (Lower + Upper)/(n+1)

grain = 40
x = np.arange(2,grain+2)
RVec = np.zeros(len(x), dtype = float)
RMat = np.zeros(len(x))
for i in range(grain):
    mat = GeneralMat(x[i])
    vecB = np.arange(1,i+3)
    Upper, Lower = LUDecomp(mat)
    vecU = ForwardSub(Lower, vecB)
    vecX = BackwardSub(Upper, vecU)
    RVec[i] = ResdiualVector(vecX,mat, vecB)
    RMat[i] = ResidualMat(mat)

#make figure
fig, ax = plt.subplots(1,1)
ax.plot(x, RVec, '--', color = 'purple', label = 'maximum overlap')
ax.tick_params(axis='y', labelcolor='red')
#form second axes
ax2 = ax.twinx()
ax2.tick_params(labelsize = 20)
ax2.plot(x, RMat, color = 'red', label = '')
plt.show()