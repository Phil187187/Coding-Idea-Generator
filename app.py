from flask import Flask, render_template, request
from brainstorm import brainstorm_html_idea_and_write

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/brainstorm', methods=['POST'])
def brainstorm():
    idea = request.form['idea']
    return brainstorm_html_idea_and_write(idea)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
