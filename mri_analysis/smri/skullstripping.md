##Skullstripping
Written by Jen Legault and Nicola Bautista (https://github.com/Qlab-UDel/qlab/wiki/Skullstripping)

*Adjusting watershed parameters for ideal brainmask volume*

It's super simple and fast!

**Adjust the watershed parameter.** Before you do anything, make sure to backup the old brainmask. To do this, go into the `mri` directory of the brain you're working on and then copy the `brainmask.mgz` file to a backup file called `brainmask_orig.mgz`. From now on, we only make edits to `brainmask.mgz`. 

## Skullstripping

1. Open FreeView by clicking “view subject”, then open the Volume files brainmask.mgz and orig.mgz from the mri folder, and make sure you put brainmask above orig. Change the colormap of brainmask to heat and lower the opacity a little bit so you can see it overlaid on orig (I personally find that an opacity of ~0.11 works well). 

2. Skullstripping is based on the watershed parameter, which helps FreeSurfer make the brainmask. The default value is 25. If the red area of the brainmask volume includes some of the skull, lower the watershed parameter. If the brainmask is too small and doesn't include some of the brain matter, you'll want to increase the watershed parameter. 

3. Exit FreeView and the GUI. In the terminal, run the command:
```bash
recon-all -skullstrip  -clean-bm -gcut -subjid [subject id]
```
This command usually takes less than 2 minutes to run. Then you can reopen the brain volumes in FreeView by clicking “View gcuts effect” and repeat the process until the brainmask is as good as possible. A good technique is to start by steadily lowering the watershed parameter by ~2 until it starts cutting into the brain, and then bump it back up so it includes the entire brain.

**Next step:** Control Point Edits
