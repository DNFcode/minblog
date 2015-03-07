$(document).ready(function(){
    $('#login-btn').on("click",function(){
        fields = {
            username: $('#login-form').find('input[name="username"]').val(),
            password: $('#login-form').find('input[name="password"]').val()
        };
        $.ajax({
            type: "POST",
            url: "/user/login/",
            dataType: "html",
            data: {data: JSON.stringify(fields)},
            success: function(html){
                if(html != 'wrong'){
                    $('#bar').html(html)
                }else{
                    alert('Wrong password or nickname')
                }
            }
               })
    });
    $('#register-btn').on("click", function(){
        fields = {
            username: $('#register-form').find('input[name="username"]').val(),
            password: $('#register-form').find('input[name="password"]').val(),
            first_name: $('#register-form').find('input[name="first_name"]').val(),
            second_name: $('#register-form').find('input[name="second_name"]').val(),
            email: $('#register-form').find('input[name="email"]').val()
        };
        $.ajax({
            type: "POST",
            url: "/user/register/",
            dataType: "html",
            data: {data: JSON.stringify(fields)},
            success: function(html){
                if(html != 'wrong'){
                    $('#bar').html(html)
                }else{
                    alert('Wrong password or nickname')
                }
            }
               })
    });
    $('#logout-btn').on("click", function(){
        $.ajax({
            type: "POST",
            url: "/user/logout/",
            dataType: "html",
            success: function(html){
                if(html != 'wrong'){
                    $('#bar').html(html)
                }else{
                    alert('Wrong password or nickname')
                }
            }
               })
    });
})
