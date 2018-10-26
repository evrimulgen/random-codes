var fs = require('fs');

module.exports = function(filePath, extStr, callback) {
    fs.readdir(filePath, function(err, list) {
        if (err) {
            return callback(err);
        } else {
            var elements = [];
            for (var i = 0; i < list.length; i++) {
                var ext = "." + extStr;
                if (list[i].substr(-1 * ext.length, ext.length) === ext) {
                    elements.push(list[i]);
                }
            }
            callback(null, elements);


        }
    });
}

// MY MADE
/*var fs = require('fs');
module.exports = function(file, desiredExt, callback) {
	fs.readdir(file, function (err, list) {
		if (err) {
			return console.log(err);
		}
		if (process.argv.length >= 4) {
			desiredFiles = process.argv[3];
			for (const i of list) {
				if (i.split(".")[1] == desiredFiles) {
					console.log(i);
				}
			}
		} else {
			callback(null, list)
		}
	});
}*/