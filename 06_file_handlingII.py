#CSV
import csv
csv_file = open("./my_file.csv","w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name","surname","edad","language","website"])
csv_writer.writerow(["Jose","Perea",26,"Español","perea.com"])
csv_writer.writerow(["Carlos","Jiménez Díaz",+9000,"Español","fundacionjimenezdiaz.com"])

csv_file.close()