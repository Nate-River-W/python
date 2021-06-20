$(function(){
    $('.info-tabs__item').on('click', function (e) {
        e.preventDefault();
        
        $('.info-tabs__item').removeClass('info-tabs__item--active');
        $(this).addClass('info-tabs__item--active');
        
        $('.info-tabs__content').removeClass('info-tabs__content--active');
        $($(this).attr('href')).addClass('info-tabs__content--active')
    
    });

    $('.info-slider').slick({
        fade: true
    });

});