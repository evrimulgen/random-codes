var bl = require('bl');
var http = require('http');

http.get(process.argv[2], function (response) {
  response.setEncoding('utf8')
  response.pipe(bl(function (err, data) {
  	console.log(data.toString().length);
  	console.log(data.toString());
  }))
  response.on('error', console.error)
}).on('error', console.error)

