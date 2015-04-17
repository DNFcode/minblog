/**
 * Created by dnf on 17.04.15.
 */
$(document).ready(function(){
    $('.comment-hider').on('click', function(){
        if($(this).next('.comments-block').is(":visible")){
            $(this).next('.comments-block').hide();
        }else{
            if($(this).attr('loaded')=='true') {
                $(this).next('.comments-block').show();
            }else{
                var id = $(this).parents('.article').attr('articleid');
                var $t = $(this)
                $.ajax({
                    method: "GET",
                    url: "/comments/"+id+"/",
                    dataType: "html",
                    success: function(data){
                        $t.next('.comments-block').children('.comments').html(data);
                        $t.next('.comments-block').show();
                        $t.attr('loaded', 'true');
                    }
                })
            }
        }
    });
    $('.save-comment').on('click', function(){
        var fields = {
            comment_text:$(this).prev('.comment-new-area').val(),
            article_id:parseInt($(this).parents('.article').attr('articleid'))
        };
        $.ajax({
            method: "POST",
            url: "/comments/save/",
            data:{data: JSON.stringify(fields)}
        });
        var id = $(this).parents('.article').attr('articleid');
        var $t = $(this).parents('.comments-block').prev('.comment-hider');
        $.ajax({
            method: "GET",
            url: "/comments/"+id+"/",
            dataType: "html",
            success: function(data){
                $t.next('.comments-block').children('.comments').html(data);
                $t.next('.comments-block').show();
                $t.attr('loaded', 'true');
            }
        })
    });
    $('.comments').on('click', '.comment-delete', function(){
        var id = $(this).parent().attr('commentid');
        var $t = $(this).parent();
        $.ajax({
            method: "POST",
            url: "/comments/delete/"+id+"/",
            success: function(data){
                $t.remove();
            }
        })
    });
    setInterval(function(){
        $('.comments-block').each(function(){
            if($(this).is(':visible')){
                var $t = $(this).children('.comments');
                var comment_id = $(this).children('.comments').children(':last').attr('commentid');
                var article_id = $(this).parents('.article').attr('articleid');
                var fields = {
                    comment_id:parseInt(comment_id),
                    article_id:parseInt(article_id)
                }
                $.ajax({
                    method: "POST",
                    url: "/comments/update/",
                    data:{data: JSON.stringify(fields)},
                    dataType: "html",
                    success: function(data){
                        $t.html($t.html()+data);
                    }
                })
            }
        })
    }, 5000)
});
