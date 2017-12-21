/*Handle Placeholder display*/

var food = ['boba', 'korean bbq', 'fast food', 'italian', 'chinese', 'french', 'tacos', 'ice cream'];
var locations = ['los angeles', 'new york', 'san francisco', 'boston', 'chicago', 'seattle', 'vancouver', 'orlando'];

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
}

var foodInt = food.length;
var locInt = locations.length;
var foodRand = getRandomInt(0, foodInt);
var locRand = getRandomInt(0, locInt);

document.getElementById('text').placeholder = food[foodRand];
document.getElementById('loc').placeholder = locations[locRand];

/*Handle Modal Clicks */

$("#aboutButton").click(function() {
  $(".modal").addClass("is-active");  
});

$(".modal-background").click(function() {
	$(".modal").removeClass("is-active");
});

$(".modal-close").click(function() {
   $(".modal").removeClass("is-active");
});
