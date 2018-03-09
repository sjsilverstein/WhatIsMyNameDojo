from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/') #This is the root
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	print "Got Post Info"
	name = request.form['name']
	print name
	return redirect('/')

app.run(debug=True)