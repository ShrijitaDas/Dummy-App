from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    text="Hey There"
    hinText="Hello World"
    return render_template("index.html",result=text,hresult=hinText)

if __name__ == '__main__':
    app.run()