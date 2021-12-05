import imageio
from numpy import array
from tifffile import imsave

rdir = "/media/maxc/IcyBox/Cooper2021_Data/"
sname = "PZ101"
recondir = f"{rdir}{sname}/Tomography/"

mfile = f"{recondir}{sname}_AirMask.tif"
mask = ~(imageio.volread(mfile).astype(bool))
print(f"Loaded mask: {mfile}")

ifile = f"{recondir}{sname}_Initial_Cropped.tif"
img = imageio.volread(ifile)
print(f"Loaded img: {ifile}")
res = mask*img

ofile = f"{recondir}{sname}_Initial_Masked.tif"
imsave(ofile, res, bigtiff=True)
