$(document).ready(function(){
	$('.sidenav').sidenav();
	$('select').formSelect();
	M.updateTextFields();
	$('textarea#description').characterCounter();

	// innermargin = $(".inner").outerHeight(true) - $(".inner").height();
	mainheight = $(window).height() - $("header").height() - $("footer").height();
	$("main").css("min-height", mainheight)
});