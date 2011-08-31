/* Author: Chris Sinchok

*/

function tweet_submitted(data) {
    if('error' in data) {
        $("#twitter-submit-edit h2").html(data["error"]).css('color','red');
    } else {
        $("#twitter-submit-edit h2").html(data["message"]).css('color','black');
    }
}

$(document).ready(function(){
  $("#roulette-tweet-box-editor").keyup(function() {
      var chars_left = 140 - $(this).val().length;
      $("#characters-remaining").html(chars_left);
      if(chars_left < 0) {
          $("#characters-remaining").css('color', 'red');
      } else {
          $("#characters-remaining").css('color', 'black');
      }
  })
  
  $("#twitter-text-submit a").click(function(){
      var bullet = $("#roulette-tweet-box-editor").text();
      Dajaxice.roulette.submit_bullet(tweet_submitted, bullet);
      return false;
  })  
});