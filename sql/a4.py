import sqlite3
import time
import random
import csv 

connection = None
cursor = None
numberlist = []
countrylist = []

def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)    
    cursor = connection.cursor()    
    cursor.execute(' PRAGMA foreign_keys=ON; ')   
    connection.commit()
    return

def csvtolist():
	global numberlist, countrylist
	
	csvfile = open('upc_corpus.csv','r',encoding='utf-8')
	csvnumber = csv.reader(csvfile)
	for item in csvnumber:
		item[0].strip()
		if item[0].isdigit() and len(item[0]) <= 16:			
			num=int(item[0])
			numberlist.append(num)			
	csvfile.close()
	csvfile = open('data_csv.csv')
	csvnumber = csv.reader(csvfile)
	for item in csvnumber:
		countrylist.append(item[0])
	csvfile.close()	

	return
    
def population():
	global connection, cursor,numberlist,countrylist	
	
	needlist = numberlist
	random.shuffle(needlist)
	path = 'A4v100.db'
	connect(path)
	counter = 0
	while counter <= 99:
		cty=random.randint(1,249)-1		
		connection.execute('INSERT OR IGNORE INTO parts (partNumber,partPrice,needsPart,madeIn) VALUES (?,?,?,?)',(numberlist[counter],random.randint(1,100),needlist[counter],countrylist[cty]))
		counter=counter+1
	connection.commit()
	connection.close()   

	random.shuffle(numberlist)
	random.shuffle(needlist)
	random.shuffle(countrylist)
	path1k = 'A4v1k.db'
	connect(path1k)
	counter = 0
	while counter<=999:		
		cty=random.randint(1,249)-1	
		connection.execute('INSERT OR IGNORE INTO parts (partNumber,partPrice,needsPart,madeIn) VALUES (?,?,?,?)',(numberlist[counter],random.randint(1,100),needlist[counter],countrylist[cty]))
		counter=counter+1
	connection.commit()
	connection.close() 
	
	random.shuffle(numberlist)
	random.shuffle(needlist)
	random.shuffle(countrylist)   
	path10k = 'A4v10k.db'
	connect(path10k)
	counter = 0
	while counter<=9999:
		cty=random.randint(1,249)-1	
		connection.execute('INSERT OR IGNORE INTO parts (partNumber,partPrice,needsPart,madeIn) VALUES (?,?,?,?)',(numberlist[counter],random.randint(1,100),needlist[counter],countrylist[cty]))
		counter=counter+1
	connection.commit()
	connection.close()    
	
	random.shuffle(numberlist)
	random.shuffle(needlist)
	random.shuffle(countrylist)
	path100k = 'A4v100k.db'
	connect(path100k)
	counter = 0
	while counter<=99999:
		cty=random.randint(1,249)-1	
		connection.execute('INSERT OR IGNORE INTO parts (partNumber,partPrice,needsPart,madeIn) VALUES (?,?,?,?)',(numberlist[counter],random.randint(1,100),needlist[counter],countrylist[cty]))
		counter=counter+1
	connection.commit()
	connection.close() 
	
	random.shuffle(numberlist)
	random.shuffle(needlist)
	random.shuffle(countrylist)
	path1m = 'A4v1M.db'
	connect(path1m)
	counter = 0
	while counter<=999999:
		cty=random.randint(1,249)-1	
		connection.execute('INSERT OR IGNORE INTO parts (partNumber,partPrice,needsPart,madeIn) VALUES (?,?,?,?)',(numberlist[counter],random.randint(1,100),needlist[counter],countrylist[cty]))
		counter=counter+1
	connection.commit()
	connection.close()    
	return    
    
  
def main():
    global connection, cursor,numberlist,countrylist
    
    csvtolist()
    population()
    return

if __name__ == "__main__":
    main()
