import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/universities', methods=['GET'])
def getUniversities():
    return {
        "data": ["Politecnico di Milano", "Statale di milano"]
    }

app.run()