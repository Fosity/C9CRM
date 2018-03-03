$('.rbac_head').click(function () {
    $(this).parent().addClass('active').siblings().removeClass('active').find('ul').removeClass('in').attr('aria-expanded', 'false');
    if ($(this).attr('aria-expanded') == 'true') {
        $(this).next().removeClass('in');
        $(this).parent().removeClass('active');
        $(this).attr('aria-expanded', 'false').next().attr('aria-expanded', 'false')
    } else {
        $(this).next().addClass('in');
        $(this).parent().addClass('active');
        $(this).attr('aria-expanded', 'true').next().attr('aria-expanded', 'true')
    }
    // $(this).next().toggleClass('in');
    // $(this).parent().removeClass('active');
    // $(this).attr('aria-expanded','false').next().attr('aria-expanded','false');
});
