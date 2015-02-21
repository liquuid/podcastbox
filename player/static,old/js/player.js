var uid='1';

function getData(url) {

    $.ajax({

        url: url,
        success: function(status) {

            data = eval('('+status+')');
            alert(data);
        },
        error: function(status) {
            alert('eeee');
        }
    });
}


function Refresh() {

    $.ajax({

        url: '/feed_ws/' + id,
        success: function(status) {

            slices = eval('('+status+')');
            for (var i in slices){

                if ( slices[i]["is_active"] == true) {
                    setStatus('status',i,'<img src="/static/images/green-ball.png">')
                }
                else{
                    setStatus('status',i,'<img src="/static/images/red-ball.png">')
                }
                setStatus('status-tagar',i,slices[i]["tag_ar"])
                setStatus('status-wpver',i,slices[i]["wp_ver"])
            }
        },
        error: function() {
            setTimeout('loopRefresh()', 5000);
        }
    });


    setTimeout('loopRefresh()', 50000);
}



$(document).ready(function() {


});