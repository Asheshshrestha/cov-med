$(function () {

    "use strict";
         $('body').scrollspy({
        target: '#nav-part'
    });
    // for navbar background color when scrolling
    $(window).scroll(function () {
        var $scrolling = $(this).scrollTop();
        var bc2top = $("#back-top-btn");
        var stickytop = $(".navbar");
        if ($scrolling >= 160) {
            stickytop.addClass('sticky');
        } else {
            stickytop.removeClass('sticky');
        }
        if ($scrolling > 50) {
            bc2top.fadeIn(1000);
        } else {
            bc2top.fadeOut(1000);
        }
    });
    
    //==================Animated Scroll Start==================
   var nav = $('nav'),
        navOffset = nav.offset().top,
        $window = $(window);
    var html_body = $('html, body');
    $('nav a').on('click', function () {
        if (location.pathname.replace(/^\//, '') === this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                html_body.animate({
                    scrollTop: target.offset().top -80
                }, 1300);
                return false;
            }
        }
    });
    
    // Closes responsive menu when a scroll link is clicked
    $('.nav-link').on('click', function () {
        $('.navbar-collapse').collapse('hide');
    });
   
    //==================Animated Scroll End==================
  
	
    /* -------------------------------------
	         Back to top js				
	 	-------------------------------------- */
    var bc2top = $('#back-top-btn');
    bc2top.on('click', function () {
        html_body.animate({
            scrollTop: 0
        }, 1400);
    });    
    
  
    /* -------------------------------------
	          Preloader				
	 	-------------------------------------- */
    $('#preloader').delay(2500).fadeOut(1000);

    
/* -------------------------------------
	          Running slick js				
	 	-------------------------------------- */
    
    $('.slider').slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        swipeToSlide: true,
        fade: true,
        verticalSwiping: true,
        autoplaySpeed: 4300,
        arrows: false,
        dot: false,
       responsive: [
            {
                breakpoint: 600,
                settings: {
                    autoplaySpeed: 6200,
                    swipe: false,
                     swipeToSlide: false,
                    touchMove: false

                }
    }]
        
    });
    /* -------------------------------------
	          Testimonial slick js				
	 	-------------------------------------- */
    
    $('.test-inner').slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        swipeToSlide: true,
        fade: true,
        prevArrow: '<i class="fas fa-long-arrow-alt-left slidNext"></i>',
        nextArrow: '<i class="fas fa-long-arrow-alt-right slidprev"></i>',
        verticalSwiping: true,
        autoplaySpeed: 3200,
        arrows: true,
        responsive: [
            {
                breakpoint: 900,
                settings: {
                    arrows: false,
                    swipe: false,
                     swipeToSlide: false,
                    touchMove: false

                }
    },
            {
                breakpoint: 767,
                settings: {
                    arrows: true,
                    swipe: false,
                     swipeToSlide: false,
                    touchMove: false
                }
			}
        ]
        
    });
    /* -------------------------------------
	          Doctor slick js				
	 	-------------------------------------- */
    
    $('.doctor-slick').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        swipeToSlide: true,
        fade: false,
        verticalSwiping: true,
        autoplaySpeed: 3200,
        arrows: false,
        responsive: [
            {
                breakpoint: 800,
                settings: {
                   arrows: false,
                    autoplay: true,
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    swipeToSlide: false,
                    touchMove: false
                }
			},
            {
                breakpoint: 767,
                settings: {
                    fade: true,
                    autoplay: true,
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: false,
                    swipe: false,
                     swipeToSlide: false,
                    touchMove: false
                }
			}
		  ]
        
    });
    
/* -------------------------------------
	          Arraw				
	 	-------------------------------------- */
//    $(".test").click(function () {
//		$('html,body').animate({
//				scrollTop: $("#symptoms").offset().top - 80
//			},
//			2000);
//	});
//    $(".test-2").click(function () {
//		$('html,body').animate({
//				scrollTop: $("#doctors").offset().top - 80
//			},
//			2000);
//	});
//    $(".test-3").click(function () {
//		$('html,body').animate({
//				scrollTop: $("#doctors").offset().top - 80
//			},
//			2000);
//	});

    
  
    //==============Closes responsive menu when a scroll link is clicked End===========
    


});