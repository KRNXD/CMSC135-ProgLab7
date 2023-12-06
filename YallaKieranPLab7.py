#Kieran Yalla
#8/12/23
#Professor Phong Banh
#CMSC 135
startdate = input("Enter a date in the format mm/dd/yyyy: ")
startlist = startdate.split("/")

month = int(startlist[0])
day = int(startlist[1])
year = int(startlist[2])

monthlist =["January", "February", "March", "April", "May", "June", "July", "August", "September","October", "November", "December"]

monthformat = monthlist[month - 1]

print(monthformat,day, year)




