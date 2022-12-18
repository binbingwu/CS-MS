import csv 
from pymongo import MongoClient
listrev = []

def csvtodb():	

	client = MongoClient('localhost',27017)
	db = client["A5db"]
	list_con = db["listings"]
	rev_con = db["reviews"] 
	collist = db.list_collection_names()
	if "listings" or "reviews" in collist:
		print("The collection exists.")		
	list_con.delete_many({})
	rev_con.delete_many({})

	csvlisting = open('YVR_Airbnb_listings_summary.csv','r',encoding='utf-8')
	csvreviews = open('YVR_Airbnb_reviews.csv','r',encoding='utf-8')	
	csv_list = csv.DictReader(csvlisting)
	csv_rev = csv.DictReader(csvreviews)
	
	rev_con.insert_many(csv_rev)	
	for row in csv_list:
		d = {}
		for k,v in row.items():
			if k == "id" or k == "host_id" or k == "price":
				d[k] = int(v)
			else:
				d[k] = v		
		results = rev_con.find({"listing_id":str(d["id"])})
		listrev.clear()
		d1 = {}
		for i in results:
			for k,v in i.items():
				if k == "listing_id" or k == "id":
					d1[k] = int(v)
				else:
					d1[k] = v	
			listrev.append(d1)
		if len(listrev) > 0:
			d["reviews"] = listrev
		list_con.insert_one(d)
	
	rev_con.drop()			
	csvlisting.close()
	csvreviews.close()	
	return   

def main():	   
	csvtodb()
	return

if __name__ == "__main__":
    main()
