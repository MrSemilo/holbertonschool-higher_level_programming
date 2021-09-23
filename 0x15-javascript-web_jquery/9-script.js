$.get('https://fourtonfish.com/hellosalut/?lang=fr')
.done(function(json){
	$('#hello').text(json.hello);
});
