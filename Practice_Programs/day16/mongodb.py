from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = r"mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"), tlsAllowInvalidCertificates=True)

# Send a ping to check if connection successful
try:
    client.admin.command("ping")
    print("Pinged. Connection successful.")
except Exception as e:
    print(e)
