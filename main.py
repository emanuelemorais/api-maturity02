from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/novo', methods=['POST'])
def novoPedido():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    description = data.get('description')
    con = sqlite3.connect("./database/sqlite.db")
    cur = con.cursor()
    cur.execute("INSERT INTO pedidos (name, email, description) VALUES (?, ?, ?)", (name, email, description))
    con.commit()

    return jsonify({"status": "success"})

@app.route('/pedidos', methods=['GET'])
def pedidos():
    con = sqlite3.connect("./database/sqlite.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM pedidos")
    pedidos = cur.fetchall()
    return jsonify({"pedidos": pedidos})


@app.route('/pedidos/<int:id>', methods=['GET'])
def pedidoById(id):
    con = sqlite3.connect("./database/sqlite.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM pedidos WHERE id = ?", (str(id)))
    pedidos = cur.fetchall()
    return jsonify({"pedidos": pedidos})

@app.route('/pedidos/<int:id>', methods=['PUT'])
def editPedido(id):
    con = sqlite3.connect("./database/sqlite.db")
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    description = data.get('description')
    cur = con.cursor()
    cur.execute("UPDATE pedidos SET name = ?, email = ?, description = ? WHERE id = ?", (name, email, description, id))
    con.commit()
    return jsonify({"status": "success"})

@app.route('/pedidos/<int:id>', methods=['DELETE'])
def deletePedido(id):
    con = sqlite3.connect("./database/sqlite.db")
    cur = con.cursor()
    cur.execute("DELETE FROM pedidos WHERE id = ?", (str(id)))
    con.commit()
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True, port=8000, host="0.0.0.0")