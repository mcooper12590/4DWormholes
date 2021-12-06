import imageio
import numpy as np
import matplotlib.pyplot as plt
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','--ifile')
parser.add_argument('-m','--mfile')
parser.add_argument('-o','--ofile')
parser.add_argument('-r','--resfile')

args = parser.parse_args()

rdir = "/media/maxc/IcyBox/Cooper2021_Data/"
sname = "PIN43"
recondir = f"{rdir}{sname}/Tomography/Initial/"

if args.ifile:
    ifile = args.ifile
else:
    ifile = f"{recondir}{sname}_Initial.tif"

if args.mfile:
    mfile = args.mfile
else:
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

if args.ofile:
    ofile = args.ofile
else:
    ofile =  f"{recondir}{sname}_Corrected.tif"
    
imageio.volwrite(ofile, img_c)
