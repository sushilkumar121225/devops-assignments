@app.route('/submittodoitem', methods=['POST'])

def submit():

    data=request.json

    itemName=data['itemName']

    itemDescription=data['itemDescription']

    collection.insert_one({

        "itemName":itemName,

        "itemDescription":itemDescription

    })

    return {"message":"Saved"}