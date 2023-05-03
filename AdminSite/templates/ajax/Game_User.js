$('tbody').on('click','.check-blocks',function(){
    var id = $(this).attr('data-sid');
    mydata = {pid:id, 'csrfmiddlewaretoken': '{{ csrf_token }}'}
    mythis = this;
    $.ajax({
        url : "{% url 'Game_User_Block' %}",
        method : "POST",
        data : mydata,
        success : function(data){
            if (data.status==1){
                $('#check'+id).html('');
                // $('#errormsg').append("<div class='alert alert-danger' id='pass"+id+"'>"+ data.driver +"</div>")
                $('#check'+id).append("<div class='onoffswitch'><input type='checkbox' name='onoffswitch' data-sid='" +id+ "' class='check-blocks onoffswitch-checkbox' id='myonoffswitch"+id+"'><label class='onoffswitch-label' for='myonoffswitch"+id+"'><div class='onoffswitch-inner'></div><div class='onoffswitch-switch'></div></label></div>");
            }
            if (data.status==2){
                $('#check'+id).html('');
                // $('#errormsg').append("<div class='alert alert-success' id='pass"+id+"'>"+ data.driver +"</div>")
                $('#check'+id).append("<div class='onoffswitch'><input type='checkbox' name='onoffswitch' data-sid='" +id+ "' class='check-blocks onoffswitch-checkbox' id='myonoffswitch"+id+"' checked><label class='onoffswitch-label' for='myonoffswitch"+id+"'><div class='onoffswitch-inner'></div><div class='onoffswitch-switch'></div></label></div>"); 
            }
            if (data.status==0){
                // console.log("Unable To Delete User")
            }
        },
    });
});

$(document).on('click', '#link', function(e) {
    var href = $(this).attr('href');
    console.log('passs click button',href);
    swal({
    title: "Are you sure?", 
    // text: "You will be redirected to "+ href, 
    type: "warning",
    confirmButtonText: "Delete",
    showCancelButton: true
    })
      .then((result) => {
      if (result.value) {
          window.location = href;
      } else if (result.dismiss === 'cancel') {
          swal(
            'Cancelled',
            '',
            'error',
          )
          // swal(
          //   'Cancelled',
          //   'Your stay here :)',
          //   'error'
          // )
      }
    })
});