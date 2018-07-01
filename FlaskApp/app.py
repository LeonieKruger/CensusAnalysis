

#https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
from flask import Flask, render_template, json, request
app = Flask(__name__)

from flaskext.mysql import MySQL
mysql = MySQL()
mysql.init_app(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp')
def signUp():
    @app.route('/signUp',methods=['POST'])
    def signUp():
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        # validate the received values
        if _name and _email and _password:
            return json.dumps({'html':'<span>All fields good !!</span>'})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})



@app.route("/Authenticate")
def Authenticate():
    name = request.args.get('inputName')
    email = request.args.get('inputEmail')
    password = request.args.get('inputPassword')
    conn = mysql.connect()
    cursor = conn.cursor()
    sql="INSERT INTO BucketList.tbl_user (user_id,user_name,user_username,user_password) " "VALUES ({}," "'{}'," "'{}'," " '{}' ); ".format(9, name ,email , password)
    number_of_rows = cursor.execute(sql)
    conn.commit()
    return "Successfully registered " +sql

if __name__ == "__main__":
    app.run()

