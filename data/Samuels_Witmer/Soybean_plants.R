setwd("~/Dropbox/Documents/Birkbeck/Modules/Current Modules/Research Methods and Data Analysis/2014-15/data/Samuels_Witmer")
soybean <- read.csv("Soybean_plants.csv",header = T,sep=',')
soybean
str(soybean)
names(soybean) <- "l"
soybean
m <- mean(soybean$l)
s <- sd(soybean$l)
se <- s / sqrt(length(soybean$l))
m
s
se

