var page = require('webpage').create();
// viewportSize 是视区的大小，可以理解为你打开了一个浏览器，然后把浏览器窗口拖到了多大
page.viewportSize = {width: 1024, height: 768};
// clipRect 是裁切矩形的大小，需要四个参数，前两个是基准点，后两个参数是宽高
page.clipRect = {top: 0, left: 0, width: 800, height: 600};
page.open('http://www.baidu.com', function(){
    page.render('germy.png');
    phantom.exit();
});