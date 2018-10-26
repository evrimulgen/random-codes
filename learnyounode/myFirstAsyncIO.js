var fs = require('fs');
var file = process.argv[2];

function callback(err, data) {
	fs.readFile(file, function (err, fileContents) {
		if (err) {
			return console.log(err)
		}
		// fs.readFile(file, 'utf8', callback) can also be used
		var lines = fileContents.toString().split("\n").length -1
		console.log(lines)
	})
};

callback()