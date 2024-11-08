import redis

# Connect to Redis
client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Create DB and insert data
client.set("product:1", "Product A, Price: 10")
client.set("product:2", "Product B, Price: 15")

# Retrieve data
print(client.get("product:1").decode('utf-8'))

# Update data
client.set("product:1", "Product A, Price: 12")

# Delete data
client.delete("product:2")