from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World"

@app.route('/second')
def second():
    return "This is te second page"

@app.route('/third/subthird')
def third():
    return "This is the subpage of third page"

@app.route('/fourth/<string:id>')
def fourth(id):
    return f'Id number of this page is : {1250}'

if __name__ == '__main__':
    app.run(debug=True, port=2000)