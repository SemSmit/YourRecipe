$(document).ready(function(){
	$('.sidenav').sidenav();
	$('select').formSelect();
	M.updateTextFields();
	$('textarea#description').characterCounter();
});