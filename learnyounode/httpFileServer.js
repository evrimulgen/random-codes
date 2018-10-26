var fs = require('fs');
var http = require('http');

var port = process.argv[2]
var file = process.argv[3]

var server = http.createServer(function callback(request, response) {
	fs.createReadStream(file).pipe(response);
});

server.listen(port);


/*var http = require('http')
var fs = require('fs')

var server = http.createServer(function (req, res) {
  res.writeHead(200, { 'content-type': 'text/plain' })

  fs.createReadStream(process.argv[3]).pipe(res)
})

server.listen(Number(process.argv[2]))*/