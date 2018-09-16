from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """ 
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
     <form method="post">
    <label>
        Rotate by:
        <input name="rot" type="text" value="0">
    </label>

    <textarea name="text" placeholder="Type message to encode here...">{0}</textarea>

    <input type="submit">
</form>
    </body>
</html>

"""

#url where index function receives requests.  application server sends requests here.
@app.route("/")
#index function handles initial GET request from browser.  This is what user see when app first runs.
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    txt = str(request.form['text'])
    rotation = int(request.form['rot'])
    encrypted = rotate_string(txt, rotation)
    return form.format(encrypted)

app.run()
