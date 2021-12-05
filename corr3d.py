import imageio
import numpy as np
import matplotlib.pyplot as plt
from acf import corr3d as corr

rdir = "/media/maxc/IcyBox/Cooper2021_Data/"
sname = "PZ103"
recondir = f"{rdir}{sname}_Initial/"

# Load image to check. Img should just be thin section, with rest
# masked off as zeros.
iname = f"{recondir}{sname}_Initial_SmallCrop.tif"
img = imageio.volread(iname).astype(np.float32) # Type should have number of bits higher than original data type, e.g. 16bit uint -> 32bit float
print(f"Loaded img: {iname}")

ofile=f"{rdir}/{sname}_correlation_data/c_e01.dat"
efile=f"{rdir}/{sname}_correlation_data/e01.dat"

mask = img>0 # Mask of indices where core is located
g_bar = np.mean(img[mask]) # mean grayscale value in thin section
img[mask] -= g_bar
norm_f = np.mean(img[mask]**2) # second moment for corr.


e = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,\
                16,17,18,19,20,21,22,23,24,25,26,27,28,\
                29,30,31,32,33,34,35,36,37,38,39,40,41,\
                42,43,44,45,46,47,48,49,50])
e = e.append([51,52,53,54,55,56,57,58,59,60,61,62,63,\
                64,65,66,67,68,69,70,71,72,73,74,75,76,77,\
                78,79,80,81,82,83,84,85,86,87,88,89,90,91,\
                92,93,94,95,96,97,98,99,100])
e = e.append([110,120,130,140,150,175,200,250,\
                300,350,400,450,500,550,600,650])

n_e = e.size
ei = np.arange(n_e)
c_e = np.zeros(n_e) # Correlations

for i in ei:
    g_r_e = corr(img, e[i])
    c_e[i] = np.mean(img[mask]*g_r_e[mask])/norm_f # Autocorrelation
    print(c_e[i])
    e.tofile(efile, ",")
    c_e.tofile(ofile, ",")
