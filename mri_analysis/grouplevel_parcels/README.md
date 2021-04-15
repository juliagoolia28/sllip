## Group Level Parcellation Analysis
This analysis, and much of the code, is adapted from [Terri Scott](https://github.com/tlscott/make_parcels). Please cite the following before using:

Scott, T.L. and Perrachione, T.K. (2019). Common cortical architectures for phonological working memory identified in individual brains. NeuroImage, 202, 116096. DOI: 10.1016/j.neuroimage.2019.116096.
https://pubmed.ncbi.nlm.nih.gov/31415882/

In addition to extracting the magnitude of response within the top 10% of voxels within a parcel, we may choose to extract the magnitude of response from each contrast within each parcel. Here are the steps to conduct that analysis:
- Extract each parcel mask, using fslmaths from the parcels_sig.nii.gz file within the parcels folder
```
