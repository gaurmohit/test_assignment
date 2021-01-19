from django.http import HttpResponse
from pymongo import MongoClient
from datetime import datetime
import json

# Create your views here.

client = MongoClient('localhost', 27017)
db = client['test_db']
collection = db['test_collection']


# save the document inside the collection
def save(request, yname):
    doc = {
        'author': yname,
        'created_on': datetime.now(),
    }
    inserted_doc = collection.insert_one(doc)
    return HttpResponse(
        json.dumps({
            "message": "item inserted and id is: " + str(inserted_doc.inserted_id)
        })
    )


# show the requested item
def show(request, yname):
    return HttpResponse(
        json.dumps({
            'message': collection.find_one({'author': yname})
        }, default=str)
    )


# show all the documents inside the collection
def show_all(request):
    arr = list()
    for doc in collection.find({}):
        doc['_id'], doc['created_on'] = str(doc['_id']), str(doc['created_on'])
        arr.append(doc)
    # import pdb
    # pdb.set_trace()
    return HttpResponse(
        json.dumps({
            'message': arr
        })
    )
