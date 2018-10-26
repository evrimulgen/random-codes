var fs = require('fs');
var line = fs.readFileSync(process.argv[2]);
console.log(Number(line.toString().split().toString().split("\n").length)-1)