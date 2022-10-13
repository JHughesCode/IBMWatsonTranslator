from flask import Flask, render_template, request
import translator

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route("/EnglishtoFrench")
def EnglishtoFrench():
    return

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    french_text = translator.translator.e2f(textToTranslate)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_text = translator.translator.f2e(textToTranslate)
    return english_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

@app.route("/about")
def view_about_page():
    return render_template("about.html", title="About project")

if __name__ == "__main__":
    app.run(debug=True)


