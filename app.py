from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def stock_func():
	nquestion = 4
	if request.method == 'GET':
		return render_template('stock_index.html')
	else:
		app.vars['stock_name'] = request.form['stock_name']
		app.vars['features'] = request.form['features']
#		return redirect('/stock_plot',app.vars)

@app.route('/stock_plot',methods=['POST'])
def stock_plot(app.vars):
	render_template('stock_plot.html',stock_name = app.vars['stock_name'],features=app.vars['features'])

	
if __name__ == '__main__':
  app.run(port=33507,debug = True)
  