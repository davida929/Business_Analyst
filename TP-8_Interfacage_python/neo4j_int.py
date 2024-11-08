from neo4j import GraphDatabase

# Connect to Neo4j
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

def add_product(tx, product_id, name, price):
    tx.run("CREATE (p:Product {product_id: $product_id, name: $name, price: $price})", product_id=product_id, name=name, price=price)

# Add product
with driver.session() as session:
    session.write_transaction(add_product, 1, "Product A", 10)
    session.write_transaction(add_product, 2, "Product B", 15)

# Query data
with driver.session() as session:
    result = session.run("MATCH (p:Product) RETURN p")
    for record in result:
        print(record["p"])

# Update data
with driver.session() as session:
    session.run("MATCH (p:Product {product_id: 1}) SET p.price = 12")

# Delete data
with driver.session() as session:
    session.run("MATCH (p:Product {product_id: 2}) DELETE p")