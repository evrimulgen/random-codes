var net = require('net');
var d = new Date();

var server = net.createServer(function(socket) {
	//socket.write(data)//, date.getFullYear());
	socket.write(socket.write(d.getFullYear() + "-" + 
		( Number(d.getMonth()+1) > 10  ? Number( d.getMonth()+1) : "0"+Number(d.getMonth()+1) )  + "-" + 
		( Number(d.getDate()) > 10  ? Number( d.getDate()) : "0"+Number(d.getDate()) ) + " " + 
		d.getHours() + ":" + d.getMinutes() + "\n"));
	socket.end();
})

server.listen(Number(process.argv[2]));



/*    var net = require('net')

function zeroFill (i) {
  return (i < 10 ? '0' : '') + i
}

function now () {
  var d = new Date()
  return d.getFullYear() + '-' +
    zeroFill(d.getMonth() + 1) + '-' +
    zeroFill(d.getDate()) + ' ' +
    zeroFill(d.getHours()) + ':' +
    zeroFill(d.getMinutes())
}

var server = net.createServer(function (socket) {
  socket.end(now() + '\n')
})

server.listen(Number(process.argv[2]))*/