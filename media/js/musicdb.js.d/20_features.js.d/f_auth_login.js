$.feature('f_auth_login', function () {
  $('#id_username, #id_password')
    .filter(function() { return this.value === ''; })
    .eq(0)
    .focus()
    ;
});
