 $( document ).ready(function() {
 
//ping  
 $.getJSON("https://api.ipify.org?format=jsonp&callback=?",
      function(json) { 
        window.ip = json.ip;
	$.ajax({
	    url: "/ping",
	    type: "post",
	    contentType: "application/json; charset=utf-8",
	    dataType: "json",
	    data: JSON.stringify({'ip':json.ip}),
        success: function(response){ 
	    }
	});
      }
    );

$( window ).unload(function() {
//pong
$.ajax({
    url: "/pong",
    type: "post",
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    data: JSON.stringify({'ip':window.ip}),
    success: function(response){ 

    }
});
}); 


});