## web_analysis
This folder contains a script used to analyze all web-based tasks: QUILS and ASL.
It imports the data, merges it into one file, computes an average accuracy score per participant, and statistically compares accuraccy overall to chance.

## clean_data
This folder contains scripts used to organize behavioral data. 
- clean_qualtrics_for_redcap.Rmd was used to take demographic surveys completed by parents on Qualtrics, and organize the data so it may be impported into RedCap.
  - Once this script is run once, data can be uploaded to RedCap and will not need to be run again.

- clean_nih_data.Rmd was used to organize and score all web-based tasks completed on Gorilla.

*No data is provided in this folder as all information included personal demographic information about the participants*
