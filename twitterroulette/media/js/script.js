/* Author: Chris Sinchok

*/

function tweet_submitted(data) {
    if('error' in data) {
        $("#twitter-submit-edit h2").html(data["error"]).css('color','red');
    } else {
        $("#twitter-submit-edit h2").html(data["message"]).css('color','black');
    }
}

function voted(data) {
    var vote_div = $('.submitted-bullet[rel="' + data['bullet_id'] + '"] > .roulette-text-submitted-vote');
    if(data['value'] == 1) {
        $(vote_div).find('.arrow-up').css("border-bottom", "30px solid green");
        $(vote_div).find('.arrow-down').css("border-top", "30px solid black");
    } else {
        $(vote_div).find('.arrow-up').css("border-bottom", "30px solid black");
        $(vote_div).find('.arrow-down').css("border-top", "30px solid green");
    }
    $(vote_div).find('.vote-count').html(data['total'])
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
  });
  
  $("#twitter-text-submit a").click(function(){
      var bullet = $("#roulette-tweet-box-editor").val();
      Dajaxice.roulette.submit_bullet(tweet_submitted, {'bullet': bullet});
      return false;
  });
  
  $('.arrow-up').click(function() {
      var bullet_id = $(this).parent('div.roulette-text-submitted-vote').parent('div.submitted-bullet').attr('rel');
      Dajaxice.roulette.vote(voted, {'bullet_id': bullet_id, 'value': 1});
  });
  
  $('.arrow-down').click(function() {
      var bullet_id = $(this).parent('div.roulette-text-submitted-vote').parent('div.submitted-bullet').attr('rel');
      Dajaxice.roulette.vote(voted, {'bullet_id': bullet_id, 'value': -1});
  });
});