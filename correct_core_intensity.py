import imageio
import numpy as np
import matplotlib.pyplot as plt
import glob

rdir = "/media/maxc/IcyBox/Cooper2021_Data/"
sname = "PZ101"
recondir = f"{rdir}{sname}/Tomography/Initial/"

ifile = f"{recondir}{sname}_Initial.tif"
mfile = f"{recondir}{sname}_HolderMask.tif"

img = imageio.volread(ifile)
mask = imageio.volread(mfile).astype(bool)

algray = np.mean(mask*img, axis=(1,2))

plt.plot(algray)
plt.show()
almedian = np.median(algray)
cf = almedian/algray

img_c = (img.T*cf).astype(np.uint16)
img_c = img_c.T

plt.plot(np.mean(img_c[:,:40,:40], axis=(1,2)))
plt.show()

ofile = f"{recondir}{sname}_Corrected.tif"
imageio.volwrite(ofile, img_c)
