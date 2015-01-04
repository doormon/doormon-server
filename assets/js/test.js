$(document).ready(function() {
  $('#open').click(function() {
    $.ajax({
      method: 'POST',
      url: "/api/push/",
      data: {
        api_key: api_key,
        type: 'door',
        state: 'open'
      },
      success: function(data) {
      }
    });
  });
  $('#close').click(function() {
    $.ajax({
      method: 'POST',
      url: "/api/push/",
      data: {
        api_key: api_key,
        type: 'door',
        state: 'closed'
      },
      success: function(data) {
      }
    });
  });
});
