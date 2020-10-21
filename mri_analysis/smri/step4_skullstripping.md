## Skullstripping
Written by Jen Legault and Nicola Bautista (https://github.com/Qlab-UDel/qlab/wiki/Skullstripping)

*Adjusting watershed parameters for ideal brainmask volume*

It's super simple and fast!

## FIRST STEP
Before you do anything, make sure to backup the old brainmask. To do this, you will copy the `brainmask.mgz` in `mri` directory to a backup file called `brainmask_orig.mgz`. 

Example on Mac Mini 1 (must edit sub-sllipID to subject #):

```cp /Users/qigroup/mnt/sylvian/sllip/dicom_conversion/derivatives/freesurfer/sub-sllipID/mri/brainmask.mgz /Users/qigroup/mnt/sylvian/sllip/dicom_conversion/derivatives/freesurfer/sub-sllipID/mri/orig_brainmask.mgz```

From now on, we only make edits to `brainmask.mgz`. 

Also, be sure your SUBJECT DIRS are correctly setup:
On Mac Mini 1:

```
export SUBJECTS_DIR=/Users/qigroup/mnt/sylvian/sllip/dicom_conversion/derivatives/freesurfer
```

On Sylvian:

```
export SUBJECTS_DIR=/home/qigroup/Documents/projects/sllip/dicom_conversion/derivatives/freesurfer
```

To double check that you have set the correct subject’s directory you can run the command:

```
echo $SUBJECTS_DIR
```

## Next Steps
1. Open FreeView (type 'freeview' in terminal)

2. Open the following Volume files (File>Load Volume): brainmask.mgz and orig.mgz from the subject's mri folder, and make sure you put brainmask above orig (using the blue arrows)

3. Change the colormap of brainmask to heat and lower the opacity a little bit so you can see it overlaid on orig (I personally find that an opacity of ~0.11 works well). 

4. Skullstripping is based on the watershed parameter, which helps FreeSurfer make the brainmask. The default value is 25. Run the following command to automatically adjust the watershed and compare how similar or different the brainmask is:
  - Exit FreeView and the GUI. 
  - In the terminal, run the command:
```
recon-all -skullstrip  -clean-bm -gcut -subjid [subject id]
```

5. Reopen the brain volumes in FreeView by loading the  brainmask.gcuts.mgz file. Does the brainmask now more accurately account for brain matter than before? Continue to repeat this process until the brainmask is as good as possible. 

**Next step:** Control Point Edits
