   
$.get('https://swapi-api.hbtn.io/api/films/?format=json')
.done(function(json){
	for( let js of json.results) {
	$('#list_movies').append(`<li> ${js.title} </li>`);
}});
