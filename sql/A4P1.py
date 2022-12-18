import sqlite3
import time
import random
import csv 

connection = None
cursor = None
numberlist = []

def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)    
    cursor = connection.cursor()    
    cursor.execute(' PRAGMA foreign_keys=ON; ')   
    connection.commit()
    return

def csvtolist():
	global numberlist,connection,cursor
	
	path = 'A4v1M.db'
	connect(path)
	cursor.execute('SELECT partnumber FROM parts;')
	row = cursor.fetchall()	
	connection.close()
	for item in row:
		num=int(item[0])
		numberlist.append(num)	
	return
    
def query_no(num):
	global connection,cursor,numberlist,fo
	
	counter = 0
	alltime1 = 0
	alltime2 = 0
	random.shuffle(numberlist)	
	while counter < num:		
		upc = numberlist[counter]
		starttime = time.time() 
		cursor.execute('SELECT partPrice FROM parts WHERE partNumber = ?;', (upc,))
		endtime = time.time()
		alltime1 = alltime1+endtime-starttime
		starttime = time.time() 
		cursor.execute('SELECT partPrice FROM parts WHERE needsPart = ?;', (upc,))
		endtime = time.time()		
		alltime2 = alltime2+endtime-starttime
		counter = counter+1
	connection.commit()
	avgtime1 = alltime1/num
	avgtime1 = avgtime1*1000
	avgtime2 = alltime2/num
	avgtime2 = avgtime2*1000	
	str1 = str(avgtime1)
	str2 = 'Average query time for Query Q1: '+str1+'ms'+'\n'
	fo.write(str2)
	str1 = str(avgtime2)
	str2 = 'Average query time for Query Q2: '+str1+'ms'+'\n'
	fo.write(str2)
	return
	
def query_with(num):
	global connection,cursor,numberlist,fo
		
	cursor.execute('DROP INDEX IF EXISTS idxNeedsPart;')
	cursor.execute('CREATE INDEX idxNeedsPart ON Parts (needsPart);')
	counter = 0
	alltime1 = 0
	alltime2 = 0
	while counter < num:		
		upc = numberlist[counter]
		starttime = time.time() 
		cursor.execute('SELECT partPrice FROM parts  WHERE partNumber = ?;', (upc,))
		endtime = time.time()
		alltime1 = alltime1+endtime-starttime
		starttime = time.time() 
		cursor.execute('SELECT partPrice FROM parts  WHERE needsPart = ?;', (upc,))
		endtime = time.time()		
		alltime2 = alltime2+endtime-starttime
		counter = counter+1
	connection.commit()
	avgtime1 = alltime1/num
	avgtime1 = avgtime1*1000
	avgtime2 = alltime2/num
	avgtime2 = avgtime2*1000	
	str1 = str(avgtime1)
	str2 = 'Average query time for Query Q1: '+str1+'ms'+'\n'
	fo.write(str2)
	str1 = str(avgtime2)
	str2 = 'Average query time for Query Q2: '+str1+'ms'+'\n'
	fo.write(str2)	
	return
	
  
def main():
	global connection,cursor,fo
	   
	csvtolist()
	num = 100
	
	fo = open('a4p1.txt','w+')
	fo.write('Executing Part 1\n\n\n')
	fo.write('Executing Task A\n')	
	
	path = 'A4v100.db'
	connect(path)
	fo.write('Opening A4v100.db\n')
	query_no(num)
	fo.write('Closing A4v100.db\n')
	connection.close()
	
	path = 'A4v1k.db'
	connect(path)
	fo.write('Opening A4v1k.db\n')
	query_no(num)
	fo.write('Closing A4v1k.db\n')
	connection.close()
	
	path = 'A4v10k.db'
	connect(path)
	fo.write('Opening A4v10k.db\n')
	query_no(num)
	fo.write('Closing A4v10k.db\n')
	connection.close()
	
	path = 'A4v100k.db'
	connect(path)
	fo.write('Opening A4v100k.db\n')
	query_no(num)
	fo.write('Closing A4v100k.db\n')
	connection.close()
	
	path = 'A4v1M.db'
	connect(path)
	fo.write('Opening A4v1M.db\n')
	query_no(num)
	fo.write('Closing A4v1M.db\n')
	connection.close()
	
	fo.write('\n Creating Index \n\n Executing Task C \n')	
	
	path = 'A4v100.db'
	connect(path)
	fo.write('Opening A4v100.db\n')
	query_with(num)
	fo.write('Closing A4v100.db\n')
	connection.close()
	
	path = 'A4v1k.db'
	connect(path)
	fo.write('Opening A4v1k.db\n')
	query_with(num)
	fo.write('Closing A4v1k.db\n')
	connection.close()
	
	path = 'A4v10k.db'
	connect(path)
	fo.write('Opening A4v10k.db\n')
	query_with(num)
	fo.write('Closing A4v10k.db\n')
	connection.close()
	
	path = 'A4v100k.db'
	connect(path)
	fo.write('Opening A4v100k.db\n')
	query_with(num)
	fo.write('Closing A4v100k.db\n')
	connection.close()
	
	path = 'A4v1M.db'
	connect(path)
	fo.write('Opening A4v1M.db\n')
	query_with(num)
	fo.write('Closing A4v1M.db\n')
	connection.close()	
   
	fo.close
	return

if __name__ == "__main__":
    main()
