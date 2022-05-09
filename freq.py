import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def histogram(value, filename, df):
    #df=pd.read_csv("gmon.csv",  sep=';')
    if value=="BAND":
        df=df[value].astype(str).to_numpy()
    else:
        df=df[value].to_numpy()
        df = np.where(df == 1, 0, df)
    unique_elements, counts_elements = np.unique(df, return_counts=True)
    #
    # #rint((np.asarray((unique_elements, counts_elements)))[1])
    # #
    print(unique_elements)
    print(counts_elements)

    helper = np.arange(len(unique_elements))
    print(helper)
    plt.bar( helper,counts_elements, color='b')
    plt.xticks(ticks=helper, labels=unique_elements, rotation=90)

    plt.xlabel('Variables')
    plt.ylabel('Repeticiones')
    #plt.show()
    plt.tight_layout()
    plt.savefig(filename,  dpi=250)
    plt.close()

def gps_(df, filename):
    filename= os.path.join(filename, 'gps')

    gps=df['GPS_ACCURACY'].to_numpy()
    time=df['TIME'].to_numpy()

    l=len(time)
    ponit=15
    l=l/ponit
    lista=[]
    for i in range(ponit):
        lista.append(int(i*l))

    plt.plot(time, gps)
    plt.xticks(lista,rotation=90)
    plt.xlabel('hora')
    plt.ylabel('metros')
    plt.tight_layout()
    plt.savefig(filename,  dpi=250)
    plt.close()
