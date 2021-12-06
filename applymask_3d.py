import imageio
from numpy import array
from tifffile import imsave
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

if args.mfile:
    mfile = args.mfile
else:
    mfile = f"{recondir}{sname}_AirMask.tif"
mask = ~(imageio.volread(mfile).astype(bool))
print(f"Loaded mask: {mfile}")

if args.ifile:
    ifile = args.ifile
else:
    ifile =  f"{recondir}{sname}_Initial_Cropped.tif"
img = imageio.volread(ifile)
print(f"Loaded img: {ifile}")
res = mask*img

if args.ofile:
    ofile = args.ofile
else:
    ofile = f"{recondir}{sname}_Initial_Masked.tif"
    
imsave(ofile, res, bigtiff=True)
