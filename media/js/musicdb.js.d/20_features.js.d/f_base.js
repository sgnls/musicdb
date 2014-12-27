$.feature('f_base', function () {
  var fixUnfixNavbar = function() {
    $('#header').toggleClass(
      'navbar-fixed-top',
      ($(window).scrollTop() > 0)
    );
  };

  $(window).bind('scroll', function() {
    fixUnfixNavbar();
    return true;
  });

  fixUnfixNavbar();
});
