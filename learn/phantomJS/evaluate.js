/*
解决输出字符串包含中文时显示乱码问题：
1. 在脚本中加入 phantom.outputEncoding="gb2312"

2. 运行命令时，添加参数 --output-ecoding=gb2312

http://blog.sina.com.cn/s/blog_6264e0aa0102w1sq.html
*/

phantom.outputEncoding="gb2312"
var url = 'http://www.baidu.com';
var page = require('webpage').create();
//任何来自于网页并且包括来自 evaluate() 内部代码的控制台信息，默认不会显示。
//需要重写这个行为，使用 onConsoleMessage 回调函数
page.onConsoleMessage = function (msg){
    console.log(msg);
};
page.open(url, function(status){
    var title = page.evaluate(function(){
        return document.title;
    });
    console.log('Page title is ' + title);
    phantom.exit();
});
