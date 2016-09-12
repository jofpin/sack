var xhReq = new XMLHttpRequest();
 xhReq.open("POST", "/not_logged", false);
 xhReq.send(null);
 var serverResponse = xhReq.responseText;
 //alert(serverResponse); //