


jQuery(function ($) {
    $(document).ready(function () {
        $("#id_post").change(function () {

            $.ajax({
                url: "/blog/parent/"+$(this).val(),
                type: "GET",
                data: {},
                success: function (resp) {
                    console.log(resp);
                    
                    
                        let comment_list = '<option value="" selected="">---------</option>'
                        $.each(resp.data, function (i, item) {
                            
                            comment_list += '<option value="' + item.id + '"> Comments by ' + item.author+ '</option>'
                        });
                        $('#id_parent').html(comment_list);
                        


                },
                error: function (e) {
                    // when get link /blog/parent/
                    if(e.status == 404){
                        let comment_list = '<option value="" selected="">---------</option>'
                        $('#id_parent').html(comment_list);
                    }else{
                        console.error(JSON.stringify(e));
                    }

                    
                },
            });
        });
    });
});