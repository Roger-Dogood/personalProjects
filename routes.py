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
    return render_template('cit-142.html')

if __name__ == '__main__':
    app.run(debug=True)
