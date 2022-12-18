from pymongo import MongoClient

def main():   
	
	client=MongoClient('localhost',27017)
	db = client["A5db"]
	list_conn = db["listings"] 
	loc = input("listing_id:")
	result = list_conn.aggregate([{"$unwind":"$reviews"},{"$match":{"id":int(loc)}},{"$sort":{"reviews.date":-1}},{"$limit":1}])
	for i in result:
		for k,v in i.items():
			if k == "host_name": 
				print("  host_name:",v)
			elif k == "price":
				print("  rental_price:",v)
			elif k == "reviews":
				print("  recent review:", v["reviewer_name"])		
	return
		    
if __name__ == "__main__":
    main()
