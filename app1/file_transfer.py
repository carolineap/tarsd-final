from flask import Flask, jsonify, request

DIRECTORY = ''

app = Flask(__name__)

@app.route('/files', methods=['POST'])
def upload():
    
    if request.method == 'POST':

        name = request.form('name')
        content = request.form('content')

        if name:

            file = open(os.path.join(DIRECTORY, name), 'w')
            file.write(content)


@app.route('/files/<name:name>', methods=['GET'])
def download(name):

    return send_from_directory(directory=DIRECTORY, filename=name, as_attachment=True)



if __name__ == "__main__":

    app.run(host='0.0.0.0', port=80)