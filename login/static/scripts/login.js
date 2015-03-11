$(document).ready(function(){
    $('#register').on('click', function(){
        $('#login-form').hide();
        $('#register-form').animate({height: "toggle",
                                     opacity: "toggle"}, "slow" || 1000);
    })
    $('#login').on('click', function(){
        $('#register-form').hide();
        $('#login-form').animate({height: "toggle",
                                  opacity: "toggle"}, "slow" || 1000);
    })
})
