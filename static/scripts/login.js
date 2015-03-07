$('#login-btn').on("click",function(){
    fields = {
        username: $('#login-form').find('input[name="username"]').val(),
        password: $('#login-form').find('input[name="password"]').val()
    };
    $.ajax({
        type: "GET",
        url: "/user/login",
        dataType: "html",
        data: JSON.stringify(fields),
        success: function(html){
            if(html != 'wrong'){
                $('#login-bar').parent().html(html)
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
        type: "GET",
        url: "/user/register",
        dataType: "html",
        data: JSON.stringify(fields),
        success: function(html){
            if(html != 'wrong'){
                $('#login-bar').parent().html(html)
            }else{
                alert('Wrong password or nickname')
            }
        }
           })
});