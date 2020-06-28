$(window).scroll(function() {
    if ($(this).scrollTop() > 25) {
        $('.user-greeting').css({
            'display': 'none'
        });
    }
});

var log = function(s) {
    console.log(s);
};