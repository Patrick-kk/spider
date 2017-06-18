/*
    当接受到请求时，可以通过改写
    onResourceRequested 和 onResourceReceived 回调函数
    来实现接收到资源请求和资源接受完毕的监听
*/

var url = 'http://www.baidu.com';
var page = require('webpage').create();
page.onResourceRequested = function(request){
    console.log('Request ' + JSON.stringify(request, undefined, 4));
};
page.onResourceReceived = function(response){
    console.log('Receive ' + JSON.stringify(response, undefined, 4));
};
page.open(url);
phantom.exit();

//运行结果会打印出所有资源的请求和接收状态，以JSON格式输出