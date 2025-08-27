# Data Analysis Modules for Robotic Rehabilitation
Repository "Data Analysis Modules for Robotic Rehabilitation" contains programming scripts for .... . Details of the developed low-cost robotic rehabilitation system are presented in the preprint titled "[Robotic Trail Maker Platform for Rehabilitation in Neurological Conditions: Clinical Use Cases](https://arxiv.org/pdf/2504.19230)" and authored by Srikar Annamraju, [Harris Nisar](https://github.com/nisar2), [Dayu Xia](https://github.com/dyxia1241), Shankar A. Deka, Anne Horowitz, [Nadica Miljković](https://github.com/NadicaSm/), and Dušan M. Stipanović.

## GitHub Repository Contents
The repository contains the following files:

1) [README.me](https://github.com/nisar2/robotic-rehab-data-analysis/blob/main/README.md) - a file containing basic information about the GitHub repository "[https://github.com/nisar2/robotic-rehab-data-analysis/](https://github.com/nisar2/robotic-rehab-data-analysis/)"
2) [train_wo](https://github.com/nisar2/robotic-rehab-data-analysis/tree/main/train_wo) - a file containing data used for training the proposed model. The naming convention of the csv files within is : {shape} + {healthy or not} + {number} + {assisted or not}. Where {shape} = {b --> B, cir --> circle, tri --> triangle}, {healthy or not} = {h --> healthy, p --> not healthy}, {number} = {the assigned number upon data collection}, {assisted or not} = {w --> assisted, wo --> not assisted}.
3) [test_wo](https://github.com/nisar2/robotic-rehab-data-analysis/tree/main/test_wo) - a file containing data used for testing the proposed model. The naming convention of the csv files within is : {shape} + {healthy or not} + {number} + {assisted or not}. Where {shape} = {hex --> hexagon, inf --> infinity}, {healthy or not} = {h --> healthy, p --> not healthy}, {number} = {the assigned number upon data collection}, {assisted or not} = {w --> assisted, wo --> not assisted}.
4) [patients_data](https://github.com/nisar2/robotic-rehab-data-analysis/blob/main/patients_data.csv) - a .csv file comprising assessment data for patients and healthy subjects. The explanation of all columns is given below.
5) [patients_stats](https://github.com/nisar2/robotic-rehab-data-analysis/blob/main/patients_stats.R) - is an R programming script with reproducible statistical analysis of data presented in patinets_data.csv file. Also, file patients_stats contains information on R version and results of statistical tests.

The file [patients_data.csv](https://github.com/nisar2/robotic-rehab-data-analysis/blob/main/patients_data.csv) contains the following 13 columns:
1) **S.No.** - session ID (numerical value - integer)
2) **SUBJECT** - subject's ID (for example: "Healthy 1" and "Patient 3")
3) **DIAGNOSIS** - information whether the subject is healthy or not (two possible values: "Healthy" and "Patients")
4) **ID** - subject's ID, similar as column **SUBJECT**, but contains only numerical value (for "Healthy 1" in column **SUBJECT**, **ID** column contains only 1)
5) **SHAPE** - can be "B", "Circle", "Hexagon", "Infinity", and "Triangle" and it is shape recreated by a subject with robotic trial maker (please, see manuscript for more details)
6) **ASSISTANCE** - this is a Boolean variable (indicates whether there was or there was not assistance during trial maker) - for Healthy subjects, the only possible value is that there was no assistance, while for patients trials were performed both with and without assistance
7) **AVERAGE.DEVIATION..mm.** - average deviation of a drawn shape in comparison to the ideal shape expressed in mm (please, see manuscript for more details)
8) **TOTAL.DURATION** - total duration of a specific trial and specific shape in s
9) **No..OF.LOOPS** -
10) **TIME.FOR.10.LOOPS** -
11) **Group** - the combination of **ASSISTANCE** and **DIAGNOSIS** column for each subject (possible values are "Healthy Unassisted", "Patient Unassisted", and "Patient Assisted")
12) **Total.Distance.Traveled..mm.** - 
13) **Speed..mm.s.** - speed in mm/s for performing a trial (please, see manuscript for more details)

### License
Unless otherwise stated, shared programming scripts are licensed under free software licence ...

### Disclaimer
The programming scripts are provided without any guarantee, we used them for research purposes - they are not intended for medical purposes.

### Citing Instructions
In case you find this code useful, please cite the following references:
1) Annamraju, S., Nisar, H., Xia, D., Deka, S. A., Horowitz, A., Miljković, N., & Stipanović, D. M. (2025). Robotic Trail Maker Platform for Rehabilitation in Neurological Conditions: Clinical Use Cases. arXiv preprint, DOI: [https://doi.org/10.48550/arXiv.2504.19230](https://doi.org/10.48550/arXiv.2504.19230).
2) Annamraju, S., Nisar, H., Xia, D., Deka, S. A., Horowitz, A., Miljković, N., & Stipanović, D. M. (2025). Data Analysis Modules for Robotic Rehabilitation, https://github.com/nisar2/robotic-rehab-data-analysis, Accessed on August 5, 2025, DOI: [https://doi.org/10.5281/zenodo.16967594](https://doi.org/10.5281/zenodo.16967594).
