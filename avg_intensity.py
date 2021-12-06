import imageio
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','--ifile')
parser.add_argument('-m','--mfile')
parser.add_argument('-o','--ofile')
parser.add_argument('-r','--resfile')

args = parser.parse_args()

rdir = "/media/maxc/IcyBox/Cooper2021_Data/"
sname = "PZ101"
recondir = f"{rdir}{sname}/Tomography/"

if args.ifile:
    ifile = args.ifile
else:
    ifile = f"{recondir}{sname}_Initial_Cropped.tif"

img = imageio.volread(ifile)
print(f"Loaded image: {img}")

pss = np.sum(np.sum(img, axis=1), axis=1).astype(np.float64)
nzp = np.sum(np.sum(img>0, axis=1), axis=1).astype(np.float64)

avg = np.divide(pss, nzp, out=np.zeros_like(pss), where=nzp>0)

if args.resfile:
    resfile = args.resfile
else:
    resfile =  f"{rdir}{sname}/{sname}_pss_avg.dat"

avg.tofile(resfile, ",")

plt.plot(avg, 'r.')
plt.show()
