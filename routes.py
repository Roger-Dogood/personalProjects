from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/homework')
def homework():
    return render_template('homework.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/cit-142')
def cit142():
    return render_template('cit142/cit-142.html')

@app.route('/cit-142/assignment01')
def assignment01():
    return render_template('cit142/assignment01.html')

@app.route('/cit-142/assignment02')
def assignment02():
    return render_template('cit142/assignment02.html')

if __name__ == '__main__':
    app.run(debug=True)
