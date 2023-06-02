from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key="Python is for Winners"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_route')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return redirect('/')

@app.route('/specify_increment', methods = ['post'])
def specify_increment():
    session['Specify Increment'] = request.form['Specify Increment']
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += int(session['Specify Increment']) -1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

