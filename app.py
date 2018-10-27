from flask import Flask, jsonify, request

app = Flask(__name__)

usernames = [{'name': 'Kelvin'}, {'name' : 'Darek'}]

@app.route('/', methods=['GET'])
def hello():
	return 'Hello World!'

@app.route('/usernames', methods=['GET'])
def returnall():
	return jsonify({'usernames': usernames})

@app.route('/usernames', methods=['POST'])
def addone():
	username = {'name' : request.json['name']}

	usernames.append(username)

	return jsonify({'usernames': usernames})	



if __name__ == '__main__':
	app.run(debug=True)