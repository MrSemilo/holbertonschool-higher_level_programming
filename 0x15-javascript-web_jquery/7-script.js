$.get('https://swapi-api.hbtn.io/api/people/5/?format=json')
.done(function(json){
	$('#character').text(json.name)
});
