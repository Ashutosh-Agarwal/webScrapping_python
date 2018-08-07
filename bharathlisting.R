data = read.csv(file.choose())

attach(data)

summary(data)

plot(Category, main = "Frequency Plot For Categories~Number of Companies",xlab = "Categories")
table(Category)

unique(data$Category[data$Company_Name == "Alliance International"])
unique(data$Company_Name[data$Phone == "+91 7290029556"])
unique(data$Category[data$Pincode == "201301"])
