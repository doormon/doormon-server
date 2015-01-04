$(document).ready(function() {
  $('#open').click(function() {
    $.ajax({
      method: 'POST',
      url: "/api/push/",
      data: {
        api_key: api_key,
        type: 'door',
        state: 'open',
        video_uri: 'http://195.235.198.107:3346/axis-cgi/mjpg/video.cgi?resolution=320x240'
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
        state: 'closed',
        video_uri: 'http://195.235.198.107:3346/axis-cgi/mjpg/video.cgi?resolution=320x240'
      },
      success: function(data) {
      }
    });
  });
});
