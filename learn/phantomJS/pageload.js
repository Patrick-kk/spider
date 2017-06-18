// 利用phantom来实现页面加载
var page = require('webpage').create();
page.open('http://cuiqingcai.com', function(status) {
  console.log("Status: " + status);
  if(status === "success") {
    page.render('cuiqingcai.png');
  }
  phantom.exit();
});
