import flask
from flask_cors import CORS, cross_origin
import requests


# Questa funzione riceve un oggetto di quelli restituiti dall'API (una unversità)
# e restituisce un oggetto come lo vuole il nostro front-end.
def apiUniversityToUniversity(apiUniversity):
    return{
        'name': apiUniversity['name'],
        'description': apiUniversity['web_pages'][0],
        'imgSrc': 'https://upload.wikimedia.org/wikipedia/it/b/be/Logo_Politecnico_Milano.png'
    }


app = flask.Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

apiAddress = f'http://universities.hipolabs.com'


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

    ricerca = flask.request.args['search']
    # 1. Chiamare l'API
    byNameResponse = requests.get(apiAddress + f'/search?name={ricerca}')
    byCountryResponse = requests.get(apiAddress + f'/search?country={ricerca}')
    byNameResult = byNameResponse.json()
    byCountryResult = byCountryResponse.json()

    result = byCountryResult+byNameResult

    # 2. Trasformiamo i dati
    # Questo trasforma tutti gli elementi di una lista, uno per uno, applicando una funzione che gli passiamo tra parentesi
    #universities = map(apiUniversityToUniversity, byNameResult)

    # Questa map è esattamente come fare questo:
    universities = []
    for element in result:
        transformedElement = apiUniversityToUniversity(element)
        universities.append(transformedElement)

    return {

        "universities": universities


    }


app.run()
