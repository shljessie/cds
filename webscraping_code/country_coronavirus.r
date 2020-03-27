<<<<<<< HEAD:cleaningdata.R
corona <- read.csv('~/Downloads/novel-corona-virus-2019-dataset/covid_19_data.csv', stringsAsFactors = F)
corona$Province.State = NULL
corona$Last.Update = NULL
corona$SNo = NULL
aggeddata <- aggregate(corona[3:5], by = corona[1:2], sum)

#write.csv(aggeddata, '~/Desktop/CDS Onboarding/coronaclean.csv', quote = F, row.names = F)
=======
corona <- read.csv('~/Downloads/novel-corona-virus-2019-dataset/covid_19_data.csv', stringsAsFactors = F)
corona$Province.State = NULL
corona$Last.Update = NULL
corona$SNo = NULL
aggeddata <- aggregate(corona[3:5], by = corona[1:2], sum)

write.csv(aggeddata, '~/Desktop/CDS Onboarding/coronaclean.csv', quote = F, row.names = F)
>>>>>>> 65cedbbc545640de9fcbcb7935840acccb900a3a:webscraping_code/country_coronavirus.r
