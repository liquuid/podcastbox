var teste = null;
var feeds = null;
var episodes = null;
var playlist = null;
var audio = null;
var current_episode = 0; 

function playerStatus(){
    //audio = document.getElementById("audio-player");
    document.getElementById("audio-player").addEventListener("ended", function() {
        console.log("acabou!!!");
        NextEpisode();
    });

    //setTimeout('playerStatus()', 5000);
}

function getCurTime(){
    console.log(document.getElementById("audio-player").currentTime);
    setTimeout('getCurTime()', 30000);
}

function getData() {
    $.ajax({

        url: '/episodes_tl_ws/',
        success: function(status) {

            episodes = eval('('+status+')');
            console.log(episodes);

           $.ajax({

                url: '/episodes_playlist/',
                success: function(status) {

                    playlist = eval('('+status+')');

                    $.ajax({

                        url: '/feed_ws/',
                        success: function(status) {

                            feeds = eval('('+status+')');
                            //console.log(feeds);
                            a = new PopulateList();
                            a.draw();
                            getCurTime();
                            //playerStatus();


                        },
                        error: function() {
                            setTimeout('loopRefresh()', 50000);
                        }
                    });


                },
                error: function() {
                    setTimeout('loopRefresh()', 50000);
                }
            });




        },
        error: function() {
            setTimeout('loopRefresh()', 50000);
        }
    });

    

}

function Episode(data){
    this.id = data.id;
    this.feed_id = data.feed_id;
    this.updated = data.updated;
    this.title = data.title;
    this.url = data.url;
    this.summary = data.summary;
 
    this.clicked = function() {
        current_episode = this.id
        console.log("clicked " + current_episode);
    
        $("#podcast-title").html(this.title);
        $("#summary").html(this.summary);
        $("#channel").html(feeds[this.feed_id].title);
        //console.log(feeds[this.feed_id].title);
        $("#date").html(this.updated);
        //console.log(this.updated);
        $("#player").html('<audio controls id="audio-player"> <source src="' + this.url + '" type="audio/mpeg">Your browser does not support the audio element.</audio>');
        //$("#player").html('<audio controls id="audio-player"> <source src="/static/19 Level Complete.mp3" type="audio/mpeg">Your browser does not support the audio element.</audio>');
        playerStatus();
    }
    
}

function EpisodeItem(episode){

    this.html = '<div id="episode-'+episode.id+ '" class="email-item pure-g">'+
                            '<div class="pure-u">' +
                                '<img class="email-avatar" alt="icone rss generico" height="64" width="64" src="/static/img/rss.png">' + 
                            '</div>'+
                            '<div class="pure-u-3-4">'+
                                '<h5 class="email-name">' + feeds[episode.feed_id].title + '</h5>'+
                                '<h4 class="email-subject">' + episode.title + '</h4>'+
                                '<p class="email-desc"></p>'+ 
                            '</div>'+
                        '</div>'
    
}

function NextEpisode(){
    new_id = playlist[playlist.indexOf(parseInt(current_episode)) + 1];
    current_episode = new_id;
    
    $("[id^=episode-").removeClass("email-item-selected");
    $("#episode-" + new_id).addClass("email-item-selected");
    episode = new Episode(episodes[new_id]);
    episode.clicked();
    document.getElementById("audio-player").autoplay = true;
    document.getElementById("audio-player").load();
    document.getElementById("audio-player").addEventListener("ended", function() {
        console.log("acabou!!!");
        NextEpisode();
    });
    //audio.play();

}
function PopulateList(){
    
    this.draw = function() {
        if ( episodes && feeds ){ 
            list = '';
            // Isso aqui faz o primeiro episodio da lista comecar ativado
            for ( i in playlist) {

                episode = new Episode(episodes[playlist[i]]);
                episode.clicked();
                break;
            }
            for (i in playlist ){
                item = new EpisodeItem(episodes[playlist[i]]);
                list += item.html;
                //console.log(episode)
            }
            $("#list").html(list);
            // Isso aqui faz o primeiro episodio da lista comecar selecionado
    
            $("#episode-" + playlist[0]).addClass("email-item-selected");

            $("[id^=episode-").click( function() {
                $("[id^=episode-").removeClass("email-item-selected");
                $("#" + this.id).addClass("email-item-selected");
                episode = new Episode(episodes[this.id.split("-")[1]]);
                episode.clicked();
            });


            
        }
        else {
            console.log(episodes);
            console.log(feeds);
            console.log("erro de ajax");
        }
    }
}
getData();

