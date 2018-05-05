import os
import csv

# Lists to store data
dates = []
revenues = []



# Open and read csv
bank1_csv = os.path.join('..', 'PyBank', 'budget_data_1.csv')
bank2_csv = os.path.join('..', 'PyBank', 'budget_data_2.csv')


with open(bank1_csv, newline="") as csvfile:
    csvreader1 = csv.DictReader(csvfile)
    for row in csvreader1:

        dates.append(row["Date"])
        revenues.append(row["Revenue"])
        #print(revenue)

with open(bank2_csv, newline="") as csvfile:
    csvreader2 = csv.DictReader(csvfile)
    for row in csvreader2:

        dates.append(row["Date"])
        revenues.append(row["Revenue"])


#total indeces of lists
indexMax = (len(revenues) - 1)


print(dates)

print(revenues)

totalRevenue = 0
for num in revenues:
    totalRevenue += int(num)

totalMonths = 0
for months in dates:
    totalMonths += 1

greatestInc = 0
greateIncIndex = 0

greatestDec = 0
greatestDecIndex = 0

for x in range(0, indexMax):
    if int(revenues[x]) > greatestInc:
        greatestInc = int(revenues[x])
        greatestIncIndex = x

for y in range(0, indexMax):
    if int(revenues[x]) < greatestDec:
        greatestDec = int(revenues[x])
        greatestDecIndex = y


print("The total revenue is: ")
print("$",totalRevenue)

print("The total months is: ")
print(totalMonths)

averageChange = totalRevenue/totalMonths

print("The average change is: ")
print("$",str(round(averageChange, 2)))

print("The length of the list is: ")
print(indexMax)

print("The greatest increaze was: ")
print(dates[x], revenues[x])

print("The greatest decrease was: ")
print(dates[y], revenues[y])

#moneyTotal += {entries["revenue"][key]}

#print(entries)
