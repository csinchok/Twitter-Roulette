
var last_max_fucked = 0;

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
	if(bullets.error != undefined){
		return false;
	}
	var cloned_element = $('.submitted-bullet:hidden');
	var appendTo = $("#main");
	var bullet = undefined;
	for( bullet in bullets){
		var ohOkayIndex = bullets[bullet];
		var cloned = cloned_element.clone();
		
		cloned.removeClass("template");
		cloned.attr("rel",ohOkayIndex.pk);
		
		cloned.children(".roulette-text-submitted-vote").addClass("voted-" + ohOkayIndex.score);
		
		// add the vote between the arrows
		var vodeSection = cloned.children(".roulette-text-submitted-vote").children(":nth-child(2)");
		vodeSection.html(ohOkayIndex.score);
		
		// add the usser name in the span
		var firstSpan = cloned.children(":nth-child(3)").children(":first-child");
		firstSpan.html("submitted by <strong>@" + ohOkayIndex.user +"</strong> on " + ohOkayIndex.date_submitted);
		
		// update the image with the user name
		var secondImg = cloned.children(":nth-child(3)").children(":nth-child(2)");
		secondImg.attr("src",secondImg.attr("tmp") + "&screen_name=" + ohOkayIndex.user);
		secondImg.attr("tmp","");

		// add the tweet text
		cloned.children(".roulette-text-submitted").html(ohOkayIndex.tweet);
		
		cloned.prependTo(appendTo);
		cloned.fadeIn('slow');
		
		if (ohOkayIndex.pk > last_max_fucked) { last_max_fucked = ohOkayIndex.pk; }
	}
}

function check_cherry_and_guide(){
	var cherry_popped = $.cookie('cherry_popped');
	if( cherry_popped == undefined ){
		guiders.createGuider({
			buttons: [{name: "Close"},{name: "Next"}],
			description: "Welcome to social roulette, it looks like this is your first time here, so let us explain how this works. Click next for the guided tour, or close to quit and get started.",
			id: "first",
			next: "second",
			overlay: true,
			title: "Welcome to social roulette!"
		}).show();
		
		guiders.createGuider({
			attachTo: "#twitter-submit-edit",
			buttons: [{name: "Close"}],
			description: "Load a bullet into the gun, this is your one chance per game, so  make it good.",
			id: "second",
			position: 9,
			title: "Step 1: Load a bullet"
		});
		
		$.cookie('cherry_popped',true, {expires : 365} );
	}
}

$(document).ready(function(){
  check_cherry_and_guide();

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
  
  $('.arrow-up').live('click',function() {
      var bullet_id = $(this).parent('div.roulette-text-submitted-vote').parent('div.submitted-bullet').attr('rel');
      Dajaxice.roulette.vote(voted, {'bullet_id': bullet_id, 'value': 1});
  });
  
  $('.arrow-down').live('click',function() {
      var bullet_id = $(this).parent('div.roulette-text-submitted-vote').parent('div.submitted-bullet').attr('rel');
      Dajaxice.roulette.vote(voted, {'bullet_id': bullet_id, 'value': -1});
  });
  
  // fade out the error container if it exists
  setTimeout("$('div.error').fadeOut('slow');",4000);
  // fade in the new elements
  setInterval("Dajaxice.roulette.getfucked_latest_from(latest_fucked,{'from_id' : last_max_fucked});",10000);
  
});