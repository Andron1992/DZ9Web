from pymongo import MongoClient
import json


def upload_to_mongodb():
    client = MongoClient('mongodb+srv://Andronweb8:20242024@cluster0.6hgsz.mongodb.net/')
    db = client['DZ9']
    quotes_collection = db['quote']
    authors_collection = db['author']

    with open('D:\\DZ8\\DZ1\\quotes.json', 'r', encoding='utf-8') as f:
        quotes = json.load(f)

    with open('D:\\DZ8\\DZ1\\authors.json', 'r', encoding='utf-8') as f:
        authors = json.load(f)

    quotes_collection.insert_many(quotes)
    authors_collection.insert_many(authors)


if __name__ == '__main__':
    upload_to_mongodb()
