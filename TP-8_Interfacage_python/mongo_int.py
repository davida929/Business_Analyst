from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://root:root@localhost:27017/")
db = client["DBventes"]
collection = db["products"]

# Insert data
collection.insert_one({"product_id": 1, "name": "Product A", "price": 10})
collection.insert_one({"product_id": 2, "name": "Product B", "price": 15})

# Query data
for product in collection.find():
    print(product)

# Update data
collection.update_one({"product_id": 1}, {"$set": {"price": 12}})

# Delete data
collection.delete_one({"product_id": 2})