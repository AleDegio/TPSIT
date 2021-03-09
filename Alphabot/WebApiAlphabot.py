"""
Alessia De Giovannini
Web Server
"""
import flask
import sqlite3

path = "percorsi.db"
app = flask.Flask(__name__)
connDB = sqlite3.connect(path, check_same_thread=False)
print("Connessione con DB avvenuta")
 
@app.route('/', methods=['GET', 'POST'])
def index(): 
    return "<h1>Alphabot</h1> \
            <p>Prototipo di web API per l'alphabot.</p> \
            <p>Premere su:</p> \
            <p><a href='./api/v1/resources/percorsi/all'>Per la lista dei percorsi</a> (/api/v1/resources/percorsi/all) </p>\
            <p><a href='./api/v1/resources/luoghi/all'>Per la lista dei luoghi</a> (/api/v1/resources/luoghi/all)</p>\
            <p><a href='./api/v1/resources/inizio_fine/all'>Per la lista dei collegamenti tra luoghi</a> (/api/v1/resources/inizio_fine/all)</p>\
            <p><a href='./api/v1/resources/inizio_fine?start=info1&end=info2'>Per il percorso da info1 a info2</a> (/api/v1/resources/inizio_fine?start=info1&end=info2)</p> \
            <p>inserire '/api/v1/resources/inizio_fine?start=<b>info1</b>&end=<b>info2</b>' modificando le voci info1 e info2 per ottenere gli altri percorsi</p>"

@app.route('/api/v1/resources/percorsi/all', methods=['GET'])
def percorsi_api_all():
    cursor = connDB.execute("SELECT * FROM percorsi")
    res = cursor.fetchall()
    keys = []
    values = []
    for i in range(0, len(res)):
        keys.append(res[i][0])
        values.append([res[i][1]])

    diz = dict(zip(keys, values)) #conversione in dizionario
    
    return flask.jsonify(diz)

@app.route('/api/v1/resources/luoghi/all', methods=['GET'])
def luoghi_api_all():
    cursor = connDB.execute("SELECT * FROM luoghi")
    res = cursor.fetchall()
    keys = []
    values = []
    for i in range(0, len(res)):
        keys.append(res[i][0])
        values.append([res[i][1]])

    diz = dict(zip(keys, values)) #conversione in dizionario
    return flask.jsonify(diz)

@app.route('/api/v1/resources/inizio_fine/all', methods=['GET'])
def inizio_fine_api_all():
    cursor = connDB.execute("SELECT * from inizio_fine")
    res = cursor.fetchall() 
    keys = []
    values = []
    for i in range(0, len(res)):
        keys.append(res[i][0])
        values.append([res[i][1]])

    diz = dict(zip(keys, values)) #conversione in dizionario
    return flask.jsonify(diz)


@app.route('/api/v1/resources/inizio_fine', methods=['GET'])
def inizio_fine_api():

    if 'end' in flask.request.args:
        end = flask.request.args['end']
    else:
        return "Specificare un'aula di arrivo"
    if 'start' in flask.request.args:
        start = flask.request.args['start']
    else:
        return "Specificare un'aula di partenza"

    cursor = connDB.execute("SELECT luoghi.id FROM luoghi WHERE luoghi.nome = ?", (end,))
    idEnd = cursor.fetchone()
    if idEnd is None:
        return "aula di destinazione inesistente"
    idEnd = idEnd[0]

    cursor = None
    cursor = connDB.execute("SELECT luoghi.id FROM luoghi WHERE luoghi.nome = ?", (start,))
    idStart = cursor.fetchone()
    if idStart is None:
         return "aula di partenza inesistente"
    idStart = idStart[0]

    cursor = connDB.execute("SELECT inizio_fine.id_percorso FROM inizio_fine WHERE id_start = ? AND id_end = ?", (idStart, idEnd)) 
    idpercorso = cursor.fetchone()
    if idpercorso is None:
        return "nessun percorso trovato"
    idpercorso = idpercorso[0]

    cursor = connDB.execute("SELECT percorsi.percorso FROM percorsi WHERE percorsi.id = ?", (idpercorso,)) 
    res = cursor.fetchone()[0]
    return flask.jsonify(res)

if __name__ == "__main__":
    app.run(host="127.0.0.1")