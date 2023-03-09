from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host= 'localhost',user= 'root', passwd= '*****')
cursor = mydb.cursor()
cursor.execute("create database if not exists task_sql")
cursor.execute("create table if not exists task_sql.mytable(name varchar(30), number int)")

@app.route('/insert', methods= ['POST'])
def insert():
    if (request.method == 'POST'):
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into task_sql.mytable values(%s, %s)", (name, number))
        mydb.commit()
        return jsonify(str("successfully inserted"))

@app.route("/update", methods= ['POST'])
def update():
    if request.method == 'POST':
        get_name = request.json['get_name']
        cursor.execute("update task_sql.mytable set number = number + 500 where name = %s", (get_name,))
        mydb.commit()
        return jsonify(str("updated successfully"))

@app.route("/delete", methods= ['POST'])
def delete():
    if (request.method == 'POST'):
        name_del =request.json['name_del']
        cursor.execute("delete from task_sql.mytable where name = %s", (name_del,))
        mydb.commit()
        return jsonify(str("deleted successfully"))

@app.route("/fetch", methods= ['POST'])
def fetch():
    if (request.method == 'POST'):
        cursor.execute("select * from task_sql.mytable")
        for i in cursor.fetchall():
            return jsonify(str(i))


if __name__ == '__main__':
    app.run()




