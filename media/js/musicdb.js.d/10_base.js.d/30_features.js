/*global
  $
*/

$.extend({
  feature: function(body_class, callback) {
    InstantClick.on('change', function() {
      if ($('body').hasClass(body_class)) {
        callback();
      }
    });
  }
});
