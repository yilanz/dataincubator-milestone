from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def stock_index():
	nquestion = 4
	if request.method == 'GET':
		return render_template('stock_index.html')
	else:
		return 'reqeust.method was not a GET!'

if __name__ == '__main__':
  app.run(port=33507,debug = True)