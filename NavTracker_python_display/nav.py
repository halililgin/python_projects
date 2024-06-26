import webbrowser
import csv
import sys
import requests


url = "http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?mf=22&frmdt=01-Dec-2016&todt=01-Apr-2017"
# http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?mf=22&frmdt=01-Dec-2016&todt=01-Apr-2017

mfCode = {}
sdate = ""
edate = ""


def csv_reader(file_obj):
    reader = csv.DictReader(file_obj)
    for row in reader:
        print(" ".join(row))


mfCode_path = "mfCode.csv"

with open(mfCode_path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        mfCode[row["Scheme Branch"]] = row["AMFI No"]


print(mfCode)
CSV_URL = url
"""
#ftpstream = urllib.request.urlopen(url)
proxy_support = urllib.ProxyHandler({"http":""})
opener = urllib.build_opener(proxy_support)
urllib.install_opener(opener)
ftpstream = urllib.request.urlopen(url)
csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
for line in csvfile:
    print(line)  # do something with line

response = urllib.request.urlopen(url)
html = response.read()
print(html)

with requests.Session() as s:
    download = s.get(CSV_URL,proxies={""})

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)
"""
webbrowser.open_new(url)
