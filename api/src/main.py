import flask
from flask_cors import CORS,cross_origin


app = flask.Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'






# Quando arriva una chiama GET all'indirizzo di questo server, seguito da /universities
# Allora, chiama la funzione getUniversities
# Poi, il valore che restituisce, lo converti in JSON e lo mandi come risposta via HTTP
@app.route('/universities', methods=['GET'])
@cross_origin()
def getUniversities():
    return {
        "data": ["Politecnico di Milano", "Statale di milano"]
    }


app.run()