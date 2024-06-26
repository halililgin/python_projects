var url="http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?mf=22&frmdt=01-Dec-2016&todt=01-Apr-2017";
var http = require('http');
var fs = require('fs');

//var http = require('http');
/*
var csvData = '';
var request = http.get(url, function(response) {
    response.on('data', function(chunk) {
        csvData += chunk;
    });
    response.on('end', function() {
        // prints the full CSV file
        console.log(csvData);
    });
});
*/
var request = require('request');
var options = {
    url:  url,
    timeout: 120000
}

request.get(options, function (error, response, body) {
    if (!error && response.statusCode == 200) {
        var csv = body;
        // Continue with your processing here.
		fs.createWriteStream('file.csv');
    }
});
request(url).pipe(fs.createWriteStream('file.csv'));