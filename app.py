import os
os.environ['OPENAI_API_KEY']="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"

from langchain.llms import OpenAI

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)
llm = OpenAI(temperature=0.9)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       return render_template('hello.html', name = llm(name))
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
