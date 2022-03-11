# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
# from annotell_data_transformation import ReadFile
# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
from converter import ReadFile
import json

@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):
		data = "Welcome to Annotell"
		return jsonify({'data': data})


@app.route('/get_result/', methods = ['GET'])
def get_result():
	path_to_annotell_annotation = 'annotell_1.json'
	with open(path_to_annotell_annotation, 'r') as content:
		json_body = json.load(content)
	result = ReadFile().convert(json_body)
	return result


# driver function
if __name__ == '__main__':
	app.run(debug = True)
