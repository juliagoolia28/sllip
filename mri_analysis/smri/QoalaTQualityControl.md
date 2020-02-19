# Using Qoala-T to help with quality control of Freesurfer reconstructed files
Written by Jen Legault (https://github.com/Qlab-UDel/qlab/wiki/Qoala-T-Quality-Control)

After Freesurfer reconstruction, we should always make sure the files were properly reconstructed, especially for child populations.  This is because children tend to move a lot and
their brains are more difficult to model due to high developmental variations between children.  
Therefore, we will use Qoala-T to help us decide which subject files to include, exclude, and/or fix.

## What is Qoala-T?
Qoala-T is a supervised-learning tool to assess accuracy of manual quality control of automatic segmented MRI data

## How to use Qoala-T

### Step 1: Extract gray matter measures

Qoala-T compares the gray matter measures for our data to see how well it fits with their gray matter model data from 784 scans of subjects aged 8 - 25 years old. 

#### Open a shell
Make sure you are logged into the sylvian computer system.
To remote in:

```ssh –XY qigroup@sylvian.ling.udel.edu```

#### Designate the subject's directory

Navigate to the folder where your Freesurfer reconstructed files are, designate this as the subject's directory, and create a folder where you want the output to go.

```cd /home/qigroup/Documents/<path_to_Freesurfer_reconstructed_files>```

```export SUBJECTS_DIR=/home/qigroup/Documents/<path_to_Freesurfer_reconstructed_files>```

```mkdir <your_folder_name>```

#### Designate which subjects you will be extracting gray matter measures from

Set a list with all the subjects you will be including for the gray matter extraction

```list="`ls -d <beginning_name_of_files_you_want_to_include>*/`"```

For example, if I wanted to include all the participants in the main Freesurfer reconstructed files location, then I would type ``` list="`ls -d sub*/`" ```, since all our subject ID's start with the prefix "sub". If I only wanted to run adult participants in a project titled "example", where adults were marked as "_a" and children were marked as "_c" then I would type ``` list="`ls -d sub-example_a*/`" ```.

#### Extract gray matter measures
Here, you will be running a series of commands that will extract gray matter volume (asegstats2table command), cortical thickness (aparcstats2table commands for each hemisphere), and surface area (also aparcstats2table commands for each hemisphere) measures for each participant in your list.

```asegstats2table --subjects $list --meas volume --skip --tablefile /home/qigroup/Documents/<path_to_Freesurfer_reconstructed_files>/<your_folder_name>/aseg_stats.txt```

```aparcstats2table --subjects $list --hemi lh --meas thickness --skip --tablefile /home/qigroup/Documents/<path_to_Freesurfer_reconstructed_files>/<your_folder_name>/aparc_thickness_lh.txt```

```aparcstats2table --subjects $list --hemi rh --meas thickness --skip --tablefile /home/qigroup/Documents/<path_to_Freesurfer_reconstructed_files>/<your_folder_name>/aparc_thickness_rh.txt```

```aparcstats2table --subjects $list --hemi lh --meas area --skip --tablefile /home/qigroup/Documents/<path_to_Freesurfer_reconstructed_files>/<your_folder_name>/aparc_area_lh.txt```

```aparcstats2table --subjects $list --hemi rh --meas area --skip --tablefile /home/qigroup/Documents/<path_to_Freesurfer_reconstructed_files>/<your_folder_name>/aparc_area_rh.txt```

#### Double check your work

Navigate to your designated output folder and check to see if all 5 text files were created.

```cd /home/qigroup/Documents//<path_to_Freesurfer_reconstructed_files>/<your_folder_name>/```

```ls```

You should see the following files: aseg_stats.txt, aparc_thickness_lh.txt, aparc_thickness_rh.txt, aparc_area_lh.txt, and aparc_area_rh.txt.

### Step 2:Input gray matter measures onto online Qoala-T app

Go to the online [Qoala-T app](https://qoala-t.shinyapps.io/qoala-t_app/) and insert the extracted text files in respective locations.

![](https://github.com/jlegault/Materials_for_Inspection_of_sMRI_data/blob/master/Images_for_wiki_page/qoala_t_app_inserts.png)

Then look at the graphical output, save this image, and download the .csv file.

**Next Step:** [[Manual Inspection of Data]]

**Previous Step:** [[Freesurfer Overview]]
