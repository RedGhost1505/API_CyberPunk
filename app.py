from flask import Flask, render_template, jsonify, abort, request
from flask_cors import CORS, cross_origin

uri='/api/productos/'
app= Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

products = [
    {
        'id':1,
        'imageSrc':'https://cdn.quasar.dev/img/parallax2.jpg',
        'title':'Title 1',
        'content':'Hola',
        'Info':'Info primer producto',
        'icon': 'las la-tshirt',
        'caption': 'Producto 1'
    },
    {
        'id':2,
        'imageSrc':'https://cdn.quasar.dev/img/parallax2.jpg',
        'title':'Title 2',
        'content':'Hola',
        'Info':'Info segundo producto',
        'icon': 'las la-tshirt',
        'caption': 'Producto 2'
    },
]

#Retorna todos los productos

@app.route(uri,methods=['GET'])
@cross_origin()
def get_tasks():
    return jsonify({'products': products})



#Post para un nuevo producto 

@app.route(uri,methods=['POST'])
@cross_origin()
def create_task():
    if request.json:
        task = {
            'id': len(products)+1,
            'imageSrc': request.json['imageSrc'],
            'title':  request.json['title'],
            'content':  request.json['content'],
            'Info': request.json['Info'],
            'icon': 'las la-tshirt',
            'caption': 'Producto ' + str(len(products)+1)
            

        }
        products.append(task)
        return jsonify({'update': products}), 201
    else:
        abort(404)


#REMOVE

@app.route(uri+'/<int:id>', methods= ['DELETE'])
@cross_origin()
def delete_task(id):
    dele = [key for key in products if key['id']==id]
    if len(dele) == 0:
        abort(404)
    products.remove(dele[0])
    return jsonify({'result': True})



if __name__=='__main__':
    app.run(debug=True)
