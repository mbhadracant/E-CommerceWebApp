
    var onScroll = function() {
            var pos = $(window).scrollTop();

            $('#navbar-container').removeClass(function (index, css) {
                return (css.match(/(^|\s)bg-\S+/g) || []).join(' ');
            });

            $('#mobile-nav').removeClass(function (index, css) {
                return (css.match(/(^|\s)mobile-nav\S+/g) || []).join(' ');
            });

            $('.navbar-item > a, #nav-bars-toggle span').removeClass(function (index, css) {
                return (css.match(/(^|\s)color-\S+/g) || []).join(' ');
            });

            $('#logo a span').removeClass(function (index, css) {
                return (css.match(/(^|\s)logo-\S+/g) || []).join(' ');
            });

            $('.search-box').removeClass(function (index, css) {
                return (css.match(/(^|\s)search-box-\S+/g) || []).join(' ');
            });

            $('.search-box + label .search-icon').removeClass(function (index, css) {
                return (css.match(/(^|\s)search-box-icon\S+/g) || []).join(' ');
            });

            $('#nav-bars-toggle span').removeClass(function (index, css) {
                return (css.match(/(^|\s)navbar-toggle-\S+/g) || []).join(' ');
            });



            if (pos >= 50) {
                $('#navbar-container').addClass('bg-bottom');
                $('#mobile-nav').addClass('mobile-nav-bottom');
                $('.navbar-item > a').addClass('color-bottom');
                $('#logo a span').addClass('logo-bottom');
                $('.search-box').addClass('search-box-bottom');
                $('#nav-bars-toggle span').addClass('navbar-toggle-bottom');
                $('.search-box + label .search-icon').addClass('search-box-icon-bottom');
                if($('#shop:hover').length > 0) {
                    $('#shop > a').css("background","black");
                    $('#shop > a').css("color","white");
                    $('.dropdown-item').css("background", "black")
                    $('.dropdown-item').css("color","white");
                    $('.dropdown-nested').css("background", "black")
                } else {
                    $('#shop > a').css("color", "black");
                    $('#shop > a').css("background", "transparent");
                }

                $('#shop > a, .dropdown-content').hover(function (event) {
                    $("#shop > a, .dropdown-content > a").css("color", "white");
                    $("#shop > a").css("background", "black");
                    $('.dropdown-content > a').css("background", "black");
                    $('.dropdown-nested').css("background", "black");
                }, function () {
                    $('#shop > a, .dropdown-content > a').css("color", "black");
                    $('.dropdown-content > a').css("background", "none");
                    $('#shop > a').css("background", "transparent");
                });

                $('.dropdown-item').mouseenter(function (event) {
                    event.stopPropagation()
                    $('.dropdown-item').css("background","black");
                    $('.dropdown-item').css("color","white");
                    $('#shop > a').css("background","black");
                    $('#shop > a').css("color","white");
                    $(this).css("background", "rgb(60,60,60)");
                });
            }
            if (pos < 50) {
                $('#navbar-container').addClass('bg-top');
                $('#mobile-nav').addClass('mobile-nav-top');
                $('.navbar-item > a').addClass('color-top');
                $('#logo a span').addClass('logo-top');
                $('.search-box').addClass('search-box-top');
                $('#nav-bars-toggle span').addClass('navbar-toggle-top');
                $('.search-box + label .search-icon').addClass('search-box-icon-top');

                if($('#shop:hover').length > 0) {
                    $('.dropdown-item').css("background", "white")
                    $('.dropdown-item').css("color", "black")
                    $('#shop > a').css("color", "black");
                    $('#shop > a').css("background", "white");
                    $('.dropdown-nested').css("background", "white")

                } else {
                    $('#shop > a').css("color", "rgb(150,150,150)");
                    $('#shop > a').css("background", "transparent");
                }

                $('#shop > a, .dropdown-content').hover(function (event) {
                    $("#shop > a, .dropdown-content > a").css("color", "black");
                    $("#shop > a").css("background", "white");
                    $('.dropdown-content > a').css("background", "white")
                    $('.dropdown-nested').css("background", "white");
                }, function () {
                    $('#shop > a, .dropdown-content > a').css("color", "rgb(150,150,150)");
                    $('#shop > a').css("background", "transparent");
                    $('.dropdown-content > a').css("background", "white");
                });

                $('.dropdown-item').mouseenter(function (event) {
                    event.stopPropagation();
                    $('.dropdown-item').css("background","white");
                    $('.dropdown-item').css("color","black");
                    $('#shop > a').css("background","white");
                    $('#shop > a').css("color","black");
                    $(this).css("background", "rgb(235,235,235)");
                });

            }
        }

        var onResize = function() {
            var width = $(window).width();

            if(width < 950) {
                $('.navbar-item').not('#logo').hide();
                $('#nav-bars').show();
            } else {
                $('.navbar-item').not('#logo').show();
                 $('#nav-bars').hide();

                 if($('#mobile-nav').height() != 0 &&  !$('#mobile-nav').is(':animated')) {
                    $('#nav-bars').click();
                    if($(window).scrollTop() < 50) {
                        $('#navbar-container').addClass("bg-mobile-top");
                    } else {
                        $('#navbar-container').removeClass("bg-mobile-top");
                    }
                }
            }
        }

    $(document).ready(function () {

        onResize();
        onScroll();

        $( window ).resize(function() {
            onResize();
        });

        $(window).scroll(function () {
            onScroll();
        });


        $('#mobile-nav-content ul li[data-target]').click(function () {

            if(!$('.mobile-nav-current').is(':animated')) {
                if ($(this).hasClass("mobile-nav-greyed")) {

                    $('.mobile-nav-current').animate({
                        left: '100%',
                    }, 950);
                    $('.mobile-nav-previous').animate({
                        right: '0%',
                    }, 950);

                    $('.mobile-nav-previous').addClass("mobile-nav-current")
                    $('.mobile-nav-current').removeClass("mobile-nav-current")
                    $('.mobile-nav-previous').addClass("mobile-nav-current")
                } else {

                    $('.mobile-nav-current').animate({
                        right: '100%',
                    }, 950);

                    $('.mobile-nav-current').addClass("mobile-nav-previous");
                    $('.mobile-nav-current').removeClass("mobile-nav-current");
                    $('.mobile-nav-' + $(this).attr("data-target")).css("left", "100%");
                    $('.mobile-nav-' + $(this).attr("data-target")).show();

                    $('.mobile-nav-' + $(this).attr("data-target")).animate({
                        left: '0%',
                    }, 950);

                    $('.mobile-nav-' + $(this).attr("data-target")).addClass("mobile-nav-current");

                }
            }

        });


        $(".dropdown-item").hover(
            function (event) {
                 $('.dropdown-nested').stop();
                $('.dropdown-nested').animate({
                    width: '250px',
                }, 250);


            });


        $('#nav-bars').click(function() {

            if($('#mobile-nav').height() == 0) {
                 $("#nav-bars-toggle").toggleClass('open');
                $('#mobile-nav').animate({
                    height: '100%',
                }, 'slow');
                $('#mobile-nav-content').fadeIn();
                if($(window).scrollTop() < 50) {
                     $('#navbar-container').addClass("bg-mobile-top");
                }
                $('html, body').on('scroll touchmove mousewheel', function(e){
                  e.preventDefault();
                  e.stopPropagation();
                  return false;
                });
            }

            if($('#mobile-nav').height() != 0 &&  !$('#mobile-nav').is(':animated')) {
                $("#nav-bars-toggle").toggleClass('open');
                $('#mobile-nav').animate({
                    height: '0%',
                }, 'slow');
                $('#mobile-nav-content').fadeOut();
                $('html, body').off('scroll touchmove mousewheel');
                if($(window).scrollTop() < 50) {
                     $('#navbar-container').addClass("bg-top");
                     $('#navbar-container').removeClass("bg-mobile-top");
                }
            }
        });


        $(".dropdown-content").mouseleave(function (event) {
            $('.dropdown-nested').stop();
            $('.dropdown-nested').css("width", "0px");
        });


        $("#shop > a").mouseenter(function () {
            $('.dropdown-nested').stop();
            $('.dropdown-nested').css("width", "0px");
        });

    });