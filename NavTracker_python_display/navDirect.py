#from selenium import webdriver
from tqdm import tqdm
import pandas as pd
from io import StringIO
#from tqdm import tqdm
import urllib
import os

import csv

phantomjsExe="C:/Users/608619925/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe"
url="http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?mf=22&frmdt=01-Apr-2015&todt=30-Apr-2017"
frmdt="01-Apr-2016"
todt="30-Apr-2016"
mf=9
urlStr="http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?mf="+str(mf)+"&frmdt="+frmdt+"&todt="+todt
phantomjsExe='./phantomJS/phantomjs.exe'
def fetchNav(url):
    #driver = webdriver.PhantomJS(executable_path=phantomjsExe) # or add to your PATH
    #driver.set_window_size(1024, 768) # optional
    #driver.get(url)
    #preTextEl = driver.find_element_by_css_selector("pre")
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read().decode('utf-8')
    #x = urllib.request.urlopen(url)
    #data=preTextEl.text.split(";")
    #print (preTextEl.text)
    #driver.save_screenshot('screen.png') # save a screenshot to disk
    #sbtn = driver.find_element_by_css_selector('button.gbqfba')
    #sbtn.click()
    #csvFile = open('example.csv', 'w', newline='')
    op_file="./data/cleanedCSV.csv"

    tqdm.pandas(tqdm,mininterval=1)

    df = pd.read_csv(StringIO(str(respData)),sep=";")
    #df.drop('Repurchase Price',axis=1)
    df.drop('Sale Price',axis=1)
    df.to_csv(op_file,index=False)
    #driver.close

    #df.plot()
'''
with open(op_file, 'w',newline='\r',encoding="utf-8") as f:
    writer = csv.writer(f,delimiter=';')
    writer.writerows([data])
    for r in tqdm(range(os.path.getsize(op_file))):
        pass
'''
'''		
my_file_name = "some.csv"
cleaned_file = "cleansome.csv"
remove_words = [";"]

with open(my_file_name, 'r', newline='') as infile, open(cleaned_file, 'w',newline='') as outfile:
    writer = csv.writer(outfile)
    for line in csv.reader(infile, delimiter=';'),tqdm(range(len(line))):
        if not any(remove_word in line for remove_word in remove_words):
            writer.writerow(line)
'''    
    
    
    
#writer.close
#print (len(data)
fetchNav(url=urlStr)
