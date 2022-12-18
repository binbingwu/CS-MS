from pymongo import MongoClient

def main():

	client=MongoClient('localhost',27017)
	db = client["A5db"]
	list_conn = db["listings"]  
	result = list_conn.aggregate([{"$unwind":"$reviews"},{"$group":{"_id":"$host_id","count":{"$sum":1}}},{"$limit":10},{"$sort":{"host_id":1}}])
	for i in result:
		print(i)
	return
    
if __name__ == "__main__":
    main()
