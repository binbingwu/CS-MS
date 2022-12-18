from pymongo import MongoClient

def main():   
	
	client=MongoClient('localhost',27017)
	db = client["A5db"]
	list_conn = db["listings"] 
	loc = input("neighbourhood:")
	result = list_conn.aggregate([{"$group":{"_id":loc,"avg":{"$avg": "$price"}}}])
	for i in result:
		print(i)
		    
if __name__ == "__main__":
    main()
