var url =   "$URL";                             //The Target
var xhr = new XMLHttpRequest();
xhr.open('POST','$URL');               
xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
xhr.send("$DATA");                              //The Post Data 
