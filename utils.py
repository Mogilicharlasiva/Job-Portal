from pymongo import MongoClient
connection_string = "mongodb+srv://mogilicharlasiva:OUPswd8112@cluster0.kkg2q.mongodb.net/"
client = MongoClient('connection_string')
db = client['job_listings']
job_collection = db['jobs']