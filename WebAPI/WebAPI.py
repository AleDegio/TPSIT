"""
Alessia De Giovannini
Web API
"""
import flask 

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Biblioteca online</h1><p>Prototipo di web API.</p>"
app.run()

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    if 'id' in request.args: 
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    results = []

    for book in books: 
        if book['id'] == id: 
            results.append(book)

    return jsonify(results)