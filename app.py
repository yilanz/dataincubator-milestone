from flask import Flask, render_template, request, redirect
import time
import numpy as np
import pandas

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.templates import RESOURCES
from bokeh.util.string import encode_utf8

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
		#print app.vars
		return redirect('/stock_plot')

@app.route('/stock_plot',methods=['GET','POST'])
def stock_plot():
	# compute start and end time
	end_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	start_time = time.strftime('%Y-%m-%d',time.localtime(time.time()-60*60*24*30))
	# construct API request
	req = 'https://www.quandl.com/api/v3/datasets/WIKI/'+app.vars['stock_name']+'.json?start_date='+start_time+'&end_date='+end_time
	
	# read API results using pandas
	df = pandas.read_json(req)
	df = df['dataset']
	id = df["column_names"].index('Close')
	date_id = df["column_names"].index('Date')
	data = np.asarray(df['data'])
	plot_time = data[:,date_id]
	plot_data = data[:,id]
	plot_time = np.asarray(plot_time,dtype=np.datetime64)
	plot_data = np.asarray(plot_data)

	# construct response html
	# Get all the form arguments in the url with defaults
	fig = figure(title="Closing Price of "+app.vars['stock_name'],x_axis_type="datetime")
	fig.line(plot_time, plot_data)
	fig.xaxis.axis_label = 'Date'
	fig.yaxis.axis_label = 'Closing Price'
	plot_resources = RESOURCES.render(js_raw=INLINE.js_raw,css_raw=INLINE.css_raw,js_files=INLINE.js_files,css_files=INLINE.css_files,)
	 
	script, div = components(fig)
	return render_template('stock_plot.html',stock_name = app.vars['stock_name'],plot_script=script, plot_div=div,plot_resources=plot_resources)
	

	
if __name__ == '__main__':
  app.run(debug=True,port=33507)
  
 #https://www.quandl.com/api/v3/datasets.json?database_code=WIKI&per_page=100&page=1&auth_token=4q-myt_cdzW9VsLz49Kz
  