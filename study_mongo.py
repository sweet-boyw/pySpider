import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['studytest']
collection = db['studytest']

result = collection.find({'age':20})
print(result)