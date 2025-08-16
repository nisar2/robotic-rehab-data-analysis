# Code for reproducing statistical results presented in the manuscript titled 
# "Robotic Trail Maker Platform for Rehabilitation in Neurological Conditions: 
# Clinical Use Case"

# > R.version
# _                           
# platform       x86_64-pc-linux-gnu         
# arch           x86_64                      
# os             linux-gnu                   
# system         x86_64, linux-gnu           
# status                                     
# major          4                           
# minor          3.3                         
# year           2024                        
# month          02                          
# day            29                          
# svn rev        86002                       
# language       R                           
# version.string R version 4.3.3 (2024-02-29)
# nickname       Angel Food Cake

# set working directory (the same as code directory)
setwd(dirname(rstudioapi::getSourceEditorContext()$path))

# load libraries
library(FSA)
library(rstatix)
library(dplyr)

# reading data
dat <- read.csv("patients_data.csv")
View(dat)

# prepare data for further processing
dat$DIAGNOSIS <- as.factor(dat$DIAGNOSIS)
dat$ASSISTANCE[dat$ASSISTANCE == "FALSE (AAN)"] <- TRUE
dat$ASSISTANCE <- as.factor(dat$ASSISTANCE)
dat$Group <- as.factor(dat$Group)
dat <- dat %>% select(Group, AVERAGE.DEVIATION..mm., Speed..mm.s.)
dat$Group <- as.factor(dat$Group)

# 147 instances overall with 3 variables

############################ AVERAGE.DEVIATION..mm. ############################
# checking normality (datasets are not normal as all p-values are <0.05)
shapiro.test(dat$AVERAGE.DEVIATION..mm.[dat$Group == "Healthy Unassisted"])
shapiro.test(dat$AVERAGE.DEVIATION..mm.[dat$Group == "Patient Assisted"])
shapiro.test(dat$AVERAGE.DEVIATION..mm.[dat$Group == "Patient Unassisted"])

# Bartlett test to check the variance
bartlett.test(AVERAGE.DEVIATION..mm. ~ Group, data = dat)
# RESULT: p-value = 0.003783

# Kruskal Wallis
kruskal.test(AVERAGE.DEVIATION..mm. ~ Group, data = dat)
dunnTest(AVERAGE.DEVIATION..mm. ~ Group, data = dat, method="bonferroni")

# RESULTS
# Dunn (1964) Kruskal-Wallis multiple comparison
# p-values adjusted with the Bonferroni method.
# 
# Comparison         Z      P.unadj        P.adj
# 1   Healthy Unassisted - Patient Assisted -4.120860 3.774605e-05 1.132381e-04
# 2 Healthy Unassisted - Patient Unassisted -5.551418 2.833619e-08 8.500856e-08
# 3   Patient Assisted - Patient Unassisted -1.430558 1.525570e-01 4.576711e-01

################################# Speed..mm.s. #################################
# checking normality (datasets are not normal as two p-values are <0.05)
shapiro.test(dat$Speed..mm.s.[dat$Group == "Healthy Unassisted"])
shapiro.test(dat$Speed..mm.s.[dat$Group == "Patient Assisted"])
shapiro.test(dat$Speed..mm.s.[dat$Group == "Patient Unassisted"])

# Bartlett test to check the variance
bartlett.test(Speed..mm.s. ~ Group, data = dat)
# RESULT: p-value < 2.2e-16

# Kruskal Wallis
kruskal.test(Speed..mm.s. ~ Group, data = dat)
dunnTest(Speed..mm.s. ~ Group, data = dat, method="bonferroni")

# RESULTS
# Dunn (1964) Kruskal-Wallis multiple comparison
# p-values adjusted with the Bonferroni method.
# 
# Comparison         Z      P.unadj        P.adj
# 1   Healthy Unassisted - Patient Assisted -1.031994 3.020748e-01 9.062243e-01
# 2 Healthy Unassisted - Patient Unassisted  4.490955 7.090463e-06 2.127139e-05
# 3   Patient Assisted - Patient Unassisted  5.522949 3.333564e-08 1.000069e-07