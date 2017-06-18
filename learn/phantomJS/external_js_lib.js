phantom.outputEncoding="gb2312";

var page = require('webpage').create();
page.open('http://www.baidu.com', function(){
    page.includeJs('http://code.jquery.com/jquery-1.8.0.min.js', function(){
        var title = page.evaluate(function(){
            $('#su').click();
            return $('title').text();
        });
        console.log('Title is ' + title);
        phantom.exit();
    });
});