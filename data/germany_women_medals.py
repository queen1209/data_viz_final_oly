import csv
import matplotlib.pyplot as plt

year = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]
year_1 = []
year_2 = []
year_3 = []
year_4 = []
year_5 = []
year_6 = []
year_7 = []
year_8 = []
year_9 = []
year_10 = []
year_11 = []
year_12 = []
year_13 = []
year_14 = []
year_15 = []
year_16 = []
year_17 = []
year_18 = []
year_19 = []
year_20 = []
year_21 = []
year_22 = []

categories = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0 

	for row in reader:
		if line_count is 0:
			print("you are in the first row")
			categories.append(row)
			line_count += 1
			
		else: 
			if row[4] == "GER":	
					if row[5] == "Women":
						if row[7] == "Gold":
							if row[0] == "1924":
								year_1.append(row[0])
			
							elif row[0] == "1928":
								year_2.append(row[0])
			
							elif row[0] == "1932":
								year_3.append(row[0])					
			
							elif row[0] == "1936":
								year_4.append(row[0])
			
							elif row[0] == "1948":
								year_5.append(row[0])
			
							elif row[0] == "1952":
								year_6.append(row[0])
			
							elif row[0] == "1956":
								year_7.append(row[0])
				
							elif row[0] == "1960":
								year_8.append(row[0])
			
							elif row[0] == "1964":
								year_9.append(row[0])
			
							elif row[0] == "1968":
								year_10.append(row[0])
				
							elif row[0] == "1972":
								year_11.append(row[0])
				
							elif row[0] == "1976":
								year_12.append(row[0])								

			
							elif row[0] == "1980":
								year_13.append(row[0])

			
							elif row[0] == "1984":
								year_14.append(row[0])		


							elif row[0] == "1988":
								year_15.append(row[0])


							elif row[0] == "1992":
								year_16.append(row[0])


							elif row[0] == "1994":
								year_17.append(row[0])


							elif row[0] == "1998":
								year_18.append(row[0])

							elif row[0] == "2002":
								year_19.append(row[0])
				
							elif row[0] == "2006":
								year_20.append(row[0])

							elif row[0] == "2010":
								year_21.append(row[0])

							elif row[0] == "2014":
								year_22.append(row[0])	


			print(line_count)
			line_count += 1	



medals = [len(year_1), len(year_2),len(year_3),len(year_4),len(year_5),len(year_6),len(year_7),len(year_8),len(year_9),len(year_10),len(year_11),len(year_12),len(year_13),len(year_14), len(year_15),len(year_16),len(year_17),len(year_18),len(year_19),len(year_20), len(year_21), len(year_22)]

graph = plt.plot(year, medals,color = "red")



plt.title("Number of Gold Medals won by Women  (GERMANY 1924-2014)")
plt.ylabel("total Number of medals")
plt.show()