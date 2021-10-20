from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/evaluate', methods=['POST',  'GET'])
def evaluate():
    rawExpr = request.form['mathexpression']
    mathExpr = str(rawExpr)
    try:
        ans = eval(mathExpr)
    except:
        ans = "non-existing due to improper expression"
    return render_template('index.html', eval='Evaluation for {} is {}'.format(mathExpr, ans))

if __name__ == '__main__':
	app.run(debug=True)