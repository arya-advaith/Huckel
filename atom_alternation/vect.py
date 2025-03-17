import pandas as pd
import matplotlib.pyplot as plt


list = [4,8,16,32,64,128,256,512,1024]

m=0
for i in list:
    x = pd.read_csv('eigenvectors_'+str(i)+'e_2a2b1close.txt',sep='\t',header=None)
    x= x.dropna(axis=1)
    for j in range(x.shape[1]):
        plt.scatter(x[j][0],x[j][1],color='red')
    plt.show()
