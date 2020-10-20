## Control Point Edits
Written by Jen Leagult and Nicola Bautista: https://github.com/Qlab-UDel/qlab/wiki/Control-Point-Edits

Now go to FreeView (type 'freeview' in terminal) and you can start making control point edits:
On the left, you will see 3 tabs (Volumes, Surfaces, Point Sets).

**Loading the Necessary Files**

1. Volumes
    - Click on **"Load Volume"** under the "Volumes" tab and go to the folder that contains the MRI volumes (usually called `mri`). Load `orig.mgz` and `wm.mgz` onto FreeView.
    - For `wm.mgz` change the Color map from "Grayscale" to "Heat". *Make sure that the `wm` volume is above the `orig` volume.*
    - Play with the opacity of the `wm` volume until you see white/gray matter contrast. 

2. Surfaces
    - Now go under the "Surfaces" tab and click on the icon with the green '+' (Load Surfaces). This time, go to the folder that contains the surfaces (it's usually called `surf`). Load `lh.white` and `rh.white`.

3. Point Sets  
*This is essential to adding control points.*
    - If this is your first time adding control points to this brain, click on **"New Point Set"** to create a new control point set. Name the new point set `control.dat`, make sure you select "control points" instead of "way points", assign template volume to `wm`, then click "OK".   

    - If you have previously made a point set for this brain before, click on **"LoadPoint Set"** to load `control.dat` from the `tmp` folder (this should be in the subject folder). Again make sure you select "control points" instead of "way points".

**Adding Control Points**

Click on **"Point Set Edit"** to change your cursor to a point set editor. Now you can add control points to the `wm` volume. Control points are used to include white matter that is not inside the surface - if there's a large area, just put a lot of control points there. Don't try to use control points to get rid of gray matter inside the surface boundary, that's what white matter editing is for.

**Applying Control Point Edits**

In the python software, click **"Recon Control Points"** . This will take ~10 hours, leave it on the queue overnight.
*Always set control points before adjusting White Matter Edits.*
 
**Helpful Shortcuts**

- **PageUp** and **PageDown** are used to go up and down the brain. 
- **Ctrl+Z** works the way you think it does! It's the undo button. 
- Click on a control point while pressing **Shift** to delete an individual point.   
You may find it helpful to toggle (check/uncheck volumes and surfaces) in order to see exactly where the white matter/gray matter boundary is. 

- **Ctrl+V** allows volume toggling
- **Ctrl+F** allows surface toggling
- **Ctrl+C** allows toggling between the two surfaces (make sure you are under surfaces tab to use this one)
- See [the official FreeView wiki](https://surfer.nmr.mgh.harvard.edu/fswiki/FreeviewGuide/FreeviewReference/FreeviewMouseCommands) for more shortcuts

**Next Step:** White Matter Edits
