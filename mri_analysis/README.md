# SLLIP MRI Analysis Pipeline

## Organization of Data (and rsyncing)
-  DICOM files are located at home/nas/dcmstorage/ and need to be rsynced to home/qigroup/Documents/projects/sllip/dicom_conversion/dicoms/ 
```
rsync -chavzP --stats /home/nas/dcmstorage/ /home/qigroup/Documents/projects/sllip/dicom_conversion/dicoms
```
AND to home/nas/projects/sllip/data/mri/dicoms/
```
rsync -chavzP --stats /home/nas/dcmstorage/ /home/nas/projects/sllip/data/mri/dicoms
```
-  BIDS files are located at home/qigroup/Documents/projects/sllip/dicom_conversion/bids/ and will be rsynced LATER to home/nas/projects/sllip/data/mri/bids/
```
rsync -chavzP --stats /home/qigroup/Documents/projects/sllip/dicom_conversion/bids/ /home/nas/projects/sllip/data/mri/bids
```
-  Derivatives (fmriprep, fsl, freesurfer) are located at home/qigroup/Documents/projects/sllip/derivatives/ and will be rsynced LATER to home/nas/projects/sllip/data/mri/derivatives/
```
rsync -chavzP --stats /home/qigroup/Documents/projects/sllip/derivatives/ /home/nas/projects/sllip/data/mri/derivatives
```

## Converting dicoms to BIDS formatter nifti
-  On terminal complete the following steps:
```
cd /home/qigroup/Documents/projects/sllip/dicom_conversion/
docker run --rm -it --entrypoint=bash -v $(pwd):/data nipy/heudiconv:latest
cd /data/
```
-  You should now be within the container and can run the conversion. **SUBJECTID in all caps should be edited:**
```
heudiconv -d /dicoms/{subject}/*/*/*.IMA -s SUBJECTID -f /sllip_heuristics.py -c dcm2niix -b -o /bids
```
- Once the conversion is complete, back up the BIDS data to NAS:
```
rsync -chavzP --stats /home/qigroup/Documents/projects/sllip/dicom_conversion/bids/ /home/nas/projects/sllip/data/mri/bids
```
## Prepare data for Freesurfer edits
We next need to convert the anatomical data to be corrected within Freesurfer. **SUBJECTID in all caps should be edited:**
```
docker run -ti --rm -v /home/qigroup/Documents/projects/sllip/dicom_conversion/bids:/data:ro -v /home/qigroup/Documents/projects/sllip/dicom_conversion/derivatives:/out -v /home/qigroup/Documents/projects/sllip/license.txt:/opt/freesurfer/license.txt poldracklab/fmriprep:1.3.1 /data /out participant --participant_label SUBJECTID --anat-only
```


