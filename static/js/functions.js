$(document).ready(function(){

	$('.sidenav').sidenav();
	$('select').formSelect();
	M.updateTextFields();
	$('textarea#description').characterCounter();

	// innermargin = $(".inner").outerHeight(true) - $(".inner").height();
	mainheight = $(window).height() - $("header").height() - $("footer").height();
	$("main").css("min-height", mainheight)


	
	
	$('#sortselect').on('change', function() {
		selectvalue = $("#sortselect").val(); 
	    if (selectvalue == "meat"){
			$(".meat").css("display", "block");
			$(".fish, .sweets, .vegetarian").css("display", "none");
		};
		if (selectvalue == "fish"){
			$(".fish").css("display", "block");
			$(".meat, .sweets, .vegetarian").css("display", "none");
		};
		if (selectvalue == "vegetarian"){
			$(".vegetarian").css("display", "block");
			$(".fish, .sweets, .meat").css("display", "none");
		};
		if (selectvalue == "sweets"){
			$(".sweets").css("display", "block");
			$(".fish, .meat, .vegetarian").css("display", "none");
		};
		if (selectvalue == "all"){
			$(".fish, .sweets, .vegetarian, .meat").css("display", "block");
		};
	});
	

	$("#backbutton").on('click', function(){
		history.back();
	});

});