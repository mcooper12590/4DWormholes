import imageio
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import glob

imgloc = sorted(glob.glob("SlicesY/*.tif"))

img = io.concatenate_images(io.ImageCollection(imgloc))
mask = imageio.volread("HolderMask.tif").astype(bool)

algray = np.mean(mask*img, axis=(1,2))

plt.plot(algray)
plt.show()
almedian = np.median(algray)
# alsub = algray - almedian
# mask = (img.T.astype(int32)-alsub)>0
# img_c = subtract(img.T, alsub, where=mask)
cf = almedian/algray
img_c = (img.T*cf).astype(np.uint16)
img_c = img_c.T
plt.plot(np.mean(img_c[:,:40,:40], axis=(1,2)))
plt.show()
imageio.mimwrite("whole_PIN43_CorrectedMult.tif", img_c)
