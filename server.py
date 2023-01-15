from flask import Flask, request, make_response, jsonify
import subprocess, silly_story
app = Flask(__name__)

@app.route('/search')
def search():
	matching_lines = {"desala":[],"gen":[]}
	query = request.args.get('query')
	context_len = 2
	with open('desala.txt', 'r') as f:
		words = silly_story.associate(f, context_len)
		s = silly_story.get_context(words, context_len)
		f.seek(0)
		lines = f.readlines()
	matching_lines["desala"] = [line for line in lines if query in line]
	lines = s.split("\n")
	matching_lines["gen"] = [line for line in lines if query in line]
	resp = jsonify(matching_lines)
	resp.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000'
	print(resp)
	return resp

if __name__ == '__main__':
    app.run()
