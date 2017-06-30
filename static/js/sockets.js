$(document).ready(function(){

var online_sckt = new WebSocket("ws://127.0.0.1:8000/online/");

online_sckt.onopen = function(){
                     var incoming_sckt = new WebSocket("ws://127.0.0.1:8000/incoming/");

                     incoming_sckt.onmessage = function(message){
                                               var in_msg = JSON.parse(message.data);
                                               $('<div id=received></div>').html(in_msg.msg).css({width: in_msg.wide + '%', marginLeft: in_msg.margin_shift}).appendTo('#chat_box');
                                               $('#chat_box').scrollTop($('#chat_box')[0].scrollHeight);
                                               }

                                    }




});