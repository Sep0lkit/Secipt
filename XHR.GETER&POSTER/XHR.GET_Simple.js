/*
 * @KaiyiZhang Github
 */
var url = "$URL";                                        //The Target       
var xhr = new XMLHttpRequest();
xhr.open("GET",url,"$IsAsync[True|False]");              // Ture: Async

xhr.onreadystatechange = function() {
  if(xhr.readyState==4){
       console.log('xhr:',xhr);
       console.log('data:',xhr.responseText);
  }
}

xhr.send();
