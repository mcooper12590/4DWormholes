import imageio
from numpy import array
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','--ifile')
parser.add_argument('-m','--mfile')
parser.add_argument('-o','--ofile')
parser.add_argument('-r','--resfile')

args = parser.parse_args()

rdir = "/media/maxc/IcyBox/Cooper2021_Data/"
sname = "PZ101"

thins = f"{rdir}{sname}/ThinSections/"

tsnum = "10"
tsdir = f"{thins}{tsnum}/"

if args.mfile:
    mfile = args.mfile
else:
    mfile = f"{tsdir}{sname}ts_{tsnum}mm_Mask.tif"

mask = (imageio.volread(mfile)-2).astype(bool)

if args.ifile:
    ifile = args.ifile
else:
    ifile = f"{tsdir}{sname}ts_{tsnum}mm_8bit.tif"

img = imageio.imread(ifile)
res = mask*img

if args.ofile:
    ofile = args.ofile
else:
    ofile = f"{tsdir}{sname}ts_{tsnum}mm_Masked.tif"

imsave(ofile, res)
