/*
脚本都是像在浏览器中运行的，所以标准的 JavaScript 的 DOM 操作和 CSS 选择器也是生效的。

例如下面的例子就修改了 User-Agent，然后还返回了页面中某元素的内容
*/

var page = require('webpage').create();
console.log('The default user agent is ' + page.settings.userAgent);
page.settings.userAgent = 'NewAgent';
page.open('http://www.httpuseragent.org', function(status){
    if (status !== 'success'){
        console.log('Unable to access ');
    } else {
        var ua = page.evaluate(function(){
            return document.getElementById('qua').textContent;
        });
        console.log(ua);
    }
    phantom.exit();
});

