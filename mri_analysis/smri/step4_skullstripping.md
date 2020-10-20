## Skullstripping
Written by Jen Legault and Nicola Bautista (https://github.com/Qlab-UDel/qlab/wiki/Skullstripping)

*Adjusting watershed parameters for ideal brainmask volume*

It's super simple and fast!

## FIRST STEP
Before you do anything, make sure to backup the old brainmask. To do this, you will copy the `brainmask.mgz` in `mri` directory to a backup file called `brainmask_orig.mgz`. 

Example (must edit sub-sllipID to subject #):

```cp /Users/qigroup/mnt/sylvian/sllip/dicom_conversion/derivatives/freesurfer/sub-sllipID/mri/brainmask.mgz /Users/qigroup/mnt/sylvian/sllip/dicom_conversion/derivatives/freesurfer/sub-sllipID/mri/orig_brainmask.mgz```

From now on, we only make edits to `brainmask.mgz`. 

## Next Steps
1. Open FreeView

*If using Mac Mini 1*
1. First open the python script on the Mac Mini 1 computer with the mnt connected (if it is not connected, notify a lead researcher)

```python /Users/qigroup/mnt/sylvian/blast/data/mri/imaging/scripts/edit_freesurfer_surface_JMS.py```

2. Designate the directory to where you have the Freesurfer reconstructed data

```/Users/qigroup/mnt/sylvian/sllip/dicom_conversion/derivatives/freesurfer```

*If using Sylvian*
1. First open the python script on the Sylvian computer using Teamview (if Teamview is not working, notify a lead researcher)

```python /home/qigroup/Documents/projects/blast/data/mri/imaging/scripts/edit_freesurfer_surface.py```

2. Designate the directory to where you have the Freesurfer reconstructed data

```/home/qigroup/Documents/projects/sllip/dicom_conversion/derivatives/freesurfer/```

*On either computer*
3. Select the subject, check that the surface was found, and hit OK.
4. Click on the Editing Brain Actions tab
5. Click on the View subject button (wait for a minute until everything loads)
6. Open the Volume files (File>Load Volume) brainmask.mgz and orig.mgz from the mri folder, and make sure you put brainmask above orig (using the blue arrows)
7. Change the colormap of brainmask to heat and lower the opacity a little bit so you can see it overlaid on orig (I personally find that an opacity of ~0.11 works well). 
8. Skullstripping is based on the watershed parameter, which helps FreeSurfer make the brainmask. The default value is 25. If the red area of the brainmask volume includes some of the skull, you will want to lower the watershed parameter. 
  - Exit FreeView and the GUI. 
  - In the terminal, run the command:
```
recon-all -skullstrip  -clean-bm -gcut -subjid [subject id]
```
If the brainmask is too small and doesn't include some of the brain matter, you'll want to increase the watershed parameter. Here is how you will do that:
  - Exit FreeView and the GUI. 
  - In the terminal, run the command (where h is the new watershed value):
```
recon-all -skullstrip -wsthresh <h> -clean-bm -subjid <subject name>
```

Reopen the brain volumes in FreeView by clicking “View gcuts effect” and repeat the process until the brainmask is as good as possible. A good technique is to start by steadily lowering the watershed parameter by ~2 until it starts cutting into the brain, and then bump it back up so it includes the entire brain.

**Next step:** Control Point Edits
