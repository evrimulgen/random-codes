const http = require('http'),
      bl = require('bl');

var queue = [];
var count = 0;
http.get(process.argv[2],aux(0));
http.get(process.argv[3],aux(1));
http.get(process.argv[4],aux(2));


function aux (i){
    return function callback(response){
                response.pipe(bl(function (err, data) { 
                    queue[i] = data.toString();
                    count++;
                    if(count == 3){
                         queue.forEach(function(pos){
                            console.log(pos);
                         });
                    }
                }));
            };
};




/*    var http = require('http')
    var bl = require('bl')
    var results = []
    var count = 0

    function printResults () {
      for (var i = 0; i < 3; i++) {
        console.log(results[i])
      }
    }

    function httpGet (index) {
      http.get(process.argv[2 + index], function (response) {
        response.pipe(bl(function (err, data) {
          if (err) {
            return console.error(err)
          }

          results[index] = data.toString()
          count++

          if (count === 3) {
            printResults()
          }
        }))
      })
    }

    for (var i = 0; i < 3; i++) {
      httpGet(i)
    }*/