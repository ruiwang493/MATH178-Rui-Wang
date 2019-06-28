import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

def plotFig(N=1000, rseed=42):
	figure, ax = plt.subplots(figsize=(6,1))
	figure.subplots_adjust(left=0, right=1, bottom=0, top=1)
	ax.axis('off')
	ax.text(0.5, 0.4, 'MATH', va='center', ha='center', weight='bold', size=85)
	figure.savefig('math.png')
	plt.close(figure)

	from matplotlib.image import imread
	data = imread('math.png')[::-1, :, 0].T
	rng = np.random.RandomState(rseed)
	X = rng.rand(7 * N, 2)
	i,j = (X * data.shape).astype(int).T
	mask = (data[i,j] < 1)
	X = X[mask]
	X[:, 0] *= (data.shape[0] / data.shape[1])
	X = X[:N]
	return X[np.argsort(X[:,0])]


X = plotFig(1000)
colorize = dict(c=X[:,0], cmap=plt.cm.get_cmap('rainbow', 4))
plt.scatter(X[:,0], X[:,1], **colorize)
plt.axis('equal')
plt.show()