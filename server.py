from flask import Flask, render_template, request
import translator

app = Flask(__name__)

@app.route("/engtofrench/<word>")
def goFrench(word):
    return translator.e2f(word)


@app.route("/frenchtoeng/<word>")
def goEnglish(word):
    return translator.f2e(word)

@app.route("/")
def renderIndexPage():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)


