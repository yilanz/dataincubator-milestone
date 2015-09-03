from falsk import Flask, render_template, request

app_stock = Flask(__name__)

@app_stock.route('/stock_index',methods=['GET','POST'])
def stock_index():
	nquestion = 4
	if request.method == 'GET':
		return render_template('stock_index.html')
	else:
		return 'reqeust.method was not a GET!'
	
if __name__ == '__main__':
	app_stock.run(port=33507,debug = True)
	