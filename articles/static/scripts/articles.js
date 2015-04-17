/**
 * Created by rigardi on 06.03.15.
 */
$(document).ready(function(){
    $('#wrongPass').collapse({'toggle': false});
    $('#wrongUsername').collapse({'toggle': false});

    $('#article-save').on("click",function(){
        var fields = {
            article_id: $('#article-id').text(),
            article_name: $('#article-name').val(),
            article_text: $('#article-text').val()
        };
        $.ajax({
            type: "POST",
            url: "/articles/save/",
            dataType: "html",
            data: {data: JSON.stringify(fields)},
            success: function(text){
                window.location
            }
       });
    });
    $('.article-delete').on("click",function(){
        var article_block = $(this).parents('.article');
        var fields = {
            article_id: $(this).attr('article_id')//$(this).prevAll('.article-id:first').text()
        };
        $.ajax({
            type: "POST",
            url: "/articles/delete/",
            dataType: "text",
            data: {data: JSON.stringify(fields)},
            success: function(text){
                if(text == 'success'){
                   article_block.hide();
                }else{
                    alert('Wrong')
                }
            }
               })
    });
    $('#register-btn').on("click", function(){
        $('#wrongUsername').collapse('hide');
        $('#wrongPass').collapse('hide');
        if($('#username-reg').val().length < 3){
            $('#wrongUsername').collapse('show');
        }else if($('#password-reg').val() != $('#password-repeat').val()){
            $('#wrongPass').collapse('show');
        }
        if($('#username-reg').val().length >= 3 & $('#password-reg').val() == $('#password-repeat').val()){
            $('#register-form').submit();
        }
    })
});