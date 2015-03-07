/**
 * Created by rigardi on 06.03.15.
 */
$(document).ready(function(){
    $('#article-save').on("click",function(){
        fields = {
            article_id: $('#article-id').text(),
            article_name: $('#article-name').val(),
            article_text: $('#article-text').val()
        };
        $.ajax({
            type: "POST",
            url: "/articles/save/",
            dataType: "text",
            data: {data: JSON.stringify(fields)},
            success: function(text){
                if(html == 'success'){
                    alert('success')
                }else{
                    alert('Wrong')
                }
            }
               })
    });
    $('.article-delete').on("click",function(){
        fields = {
            article_id: $(this).attr('article_id')//$(this).prevAll('.article-id:first').text()
        };
        $.ajax({
            type: "POST",
            url: "/articles/delete/",
            dataType: "text",
            data: {data: JSON.stringify(fields)},
            success: function(text){
                if(text == 'success'){
                    alert('success')
                }else{
                    alert('Wrong')
                }
            }
               })
    });
});