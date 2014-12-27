$.feature('f_base', function () {
  $(window).bind('scroll', function() {
    $('#header').toggleClass('navbar-fixed-top', ($(window).scrollTop() > 0));
  });
});
