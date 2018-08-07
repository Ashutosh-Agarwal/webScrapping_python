#merging diff dataset in one folder

multmerge = function(mypath){
  filenames = list.files(path=mypath, full.names = TRUE)
  datalist = lapply(filenames, function(x) {read.csv(file = x, header = TRUE)})
  Reduce(function(x,y) {rbind(x,y)}, datalist)
}
mydata = multmerge("C:/Users/Ashutosh/Desktop/bharathlisting/")

write.csv(mydata,"C:/Users/Ashutosh/Desktop/bharathlisting/bharathlisting.csv",row.names = FALSE)
