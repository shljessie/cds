corona <- read.csv('~/Downloads/novel-corona-virus-2019-dataset (1)/covid_19_data.csv', stringsAsFactors = F)
corona$Province.State = NULL
corona$Last.Update = NULL
corona$SNo = NULL
aggeddata <- aggregate(corona[3:5], by = corona[1:2], sum)

write.csv(aggeddata, '~/GitHub/cds/Kassie/422coronaclean.csv', quote = F, row.names = F)
