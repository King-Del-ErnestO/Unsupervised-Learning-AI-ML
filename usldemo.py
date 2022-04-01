from sklearn.datasets import load_sample_image
from matplotlib import pyplot as plt
import numpy as np
#import cv2 (we can use cv2 to get an image(png) from your sys and work with it instead)

china = load_sample_image('china.jpg')

ax = plt.axes(xticks=[], yticks=[])
# ax.imshow(china)

# print(china.shape)

data = china / 255.0 #use 0...1 scale
data = data.reshape(427 * 640, 3)
print(data.shape)

def plot_pixels(data, title, colors=None, N=10000):
    if colors is None:
        colors = data

    #choose a rsndom subset
    rng = np.random.RandomState(0)
    i = rng.permutation(data.shape[0])[:N]
    colors = colors[i]
    R, G, B = data[i].T

    fig, ax = plt.subplots(1, 2, figsize=(16, 6))
    ax[0].scatter(R, G, color=colors, marker='.')
    ax[0].set(xlabel='Red', ylabel='Green', xlim=(0, 1), ylim=(0, 1))

    ax[1].scatter(R, B, color=colors, marker='.')
    ax[1].set(xlabel='Red', ylabel='Blue', xlim=(0, 1), ylim=(0, 1))

    fig.suptitle(title, size=20);

plot_pixels(data, title="Input color space: 16 million possible colors")
plt.show()

import warnings; warnings.simplefilter('ignore')

from sklearn.cluster import MiniBatchKMeans
kmeans = MiniBatchKMeans(16)
kmeans.fit(data)

new_colors = kmeans.cluster_centers_[kmeans.predict(data)]

plot_pixels(data, colors=new_colors, title='Reduced color space: 16 colors')

plt.show()
china_recolored = new_colors.reshape(china.shape)

fig, ax = plt.subplots(1, 2, figsize=(16, 6), subplot_kw=dict(xticks=[], yticks=[]))

fig.subplots_adjust(wspace=0.05)
ax[0].imshow(china)
ax[0].set_title('Original Image', size=16)
ax[1].imshow(china_recolored)
ax[1].set_title('16-color Image', size=16)
plt.show()























