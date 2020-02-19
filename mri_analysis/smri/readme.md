## This section overviews how to analyze sMRI data using Qoala-T and Freesurfer. 
This information was created from: https://github.com/Qlab-UDel/qlab/wiki/FreeSurfer-Overview

Always remember to work in the sllip environment:
```
sllip_env
```

Run command:
```
python /home/qigroup/Documents/projects/blast/data/mri/imaging/scripts/edit_freesurfer_surface.py
```
When the software loads, ensure Project Surface Directory reads:\
/home/qigroup/Documents/projects/sllip/dicom_conversion/derivatives/freesurfer/

Enter the subject ID: sub-sllip###

### These edits are listed in the general order in which they should be done:
Quality Control > Manual Inspection of Data > Skullstrip > Reconstruction > Control Point Edits > Reconstruction > White Matter Edits > Reconstruction
