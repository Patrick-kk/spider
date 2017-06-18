// 测试页面加载速度
var page = require('webpage').create(),
  system = require('system'),
   t, address;

if (system.args.length === 1){
    console.log('Usage: loadspeed.js <some URL>');
    phantom.exit();
}

t = Date.now();
address = system.args[1];
if (address.indexOf('http') == -1){
    address = 'http://' + address;
}
console.log('Opening ' + address);
page.open(address, function(status){
    console.log("Status: " + status);
    if (status != "success"){
        console.log('FAIL to load the address');
    } else {
        t = Date.now() - t;
        console.log('Loading ' + system.args[1]);
        console.log('Loading time ' + t + ' m sec');
    }
    phantom.exit();
});
