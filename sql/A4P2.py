import sqlite3
import time
import random
import csv 

connection = None
cursor = None

def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)    
    cursor = connection.cursor()    
    cursor.execute(' PRAGMA foreign_keys=ON; ')   
    connection.commit()
    return
  
def query_no(num):
	global connection,cursor,fo
	
	alltime = 0
	counter = 0
	while counter < num:
		counter = counter+1
		starttime = time.time() 
		cursor.execute('SELECT madeIN,AVG(partPrice) FROM parts GROUP BY madeIN;')
		endtime = time.time()
		alltime = alltime+endtime-starttime		
		row = cursor.fetchall()			   	
	avgtime = alltime/num
	avgtime = avgtime*1000
	str1 = str(avgtime)	
	str2 = 'Average query time for Query Q3: '+str1+'ms'+'\n'
	fo.write(str2)
	return
	
def query_with(num):
	global connection,cursor,fo
	
	cursor.execute('DROP INDEX IF EXISTS idxMadeIn;')
	cursor.execute('DROP INDEX IF EXISTS idxNeedsPart;')
	cursor.execute('CREATE INDEX idxMadeIn ON Parts (MadeIn);')
	alltime = 0
	counter = 0
	while counter < num:
		counter = counter+1
		starttime = time.time() 
		cursor.execute('SELECT madeIN,AVG(partPrice) FROM parts GROUP BY madeIN;')
		endtime = time.time()
		alltime = alltime+endtime-starttime		
	avgtime = alltime/num
	avgtime = avgtime*1000
	str1 = str(avgtime)	
	str2 = 'Average query time for Query Q3: '+str1+'ms'+'\n'
	fo.write(str2)
	return  	
  
def main():
	global connection,cursor,fo
	num = 100
	
	fo = open('a4p2.txt','w+')
	fo.write('Executing Part 2\n\n\n')
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
	
	fo.write('\n Creating Index \n\n\n Executing Task B \n')	
	
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
