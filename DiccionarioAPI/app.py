import os
from flask import Flask, redirect, render_template, request , send_from_directory, url_for , jsonify  
from Models.MongoDBConnection import MongoDBConnection
from bson.json_util import dumps 
from flask_cors import CORS
from bson import ObjectId
 

app = Flask(__name__)


cors = CORS(app, resources={r"/*": {"origins": "*"}})

mongo_uri = "mongodb+srv://javiersmuela:3VE7Du3rq2HLWK3E@cluster0.wf5o5.mongodb.net/?retryWrites=true&w=majority"

# URL Mongo para que haga conexión con la base de datos.

if not mongo_uri: 
    print("Error Get Enviroment")


mongo_connection = MongoDBConnection(mongo_uri)

@app.route('/definicion/<word>')
def index(word):
    try:
        # Intentar establecer la conexión a MongoDB
        mongo_connection.connect("dbdiccionario" , "diccionario")
            
        # Realizar consultas a la base de datos usando el método perform_query
        results = mongo_connection.perform_query({"word": word})
            
        if results:
             # Crear un diccionario con el orden deseado
            response_data = {
                "_id" : str(results['_id']) ,
                "word": results["word"],
                "definition": results["definition"],
                "examples" : results["examples"],
              
             }


            return jsonify(response_data)
        else:
            return jsonify({   "error" : "No hay resultados."})

    except  Exception as e:  
        return jsonify(e) 



@app.route('/sinonimos/<word>')
def sinonimos(word):
    try:
        mongo_connection.connect("dbdiccionario" , "diccionario")

        # Realizar consultas a la base de datos usando el método perform_query
        results = mongo_connection.perform_query({"word": word})

        if results:
            sinonimos = results.get("synonyms", [])
            return jsonify({   "_id" : str(results['_id']) ,  "word": word, "sinonimos": sinonimos})
        else:
            return jsonify({   "error" : "No hay resultados."})
    except Exception as e:
        return jsonify({"error": str(e)})



@app.route('/antonimos/<word>')
def antonimos(word): 
    try:
        # Intentar establecer la conexión a MongoDB
        mongo_connection.connect("dbdiccionario" , "diccionario")

        # Realizar consultas a la base de datos usando el método perform_query
        results = mongo_connection.perform_query({"word": word})

        if results:
            antonimos = results.get("antonyms", [])
            return jsonify({   "_id" : str(results['_id']) , "word": word, "antonimos": antonimos})
        else:
            return jsonify({   "error" : "No hay resultados."})
    except Exception as err:
       return jsonify({"error": str(err)})

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run()
