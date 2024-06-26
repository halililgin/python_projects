import webview
import threading
import http.server
import socketserver
from flask import Flask, render_template, request, url_for, jsonify
import pandas as pd

import os, json
from navDirect import fetchNav


'''
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
def startServer():
	with socketserver.TCPServer(("", PORT), Handler) as httpd:
		print("serving at port", PORT)
		httpd.serve_forever()
		
'''
db = './data/cleanedCSV.csv'
schemes = './data/fundDB.csv'
amfiCode = './data/mfCode.csv'
schemeDB = './static/test.json'

def startServer():
	#app.debug=True
	app.run(host="127.0.0.1",port=8000,threaded=True)
	

app = Flask(__name__)
 
 
@app.route("/")
def hello():
	fundHouse = pd.read_csv(amfiCode)
	schemeList = pd.read_csv(schemes)
	navs = pd.read_csv(db)
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT)
	#schemedata=""#pd.read_json(schemeDB)
	#data = json.load(open(json_url))
	return render_template('app.html',fundHouse=fundHouse) #"Hello World!"
'''
@app.route("/json", methods=['GET'])
def show_json():
	#df=pd.read_json('test.json')
	return open('./static/test.json').read()
'''
@app.route('/_get_schemes')
def get_schemes():
	df = pd.read_csv(schemes)
	fund = request.args.get('f', 0, type=str)
	#b = request.args.get('b', 0, type=int)
	x=df[df['fundHouse']==fund]	
	return jsonify(result=x['fundName'].to_json(orient='records'))

@app.route('/_show_nav')
def show_nav():
	df = pd.read_csv(amfiCode)
	fH = request.args.get('fH', 0, type=str)
	sch = request.args.get('sch', 0, type=str)
	sd = request.args.get('sd', 0, type=str)
	ed = request.args.get('ed', 0, type=str)
	#b = request.args.get('b', 0, type=int)
	x = df[df['FundHouse']==fH]
	mf = df.loc[df['FundHouse']==fH,'AMFI_No'].values[0]
	#print (mf,sch,sd,ed)
	urlStr="http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?mf="+str(mf)+"&frmdt="+sd+"&todt="+ed
	fetchNav(url=urlStr)
	df=pd.read_csv(db)
	x=df[df['Scheme Name']==sch]
	return jsonify(result=x.to_json(orient='records'))
	#return jsonify(result=x)

@app.route("/test" , methods=['GET', 'POST'])
def test():
	select = request.form.get('fundHouse')
	return(str(select)) # just to see what select is

def startServer():
	#app.debug=True
	app.run(host="127.0.0.1",port=8000,threaded=True)
	


if __name__ == "__main__":
	t = threading.Thread(target=startServer)
	t.daemon = True
	t.start()    
	webview.create_window("Hi!", "http://127.0.0.1:8000/")	
	sys.exit()
	
    

'''
if __name__ == '__main__':
    """  https://github.com/r0x0r/pywebview/blob/master/examples/http_server.py
    """
	
    t = threading.Thread(target=startServer)
    t.daemon = True
    t.start()
 
    webview.create_window("Hi!", "http://127.0.0.1:8000/app.html")
 
    sys.exit()

	'''