var fs = require('fs');
var file = process.argv[2];
//var list = [];

fs.readdir(file, function (err, fileLocation) {
	if (err) {
		return console.log(err);
	}
	if (process.argv.length >= 4) {
		desiredFiles = process.argv[3];
		for (const i of fileLocation) {
			if (i.split(".")[1] == desiredFiles) {
				//list.push(i);
				console.log(i)
			}
		}
		//console.log(list);
	} else {
	var lines = fileLocation;
	console.log(lines);
	}
})



// LEARNYOUNODE example one. Better one :(
/*var fs = require('fs')
var path = require('path')

var folder = process.argv[2]
var ext = '.' + process.argv[3]

fs.readdir(folder, function (err, files) {
  if (err) return console.error(err)
  files.forEach(function (file) {
    if (path.extname(file) === ext) {
      console.log(file)
    }
  })
})*/