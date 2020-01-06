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

## Converting dicoms to BIDS formatter nifti
-  On terminal complete the following steps:
```
cd /home/nas/projects/sllip/
docker run --rm -it --entrypoint=bash -v $(pwd):/data nipy/heudiconv:latest
cd /data/
```
-  You should now be within the container and can run the conversion. **SUBJECTID in all caps should be edited:**
```
rm -r -f /data/niftis/*
heudiconv -d /data/mri/dicoms/{subject}/*/*/*.IMA -s SUBJECTID -f /data/mri/sllip_heuristics.py -c dcm2niix -b -o /data/mri/bids
```


