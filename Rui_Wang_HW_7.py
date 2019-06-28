import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.metrics import pairwise_distances
from matplotlib.image import imread
from sklearn.manifold import MDS
from mpl_toolkits import mplot3d

def plotFig(N=1000, rseed=42):
	figure, ax = plt.subplots(figsize=(6,1))
	figure.subplots_adjust(left=0, right=1, bottom=0, top=1)
	ax.axis('off')
	ax.text(0.5, 0.4, 'MATH', va='center', ha='center', weight='bold', size=85)
	figure.savefig('math.png')
	plt.close(figure)

	data = imread('math.png')[::-1, :, 0].T
	rng = np.random.RandomState(rseed)
	X = rng.rand(7 * N, 2)
	i,j = (X * data.shape).astype(int).T
	mask = (data[i,j] < 1)
	X = X[mask]
	X[:, 0] *= (data.shape[0] / data.shape[1])
	X = X[:N]
	return X[np.argsort(X[:,0])]

def rotate(X, angle):
	theta =np.deg2rad(angle)
	rad = [[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]]
	return np.dot(X, rad)

def random_projection(X, dimension=3, rseed=42):
	assert dimension >= X.shape[1]
	rng = np.random.RandomState(rseed)
	C = rng.randn(dimension, dimension)
	e, V = np.linalg.eigh(np.dot(C, C.T))
	return np.dot(X, V[:X.shape[1]])


# Making/Rotating the shape
X = plotFig(1000)
colorize = dict(c=X[:,0], cmap=plt.cm.get_cmap('rainbow', 4))
plt.scatter(X[:,0], X[:,1], **colorize)
X2 = rotate(X,45)+1
plt.scatter(X2[:,0], X2[:,1], **colorize)
plt.axis('equal')
plt.show()

# Distance Matrix
D = pairwise_distances(X)
D.shape
D2= pairwise_distances(X2)
np.allclose(D,D2)
plt.imshow(D, zorder=2, cmap='Blues', interpolation='nearest')
plt.colorbar()
plt.show()

#MDS
model = MDS(n_components=2, dissimilarity='precomputed', random_state=1)
out = model.fit_transform(D)
plt.scatter(out[:,0], out[:,1], **colorize)
plt.axis('equal')
plt.show()

X3 = random_projection(X,3)
X3.shape
ax = plt.axes(projection='3d')
ax.scatter3D(X3[:,0], X3[:,1], X3[:,2], **colorize)
ax.view_init(azim=70, elev=50)
plt.show()

model3=  MDS(n_components=2, random_state=1)
out3 = model3.fit_transform(X3)
plt.scatter(out3[:,0], out3[:,1], **colorize)
plt.axis('equal')
plt.show()