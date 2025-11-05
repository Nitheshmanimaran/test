from pymongo import MongoClient

def list_databases():
    # Connect to the MongoDB server
    client = MongoClient('mongodb://localhost:27017/')
    
    # List databases
    databases = client.list_database_names()
    
    return databases

if __name__ == "__main__":
    dbs = list_databases()
    print("Databases:", dbs)