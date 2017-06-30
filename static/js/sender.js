$(document).ready(function(){
$('#chat_box').scrollTop($('#chat_box')[0].scrollHeight);
$('#toss_btn').click(function(){
var contents = $('#input').val();
var wide = contents.length;
var ctoken = $('input[name=csrfmiddlewaretoken]').val();
var receiver = $('#receiver').val();

function how_wide(wide){
            if (wide < 14){return 13;}
            if (wide > 13 && wide < 56){return wide;}
            if (wide > 55){return 56;}}

$.ajax({ url:'/',
        method: 'POST',
        cache: false,
        data:{'csrfmiddlewaretoken':ctoken,'toss':contents,'receiver': receiver, 'wide': how_wide(wide)},
        success: function(){$('<div id="sender"></div>').html(contents).width(how_wide(wide)+'%').appendTo('#chat_box');
                            $('#input').val('');
                            $('#chat_box').scrollTop($('#chat_box')[0].scrollHeight);}   });

         });

});