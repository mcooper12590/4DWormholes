# 4DWormholes
Code to analyse wormhole time evolution

## Requirements
Python packages:
SciPy,
NumPy,
imageio,
Matplotlib,
argparse,
pandas,
glob,
tqdm,
and Mayavi.

Cython is required for running correlations.

These packages and Cython are available in the base Anaconda3 install.

## Running scripts

### Masks and intensity correction
Masks can be applied running the applymask_2d.py and applymask_3d.py scripts. These have the options '-i', '-m', and '-o' for input file, mask file, and output file, respectively. Intensity correction uses correct_core_intensity.py with the same options.

### Average intensity
Average intensity per slice is calculated using avg_intensity.py. This has the options '-i' and '-r' for input file and results file, respectively.

### Correlations
To run correlations the acf package must be compiled by running setup.py in the acf/ directory. 2D correlations on thin sections are calculated in corr2d.py with options '-d', '-n', and '-s', for thin section root directory, sample number, and sample name, respectively.

3D correlations are calculated in corr3.py with options '-d', '-i' and '-s' for directory, input file, and sample name, respectively.

## Analysis notebooks
Notebooks 'PIN43_4D.ipynb' and 'PZ103_4D.ipynb' generate difference images, skeletons, and measure tip position from the 4D data sets. 'MainPlottingandAnalysis.ipynb' performs data analysis for the main text, while 'SupplementalPlotting.ipynb' performs data analysis for the supplemental. These are run in Jupyter Notebook.

## Generating results from Cooper et al.
The data and code available can reproduce the results from tomography and thin sections. 4D tomography data are available for PIN103 and PZ43 along with initial tomography. Initial tomography and thin section data are available for PZ101.
