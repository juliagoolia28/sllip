# Structural Analysis of SLLIP MRI Data
## This section overviews how to analyze sMRI data using Qoala-T and Freesurfer. 
This information was created from: https://github.com/Qlab-UDel/qlab/wiki/FreeSurfer-Overview

Always remember to work in the sllip environment:
```
sllip_env
```
### Edits will generally be conducted in the following order:
Quality Control > Manual Inspection of Data > Skullstrip > Reconstruction > Control Point Edits > Reconstruction > White Matter Edits > Reconstruction

### But first, you need to extract your sMRI values using the following steps, if you haven't already:
## **Extracting gray matter measures**
This tutorial will show you how to extract your gray matter volume (GMV) and cortical thickness (CT) measures from your freesurfer reconstructed data.  This step comes after the final reconstruction step (using the recon-all -autorecon-all command). Therefore, in this tutorial whenever I refer to reconstructed data, I am referring to the output files that Freesurfer creates and fills in during the recon-all process.

### **Overview**
Freesurfer provides a very simple and organized method for extracting gray matter measures after reconstruction.  The output is a text file which you can open in Excel (make sure you specify that it is tab delimited in excel to open the file).  These outputs will include each subject’s CT or GMV (based on which scripts below you run) for each region in the desikan killiany atlas. These outputs are particularly useful when you want to run region of interest (ROI) based analyses.

## **To Start**
### **Set up your subject's directory**
Setting up your subject's directory informs Freesurfer where you want your created files to go.  Make sure you go to the directory (main folder) where you want where you want the output files to go. Then, you should designate where all the participant’s reconstructed data are (so you should see all your subjects' folders here, make sure you do not go into just one subject's folder). 
````
cd /home/qigroup/Documents/projects/sllip/dicom_conversion/derivatives/freesurfer/smri_outputs/smri_extractions
export SUBJECTS_DIR=/home/qigroup/Documents/projects/sllip/dicom_conversion/derivatives/freesurfer
````
To double check that you have set the correct subject’s directory you can run the command:
````
echo $SUBJECTS_DIR
````
You should then see the path you set: /home/qigroup/Documents/projects/sllip/dicom_conversion/derivatives/freesurfer/smri_outputs/smri_extractions

### **Extracting cortical surface data**
For CT or GMV measures along the parcellated surface (gyri and sulci of cerebral cortex), you can run the following commands, where you need to include each Freesurfer’s subject IDs, with 1 space between each subject. Each command only gets data from one hemisphere (right hemisphere: rh or left hemisphere: lh) and one measure (thickness or volume) at a time.
#### **Extracting cortical thickness data**
Here are the commands you would run for extracting the cortical thickness for the right hemisphere and left hemisphere:
````
aparcstats2table --subjects <subject_1_ID>  <subject_2_ID>  --hemi rh --meas thickness --tablefile <filename>.txt
aparcstats2table --subjects <subject_1_ID>  <subject_2_ID>  --hemi lh --meas thickness --tablefile <filename>.txt
````
An example of this command in the right hemisphere with 14 subjects:
```
aparcstats2table --subjects sub-sllip001 sub-sllip002 sub-sllip004 sub-sllip005 sub-sllip006 sub-sllip007 sub-sllip008 sub-sllip009 sub-sllip010 sub-sllip011 sub-sllip012 sub-sllip013 sub-sllip014 sub-sllip015  --hemi rh --meas thickness --tablefile aparc_rh_n14_040120.txt
```
#### **Extracting gray matter volume data**
Here are the commands you would run for extracting the gray matter volume for the right hemisphere and left hemisphere:
````
aparcstats2table --subjects <subject_1_ID>  <subject_2_ID>  --hemi rh --meas volume --tablefile <filename>.txt
aparcstats2table --subjects <subject_1_ID>  <subject_2_ID>  --hemi lh --meas volume --tablefile <filename>.txt
````
### **Extracting subcortical and total intracranial volume data**
For GMV of subcortical structures, and to get estimated intracranial volume (eTIV), you only need to run one script since it includes both right and left hemisphere data.  The estimated intracranial volume is the estimated total volume for each person's brain.  You should always include particiants' eTIV measure as a control variable so that you control for the fact that people with bigger brains may have larger volumes or thicker cortices in regions of interest as compared to people with smaller brains.  
Here is the command for extracting the gray matter volume in subcortical regions across both hemispheres as well as the eTIV:
````
asegstats2table --subjects  <subject_1_ID>  <subject_2_ID> --meas volume --tablefile <filename>.txt
````

