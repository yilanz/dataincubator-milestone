from falsk import Flask
app_stock = Flask(__name__)

@app_stock.route('/')
def stock_index():
	return "Hello World!"
	
if __name__ == '__main__':
	app_stock.run(debug = True)