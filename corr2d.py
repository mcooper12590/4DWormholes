import imageio
import numpy as np
import matplotlib.pyplot as plt
from acf import corr2d as corr

rdir = "/media/maxc/IcyBox/Cooper2021_Data/"
sname = "PZ101"
thins = f"{rdir}{sname}/ThinSections/"
tsnum = "10"
tsdir = f"{thins}{tsnum}/"

# Load image to check. Img should just be thin section, with rest
# masked off as zeros.
iname = f"{tsdir}{sname}ts_{tsnum}mm_Masked.tif"
img = imageio.imread(iname).astype(np.float32) # Type should have number of bits higher than original data type, e.g. 16bit uint -> 32bit float
print(f"Loaded img: {iname}")

ofile=f"{tsdir}/{tsnum}_correlation_data/c_e01.dat"
efile=f"{tsdir}/{tsnum}_correlation_data/e01.dat"

mask = img>0 # Mask of indices where core is located
g_bar = np.mean(img[mask]) # mean grayscale value in thin section
img[mask] -= g_bar
norm_f = np.mean(img[mask]**2) # second moment for corr.


e = np.array([0,1,2,3,4,5,6,7,8,9,10,20,30,\
                40,50,60,70,80,90,100,200,300,400,500,600,700,\
                800,900,1000,1500,2000,2500,3000])
n_e = e.size
ei = np.arange(n_e)
c_e = np.zeros(n_e) # Correlations

for i in ei:
    g_r_e = corr(img, e[i])
    c_e[i] = np.mean(img[mask]*g_r_e[mask])/norm_f # Autocorrelation
    print(c_e[i])
    e.tofile(efile, ",")
    c_e.tofile(ofile, ",")
