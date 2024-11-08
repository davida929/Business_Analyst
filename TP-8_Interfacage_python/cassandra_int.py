from cassandra.cluster import Cluster

# Connexion au cluster Cassandra
cluster = Cluster(['127.0.0.1'], port=9042)  # Spécifiez l'adresse et le port
session = cluster.connect()

# Création d'une keyspace et utilisation
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS DBventes
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
""")
session.set_keyspace('DBventes')

# Création d'une table
session.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id int PRIMARY KEY,
        name text,
        price float
    )
""")

# Insertion des données
session.execute("INSERT INTO products (product_id, name, price) VALUES (1, 'Produit A', 10.0)")
session.execute("INSERT INTO products (product_id, name, price) VALUES (2, 'Produit B', 15.0)")

# Requête pour lire les données
rows = session.execute("SELECT * FROM products")
for row in rows:
    print(row)

# Fermeture de la connexion
cluster.shutdown()