$(document).ready(function() {
   var left = true;

   var months = new Array();
   months[0] = "January";
   months[1] = "February";
   months[2] = "March";
   months[3] = "April";
   months[4] = "May";
   months[5] = "June";
   months[6] = "July";
   months[7] = "August";
   months[8] = "September";
   months[9] = "October";
   months[10] = "November";
   months[11] = "December";

   var ws = new WebSocket('ws://duckit.margffoy-tuay.com/feed');
   ws.onmessage = function(str) {
       // console.log(str);
       var dom = '<div class="direct-chat-msg ';
       if(!left)
       {
           dom += ' right';
       }
       dom += '">';
       dom += '<div class="direct-chat-info clearfix">';
       dom += '<span class="direct-chat-name pull-';
       if(left)
       {
           dom += 'left">';
       }
       else
       {
           dom += 'right">';
       }

       dom += 'System</span>\n';
       dom += '<span class="direct-chat-timestamp pull-';
       if(left)
       {
           dom += 'right">';
       }
       else
       {
           dom += 'left">';
       }
       var date = new Date(str.timeStamp/1000);
       var days = date.getDay();
       var month = months[date.getMonth()];
       var hours = date.getHours();
       // Minutes part from the timestamp
       var minutes = "0" + date.getMinutes();
       // Seconds part from the timestamp
       var seconds = "0" + date.getSeconds();

       // Will display time in 10:30:23 format
       var formattedTime = days + ' ' + month + ' - ' + hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
       dom += ''+formattedTime+'</span></div>';
       dom += '<div class="direct-chat-text">';
       dom += str.data+'</div></div>';
       $('#chat-win').append(dom);
       left = !left;       
   }
});