# 4DWormholes
Code to analyse wormhole time evolution

## Requirements
Python packages:
SciPy,
NumPy,
imageio,
tifffile,
Matplotlib,
argparse,
pandas,
glob,
tqdm,
and Mayavi.

Cython is required for running correlations.

These packages and Cython are available in the base Anaconda3 install.

As tomography data are large, and in some cases the smaller 4D data are all loaded in RAM, at least 32GB of RAM is required to run some scripts.

## Running scripts

### Masks and intensity correction
Masks are applied by running the applymask_2d.py and applymask_3d.py scripts. These have the options '-i', '-m', and '-o' for input file, mask file, and output file, respectively. Intensity correction uses correct_core_intensity.py with the same options.

### Average intensity
Average intensity per slice is calculated using avg_intensity.py. This has the options '-i' and '-r' for input file and results file, respectively.

### Correlations
To run correlations the acf package must be compiled by running setup.py in the acf/ directory. 2D correlations on thin sections are calculated in corr2d.py with options '-d', '-n', and '-s', for thin section root directory, sample number, and sample name, respectively.

3D correlations are calculated in corr3.py with options '-d', '-i' and '-s' for data save directory, input file, and sample name, respectively.

## Analysis notebooks
Notebooks 'PIN43_4D.ipynb' and 'PZ103_4D.ipynb' generate difference images, skeletons, and measure tip position from the 4D data sets. 'MainPlottingandAnalysis.ipynb' performs data analysis for the main text, while 'SupplementalPlotting.ipynb' performs data analysis for the supplemental. These are run in Jupyter Notebook.

## Results from Cooper et al.
Data measured from tomography and thin sections (Acf, avg. intensity, tip position) is available in the WormholeGrowth/ directory, as well as pressure log data, numerical model data, and (U)SANS data. These data can be analysed in 'MainPlottingandAnalysis.ipynb' and 'SupplementalPlotting.ipynb'.

### Generating results from full data
Full tomography and thin section data are available upon request. When downloaded, PATH_TO_DOWNLOAD/ refers to the top directory containing sample subdirectories. To generate results the data is first reduced using masks. For PIN43 there is an additional intensity correction step prior to masking, and a separate mask script available in the PZ43 data directory.

Processing PZ103:
```
python applymask_3d.py -i PATH_TO_DOWNLOAD/PZ103/Initial/PZ103_Initial_Cropped.tif -m PATH_TO_DOWNLOAD/PZ103/Initial/PZ103_AirMask.tif -o PATH_TO_DOWNLOAD/PZ103/Initial/PZ103_Initial_Masked.tif
python avg_intensity.py -i PATH_TO_DOWNLOAD/PZ103/Initial/PZ103_Initial_Masked.tif -r PZ103_pss_avg.dat
python corr3d.py -i PATH_TO_DOWNLOAD/PZ103/Initial/PZ103_Initial_SmallCrop.tif -s PZ103 -d ./
```

Processing PIN43:
```
python correct_core_intensity.py -i PATH_TO_DOWNLOAD/PIN43/Initial/PIN43_Initial.tif -m PATH_TO_DOWNLOAD/PIN43/Initial/PIN43_HolderMask.tif -o PATH_TO_DOWNLOAD/PIN43/Initial/PIN43_Initial_Corrected.tif
python PATH_TO_DOWNLOAD/PIN43/Initial/applymask.py
python avg_intensity.py -i PATH_TO_DOWNLOAD/PIN43/Initial/PIN43_Initial_Masked.tif -r PIN43_pss_avg.dat
python corr3d.py -i PATH_TO_DOWNLOAD/PIN43/Initial/PIN43_Corrected_Cropped.tif -s PIN43 -d ./
```

Processing PZ101 tomography:
```
python applymask_3d.py -i PATH_TO_DOWNLOAD/PZ101/Tomography/PZ101_Initial_Cropped.tif -m PATH_TO_DOWNLOAD/PZ101/Tomography/PZ101_AirMask.tif -o PATH_TO_DOWNLOAD/PZ101/Tomography/PZ101_Initial_Masked.tif
python avg_intensity.py -i PATH_TO_DOWNLOAD/PZ101/Tomography/PZ101_Initial_Masked.tif -r PZ101_pss_avg.dat
```

Processing PZ101 thin sections (for each thin section):
```
python applymask_3d.py -i PATH_TO_DOWNLOAD/PZ101/ThinSections/NUM/PZ101ts_NUMmm_8bit.tif -m PATH_TO_DOWNLOAD/PZ101/ThinSections/NUM/PZ101ts_NUMmm_Mask.tif -o PPATH_TO_DOWNLOAD/PZ101/ThinSections/NUM/PZ101ts_NUMmm_Masked.tif
python corr2d.py -s PZ101 -d PATH_TO_DOWNLOAD/PZ101/ThinSections/ -n NUM
```
