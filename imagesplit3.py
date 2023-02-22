import numpy as np
from patchify import patchify
from PIL import Image
import os

for Bfiles in os.listdir('backgroundTemp/In'):
    image = Image.open("backgroundTemp/In/{}".format(Bfiles))
    name, fext = os.path.splitext(Bfiles)
    image = np.asarray(image)
    patches = patchify(image, (1280, 1280, 3), step=1235)
    print(patches.shape)  # (6, 10, 1, 512, 512, 3)

    for i in range(patches.shape[0]):
        for j in range(patches.shape[1]):
            patch = patches[i, j, 0]
            patch = Image.fromarray(patch)
            num = i * patches.shape[1] + j
            patch.save(f"backgroundTemp/Out/{name}_split{num}.png")