from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from pymongo import MongoClient
from connexion import Query

#FLASK
app = Flask(__name__)

#Connection
client = Query().conn()
conn = client.WWF.Don
login = client.WWF.Compte
user_token = ""


def compte(user, password):
    user = user
    password = password
    conn = client.WWF.Compte.find({"user": {"$eq": user}})
    for i in conn:
        item = i
    try: item
    except NameError: item = None
    if (item):
        global user_token 
        user=item["user"]
        if (password == item["user"]):
            password=item["password"]
            user_token = user
            return True
        else:
            return False


#Web
@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        user = request.form["user"]
        password = request.form["password"]
        if compte(user, password):
            return render_template("main.html", resulta=user_token)
    return render_template("main.html", resulta=user_token)

@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        mail = request.form['mail']
        don = request.form["don"]
        #checkbox = request.form["check"]

        if nom == '' or prenom == '' or don == '':
            pass
        else:
            item = { "nom": nom, "prenom": prenom,"mail": mail, "don": don}
            conn.insert(item)

    return render_template('form.html',resulta=user_token)

@app.route('/info')
def info():
    item = list(conn.find())
    y=0
    for i in item:
        y += int(i["don"])
    post = y

    return render_template('info.html', post=post, result=item, resulta=user_token)
