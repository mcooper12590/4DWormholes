import imageio
from numpy import array

rdir = "/media/maxc/IcyBox/Cooper2021_Data/"
sname = "PZ101"

thins = f"{rdir}{sname}/ThinSections/"

tsnum = "10"
tsdir = f"{thins}{tsnum}/"

mfile = f"{tsdir}{sname}ts_{tsnum}mm_Mask.tif"
mask = (imageio.volread(mfile)-2).astype(bool)


ifile = f"{tsdir}{sname}ts_{tsnum}mm_8bit.tif"
img = imageio.imread(ifile)
res = mask*img

ofile = f"{tsdir}{sname}ts_{tsnum}mm_Masked.tif"
imsave(ofile, res)
