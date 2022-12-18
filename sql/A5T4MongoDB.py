from pymongo import MongoClient
def main():

	client=MongoClient('localhost',27017)
	db = client["A5db"]
	list_conn = db["listings"]  
	result = list_conn.find({"reviews":{"$exists":0 }}).sort([("id",1)]).limit(10)
	for i in result:
		for k,v in i.items():
			if k == "id":
				print(v)	
    
if __name__ == "__main__":
    main()
