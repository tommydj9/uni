import flask
from flask_cors import CORS, cross_origin


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
    # Noi qua leggeremo i dati da una API esterna -> HTTP GET
    # Quell'API ti restituirà una lista di oggetti/dizionari.
    # Per ognuno di quelli, noi ne creiamo uno nel formato che vogliamo noi, cioè
    # Poi li trasformiamo per restituire al front-end dei dati fatti così:
    #   {
    #       name: ...
    #       description: ...
    #       imgSrc: ...
    #   }
    return {
        "universities": [{
            "name": "Politecnico di Milano",
            "description": "L'università politecnica più grande d'Italia.",
            "imgSrc": "https://upload.wikimedia.org/wikipedia/it/b/be/Logo_Politecnico_Milano.png"
        }, {

            "name": "Statale Milano",
            "description": "sdfghjklaf.",
            "imgSrc": "https://upload.wikimedia.org/wikipedia/it/thumb/0/04/Logo_Universit%C3%A0_degli_Studi_di_Milano.svg/1200px-Logo_Universit%C3%A0_degli_Studi_di_Milano.svg.png"
        },
            {
            "name": "Statale Milano",
            "description": "sdfghjklaf.",
            "imgSrc": "https://upload.wikimedia.org/wikipedia/it/thumb/0/04/Logo_Universit%C3%A0_degli_Studi_di_Milano.svg/1200px-Logo_Universit%C3%A0_degli_Studi_di_Milano.svg.png"
        }]
    }


app.run()
