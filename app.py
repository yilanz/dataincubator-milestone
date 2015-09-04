from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.vars={}
@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def stock_func():
	nquestion = 4
	if request.method == 'GET':
		return render_template('stock_index.html')
	else:
		#print 'inside else'
		app.vars['stock_name'] = request.form['stock_name']
		app.vars['features'] = request.form.getlist('features')
		#print app.vars
		return redirect('/stock_plot')

@app.route('/stock_plot',methods=['GET','POST'])
def stock_plot():
	return render_template('stock_plot.html',stock_name = app.vars['stock_name'],features=app.vars['features'])

	
if __name__ == '__main__':
  app.run(debug=True,port=33507)
  