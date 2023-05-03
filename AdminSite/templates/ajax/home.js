$(document).ready(function(){
    mydata = {'pid': '1','csrfmiddlewaretoken': '{{ csrf_token }}'}
    mythis = this;
    $.ajax({
      url : "{% url 'index' %}",
          method : "POST",
          data : mydata,
          success : function(data){
            if(data.session == '1'){
              // Players
              $("#player").html('');
              $("#player").append(data.Player);
              if(data.Block_Player > 0){
                $("#block_player").html('');
                $("#block_player").append("<span class='text-danger text-sm font-weight-bolder'> </span>");
                $("#block_player span").append(data.Block_Player);
                $("#block_player").append(" Block Players");
              } else{
                $("#block_player").html('');
                $("#block_player").append("<span class='text-danger text-sm font-weight-bolder'> &nbsp; </span>");
              }
              
              // Drills              
              $("#active_drill").html('');
              $("#active_drill").append(data.drill_active);
              if(data.drill_block > 0){
                $("#block_drill").html('');
                $("#block_drill").append("<span class='text-danger text-sm font-weight-bolder'> </span>");
                $("#block_drill span").append(data.drill_block);
                $("#block_drill").append(" Deactivated Drills");
              } else{
                $("#block_drill").html('');
                $("#block_drill").append("<span class='text-danger text-sm font-weight-bolder'> &nbsp; </span>");
              }
              // Requestes
              $("#new_req").html('');
              $("#new_req").append(data.New_req);

              // Static
              $("#active_post").html('')
              $("#active_post").append(data.Post_active)
              if(data.Post_block > 0){
                $("#block_post").html('');
                $("#block_post").append("<span class='text-danger text-sm font-weight-bolder'> </span>");
                $("#block_post span").append(data.Post_block);
                $("#block_post").append(" Deactivated Static Pages");
              } else{
                $("#block_post").html('');
                $("#block_post").append("<span class='text-danger text-sm font-weight-bolder'> &nbsp; </span>");
              }
              var refreshIntervalId = setInterval(ajaxCall, 1000);
            } else {
              url = "{% url 'login' %}"
              window.location.assign(url);
            }
          },
          error : function(data){
            url = "{% url 'login' %}"
            window.location.assign(url);
          },
    });
  });

function ajaxCall() {
    $.ajax({
      url : "{% url 'index' %}",
          method : "POST",
          data : mydata,
          success : function(data){
            if(data.session == '1'){
              // Players
              $("#player").html('');
              $("#player").append(data.Player);
              if(data.Block_Player > 0){
                $("#block_player").html('');
                $("#block_player").append("<span class='text-danger text-sm font-weight-bolder'> </span>");
                $("#block_player span").append(data.Block_Player);
                $("#block_player").append(" Block Players");
              } else{
                $("#block_player").html('');
                $("#block_player").append("<span class='text-danger text-sm font-weight-bolder'> &nbsp; </span>");
              }
              
              // Drills              
              $("#active_drill").html('');
              $("#active_drill").append(data.drill_active);
              if(data.drill_block > 0){
                $("#block_drill").html('');
                $("#block_drill").append("<span class='text-danger text-sm font-weight-bolder'> </span>");
                $("#block_drill span").append(data.drill_block);
                $("#block_drill").append(" Deactivated Drills");
              } else{
                $("#block_drill").html('');
                $("#block_drill").append("<span class='text-danger text-sm font-weight-bolder'> &nbsp; </span>");
              }
              // Requestes
              $("#new_req").html('');
              $("#new_req").append(data.New_req);
              
              // Static
              $("#active_post").html('')
              $("#active_post").append(data.Post_active)
              if(data.Post_block > 0){
                $("#block_post").html('');
                $("#block_post").append("<span class='text-danger text-sm font-weight-bolder'> </span>");
                $("#block_post span").append(data.Post_block);
                $("#block_post").append(" Deactivated Static Pages");
              } else{
                $("#block_post").html('');
                $("#block_post").append("<span class='text-danger text-sm font-weight-bolder'> &nbsp; </span>");
              }
            } else {
              url = "{% url 'login' %}"
              window.location.assign(url);
            }
          },
          error : function(data){
            url = "{% url 'login' %}"
            window.location.assign(url);
          },
    });
}