from flask import Flask, render_templeate, jsonify, abort, request

uri='/api/productos/'
app= Flask(__name__)



products = [
    {
        'id':1,
        'imageSrc':'https://cdn.quasar.dev/img/parallax2.jpg',
        'title':'Title 1',
        'content':'Hola'
    },
    {
        'id':2,
        'imageSrc':'https://cdn.quasar.dev/img/parallax2.jpg',
        'title':'Title 2',
        'content':'Hola'
    },
]

#Retorna todos los productos

@app.route(uri,methods=['GET'])
def get_tasks():
    return jsonify({'products': products})



#Post para un nuevo producto 

@app.route(uri,methods=['POST'])
def create_task():
    if request.json:
        task = {
            'id': len(products)+1,
            'imageScr': request.json['imageScr'],
            'title':  request.json['title'],
            'content':  request.json['content'],

        }
        products.append(task)
        return jsonify({'update': products}), 201
    else:
        abort(404)


#REMOVE

@app.route(uri+'/<int:id>', methods= ['DELETE'])
def delete_task(id):
    dele = [key for key in products if key['id']==id]
    if len(dele) == 0:
        abort(404)
    products.remove(dele[0])
    return jsonify({'result': True})



if __name__=='__main__':
    app.run(debug=True)