$(document).ready(function() {

  var Sack = {
    self: this,
    name: "Sack",
    out: "",
    key: "abcdefghijklmnopqrstuvwxyz0123456789",
    token: Math.random().toString().substring(7).substr(0,7),
    array: [0,1,2,3,4,5,6,7,8,9],
    loader: "<ul class=\"loader\"><li></li><li></li><li></li></ul>",
    victims: $.victims,
    attrDeclareOne: $("[data-show-victims1]"),
    attrDeclareTwo: $("[data-show-victims2]"),
    log: function(value) {
      // simplification > console.log
      console.log(value);
    },
    deploy: function() {
      Sack.self.reflectVictims();
      Sack.self.showDetail();
    }
  };
  window.Sack = Sack;

// unique detail function for attr > sack
  Sack.self.jsToken = function() {
    var randomToken = function() {
      // helping: http://stackoverflow.com/questions/8532406/create-a-random-token-in-javascript-based-on-user-details
      return Sack.token;
    };
    var generateToken = function() {
      return randomToken();
    }; 
    var random = function(values) {
      return values[Math.floor((Math.random()*values.length))];
    };
    var supportRand = function() {
      for(var val = 0; val < 5; val++)
        Sack.out += Sack.key.charAt(Math.floor(Math.random()*Sack.key.length));
      return Sack.out; 
    }
    var prefixRand = function() {
      return random(Sack.array)  
    };

    var token = Sack.runToken = prefixRand() + supportRand() + generateToken();

    Sack.log("jsToken:" + " " + token);

    // running token
    return token; 
  }

  // Running jsToken
  var token = Sack.self.jsToken();

Sack.self.showDetail = function() {
  // Generate unique box Modal (Detail) safe touch :)
  $('[button-sack-detail="show"]').attr("href","#showDetail" + "-" + token);
  $(".SackReport-details").attr("id", "showDetail" + "-" + token);
};


$('.SackReport-Tabs--container .SackReport-Tabs--button').on("click", function(e) {
    e.preventDefault();

    // Remove active class from buttons
    $('.SackReport-Tabs--container .SackReport-Tabs--button').removeClass('is-active');

    // Add the correct active class
    $(this).addClass('is-active');

    // Hide all tab items
    $('[class^=tab-item]').hide();

    // Show the clicked tab
    var number = $(this).data('tab-item');
    $('.tab-item-' + number).fadeIn();

    if(number==1){
      Sack.victims.get.getAJAX('show-victims1');
    }else{
      Sack.victims.get.getAJAX('show-victims2');
    }
});

$(".tab-item-1").show();


/* if (typeof Sack.victims === "undefined") { 
      Sack.victims = {};
    } */
  
    Sack.victims = {};

      Sack.victims.get = {

      pull: function() {
        if (Sack.attrDeclareOne) {
          this.getAJAX("show-victims1");
          //this.getAJAX("show-victims2");
        } 
        else {
          Sack.log("information:" + " " + "There is no data :(");
        }
      },

      getAJAX: function(suffix) { 
        /* data get json and ajax not cache :) */
        var self = this;
        $.ajaxSetup({
          url: "/xmlhttp/",
          type: "POST",
          data: { 
            "":"" 
          },
          cache: false
        });

      // loader of data content (JSON is revealed)
      Sack.attrDeclareOne.html(Sack.loader);
      
if(suffix=='show-victims1'){
dynamic = Sack.attrDeclareOne.data(suffix);
}else if(suffix=='show-victims2'){
dynamic = Sack.attrDeclareTwo.data(suffix);
}
      $.post(dynamic, { 
        "":""  
      } , function(data, textStatus) {
        var doHtmlOne = self.relationship(); 
        var doHtmlTwo = self.relationship(); 
        
        $.each(data,function(_,_item) {  
          doHtmlOne += self.showDetailsOne(_item); 
          doHtmlTwo += self.showDetailsTwo(_item); 
        });

        Sack.attrDeclareOne.html(doHtmlOne);
        Sack.attrDeclareTwo.html(doHtmlTwo);


	  $('[button-sack-detail="show"]').click(function(types) {
      var me = $(this);  
      var parent = me.parent().next(".SackReport-details");
      parent.first().addClass("active"); 
      types.preventDefault();
    });

	  $(".close-btn").click(function(types) {
      var me = $(this);  
      var parent = me.parent().parent().parent().removeClass("active"); 
      types.preventDefault(); 
	  });


    }, "json");
      
    /*
      $.getJSON(Sack.attrDeclareOne.data(suffix),function(data) {
        
        var doHtmlOne = self.relationship(); 
        var doHtmlTwo = self.relationship();
        
        $.each(data,function(_,_item) {  
          doHtmlOne += self.showDetailsOne(_item);
          doHtmlTwo += self.showDetailsTwo(_item);
        });

        Sack.attrDeclareOne.html(doHtmlOne);
        Sack.attrDeclareOne.html(doHtmlTwo);
        
      }).error(function(j,t,e) { 
      // error load dataJSON :Â´(
        Sack.attrDeclareOne.html('<div data-error="' + "json" + '">' + "Error" + " " + e + '</div>');
        Sack.log("Error:" + " " + e);
      }); */
      
    },
    
    // your div here here :)
    relationship: function() {
      html = ('');
      return html;
    },

    // data Json
    showDetailsOne: function(data) { 
      var show = {
        id: data.id,
        data2: data.data,
        status: data.status,
        date: data.date,
        time: data.time,
        target: data.target,
        ip: data.ip,
        isp: data.isp,
        country: data.country,
        city: data.city,
        latitude: data.latitude,
        longitude: data.longitude,
        os: data.os,
        browser: data.browser,
        browserVersion: data.browserVersion,
        useragent: data.useragent,
        requests: data.requests,
        ports: data.ports
      }

      html = '<ul class="SackReport-Results--bodyBox">' +
            '<li>' +
              '<span class="SackReport-Results--element---flagLocation">' +
                '<img src="assets/img/flags/' + show["country"] + '.png">' +
              '</span>' +
              '<span class="SackReport-Results--element---ipLocation">' + show["ip"] + '</span>' +
            '</li>' +
            
            '<li style="width: 15%;">' +
              '<span class="SackReport-Results--element---box">' +
                '<span class="SackReport-Results--element---icon SackReport-Results--element---icon----' + show["os"] + '"></span>' +
                '<span class="SackReport-Results--element---text">' + show["os"] + '</span>' +
              '</span>' +
            '</li>' +

            '<li>' +
              '<span class="SackReport-Results--element---box">' +
                '<span class="SackReport-Results--element---icon SackReport-Results--element---icon----' + show["browser"] + '"></span>' +
                '<span class="SackReport-Results--element---text">' + show["browser"] + '</span>' +
              '</span>' +
            '</li>' +
            
            '<li style="width: 20%;">' +
              '<span class="SackReport-Results--element---box">' + show["date"] + ' - ' + show["time"] + '</span>' +
            '</li>' +

            '<li style="width: 10%;">' +
              '<span class="SackReport-Results--element---box"><strong>' + show["requests"] + '</strong> inputs</span>' +
            '</li>' +

            '<li>' +
              '<span class="SackReport-Results--element---showDetails">' +
                '<a class="SackReport-element--detailsText" href="#" button-sack-detail="show">' +
                  '<span class="m icon-database"></span> Details <span class="icon-angle-double-right"></span></a>' +
              '</span>' +

              '<div class="SackReport-details">' +
                '<div class="SackReport-details--reflect">' +
                  '<div class="SackReport-details--reflect---Header">' +
                    '<div class="close-btn">' +
                      '<i class="icon-times"></i>' +
                    '</div>' +
                    '<h2 class="SackReport-details--reflect---Header----title"><span class="icon-database"></span> Details</h2>' +
                  '</div>' +

                  '<div class="SackReport-details--reflect---subHeaderData">' +
                    '<div class="SackReport-details--reflect---subHeaderData----define">' +
                      '<div class="' + show["status"] + '">' + show["status"] + '</div>' +
                      '<div class="SackReport-details--reflect---subHeaderData----define-----value">ID: <strong>' + show["id"] + '</strong></div>' +
                      '<div class="SackReport-details--reflect---subHeaderData----define-----value">Target: <strong>' + show["target"] + '</strong></div>' +
                      '<div class="SackReport-details--reflect---subHeaderData----define-----value">IP victim: <strong>' + show["ip"] + '</strong></div>' +
                      '<div class="SackReport-details--reflect---subHeaderData----define-----value">Requests: <strong>' + show["requests"] + '</strong></div>' +
                    '</div>' +
                  '</div>' +

                  '<div class="body">' +
                    '<div class="SackReport-details--dataShow">' +
                      '<h2 class="SackReport-details--dataShow---title">General information</h2>' +
                      '<ul>' +
                        '<div class="data"><strong>Operating System:</strong> ' + show["os"] + '</div>' +
                        '<div class="data" title="' + show["useragent"] + '"><strong>User agent:</strong> ' + show["useragent"] + '</div>' +
                        '<div class="data"><strong>Browser:</strong> ' + show["browser"] + ' ' + show["browserVersion"] + '</div>' +
                        '<div class="data"><strong>Ports:</strong> ' + show["ports"] + '</div>' +
                      '</ul>' +
                    '</div>' +

                    '<div class="SackReport-details--dataShow">' +
                      '<h2 class="SackReport-details--dataShow---title">Information of location</h2>' +
                      '<ul>'+
                        '<div class="data"><strong>ISP Name:</strong> ' + show["isp"] + '</div>' +
                        '<div class="data"><strong>Country:</strong> ' + show["country"] + '</div>' +
                        '<div class="data"><strong>City:</strong> ' + show["city"] + '</div>' +
                        '<div class="data"><strong>Latitude:</strong> ' + show["latitude"] + '</div>' +
                        '<div class="data"><strong>Longitude:</strong> ' + show["longitude"] + '</div>' +
                      '</ul>' +
                    '</div>' +

                  '</div>' +
                '</div>' +
              '</div>' +

            '</li>' +
          '</ul>';

          // preview data in console 
             Sack.log('Ip : ' + show["ip"] + ' | Date :' + show["date"]);
          return html;
    },

    showDetailsTwo: function(data) { 
      var show = {
        endpoint: data.endpoint,
        target: data.target,
        ip: data.ip,
        date: data.date,
        time: data.time,
        datapost: data.data,
      }

      html = '<div class="SackReport-details--Inspect">' +

                  '<div class="SackReport-details--Inspect---subHeaderData">' +
                    '<div class="SackReport-details--Inspect---subHeaderData----define">' +
                      '<div class="post">post</div>' +
                      '<div class="SackReport-details--Inspect---subHeaderData----define-----value">Endpoint: <strong>' + show["endpoint"] + '</strong></div>' +
                      '<div class="SackReport-details--Inspect---subHeaderData----define-----value">Target: <strong>' + show["target"] + '</strong></div>' +
                      '<div class="SackReport-details--Inspect---subHeaderData----define-----value">IP victim: <strong>' + show["ip"] + '</strong></div>' +
                      '<div class="SackReport-details--Inspect---subHeaderData----define-----value">Date: <strong>' + show["date"] + ' - ' + show["time"] + '</strong></div>' +
                    '</div>' +
                  '</div>' +

                  '<div class="body">' +
                    '<div class="SackReport-details--dataShowInspect">' +
                      '<ul>' +
                         show["datapost"] + 
                      '</ul>' +
                    '</div>' +

                  '</div>' +
                '</div>';

          return html;

    }
  };


  Sack.self.reflectVictims = function() {
      Sack.victims.get.pull();
    }; 

    // run functions
    Sack.deploy();



});




$( document ).ready(function() {
  

$("#status").load( "/stats", function( response, status, xhr ) {
var r = JSON.parse(xhr.responseText); 
    $( "#status" ).html( r.online);
});
$("#targets").load( "/stats", function( response, status, xhr ) {
var r = JSON.parse(xhr.responseText); 
    $( "#targets" ).html( r.targets);
});
$("#victims").load( "/stats", function( response, status, xhr ) {
var r = JSON.parse(xhr.responseText); 
    $( "#victims" ).html( r.victims);
});
$("#requests").load( "/stats", function( response, status, xhr ) {
var r = JSON.parse(xhr.responseText); 
    $( "#requests" ).html( r.requests);
});
$("#locations").load( "/stats", function( response, status, xhr ) {
var r = JSON.parse(xhr.responseText); 
    $( "#locations" ).html( r.locations);
});




});


