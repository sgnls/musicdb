$.feature('f_base', function () {
  var fixUnfixNavbar = function() {
    var toggle = ($(window).scrollTop() > 0);

    $('body').toggleClass('f_fixed_top', toggle);
    $('#header').toggleClass('navbar-fixed-top', toggle);
  };

  $(window).bind('scroll', function() {
    fixUnfixNavbar();
    return true;
  });

  fixUnfixNavbar();
});
