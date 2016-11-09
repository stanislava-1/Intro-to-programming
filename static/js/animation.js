// A car animation

$(document).ready(function(){
    $(".start").one('click', function(){
        $(".car").css('position', 'relative').animate({left: '+=80%'}, 'slow');
    });
    $(".back").click(function(){
        document.location.reload(true);     
    });
});