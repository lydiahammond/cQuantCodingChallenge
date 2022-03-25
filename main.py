import csv

read2016 = csv.reader(open("ERCOT_DA_Prices_2016.csv"), delimiter=",")
read2017 = csv.reader(open("ERCOT_DA_Prices_2017.csv"), delimiter=",")
read2018 = csv.reader(open("ERCOT_DA_Prices_2018.csv"), delimiter=",")
read2019 = csv.reader(open("ERCOT_DA_Prices_2019.csv"), delimiter=",")

prices=[]
prices.append(list(read2016))
prices.append(list(read2017))
prices.append(list(read2018))
prices.append(list(read2019))

years = ['2016','2017','2018','2019']
months = ['01','02','03','04','05','06','07','08','09','10','11','12']
avgs = []

for year in years:

    for month in months:
        y_m = year + "-" + month
        avgs.append(y_m)
        sum = 0
        count = 0

        for row in prices:
            if y_m in row[0]:
                price = row[2]
                sum += float(price)
                count += 1

        avg = sum/count
        avgs.append(avg)
