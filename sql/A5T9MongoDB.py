from pymongo import MongoClient

def main():   
	
	client=MongoClient('localhost',27017)
	db = client["A5db"]
	list_conn = db["listings"] 
	k = []
	a = ""
	loc = input("keywords:")
	for i in loc:
		if i !=',':
			a = a+i
		else:
			k.append(a)
			a = ""
	k.append(a)
				
	result = list_conn.aggregate([{"$unwind":"$reviews"},{"$project":{"reviews.reviewer_id":1,"reviews.comments":1}},{"$match":{"$and":[{"reviews.comments":{"$regex":k[0]}},{"reviews.comments":{"$regex":k[1]}},{"reviews.comments":{"$regex":k[2]}}]}},{"$limit":3}])
	for i in result:
		for k,v in i.items():
			if k == "reviews":
				print("reviewer_id:", v["reviewer_id"])
	return
		    
if __name__ == "__main__":
    main()
