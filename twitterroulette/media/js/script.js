/* Author: Chris Sinchok

*/

function tweet_submitted(data) {
    if('error' in data) {
        $("#twitter-submit-edit h2").html(data["error"]).css('color','red');
    } else {
        $("#twitter-submit-edit h2").html(data["message"]).css('color','black');
        // clear the text box
        $("#roulette-tweet-box-editor").val("");
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

function latest_fucked(bullets){
	console.log(bullets);
	var cloned_element = $('.submitted-bullet:hidden');
	var appendTo = $("#main");
	var bullet = undefined;
	for( bullet in bullets){
		var ohOkayIndex = bullets[bullet];
		var cloned = cloned_element.clone();
		cloned.removeClass("template");
		cloned.attr("rel",ohOkayIndex.pk);
		
		cloned.children(".roulette-text-submitted-vote").addClass("voted-" + "TBD");
		cloned.children(".roulette-text-submitted-author > span").html("submitted by <strong>@" + ohOkayIndex.fields.user +"</strong>");
		var img = cloned.children(".roulette-text-submitted-author > img");
		img.attr("src",img.attr("tmp") + "screen_name=" + ohOkayIndex.fields.user);
		img.attr("tmp","");
		
		cloned.appendTo(appendTo);
		cloned.show();
	}
}

$(document).ready(function(){
  Dajaxice.roulette.getfucked_latest_from(latest_fucked,{'from_id' : 0});
  
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
  
  setTimeout("$('div.error').fadeOut('slow');",4000);
  $('#countdown').countdown({until: new Date('{{this_round.round_end|date:"F j, Y G:i:s"}}'), compact: true, format: 'HMS', description: ''});
  
});