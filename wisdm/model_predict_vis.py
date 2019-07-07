from mpl_toolkits import mplot3d
import pandas as pd
import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
filepath="data/WISDM_ar_v1.1_prep.csv"

df = pd.read_csv(filepath, names=['User ID', 'Label', 'Timestamp', 'accelX', 'accelY', 'accelZ'], index_col=False)
cols=[1,3,4,5]
df2=df[df.columns[cols]]
sitting=df2.loc[df['Label']=="Sitting"]
jogging=df2.loc[df['Label']=="Jogging"]
upstairs=df2.loc[df['Label']=="Upstairs"]
downstairs=df2.loc[df['Label']=="Downstairs"]
walking=df2.loc[df['Label']=="Walking"]
standing=df2.loc[df['Label']=="Standing"]
ax.scatter(sitting.iloc[:,1], sitting.iloc[:,2], sitting.iloc[:,3], s=1, c="yellow")
#plt.show()
ax.scatter(jogging.iloc[:,1], jogging.iloc[:,2], jogging.iloc[:,3], s=1, c="red")
#plt.show()
ax.scatter(upstairs.iloc[:,1], upstairs.iloc[:,2], upstairs.iloc[:,3], s=1, c="blue")
#plt.show()
ax.scatter(downstairs.iloc[:,1], downstairs.iloc[:,2], downstairs.iloc[:,3], s=1, c="green")
#plt.show()
ax.scatter(walking.iloc[:,1], walking.iloc[:,2], walking.iloc[:,3], s=1, c="black")
#plt.show()
ax.scatter(standing.iloc[:,1], standing.iloc[:,2], standing.iloc[:,3], s=1, c="purple")
plt.show()


