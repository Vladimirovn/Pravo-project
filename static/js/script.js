$('.captcha').click(function () {
    $.getJSON("/captcha/refresh/", function (result) {
        $('.captcha').attr('src', result['image_url']);
        $('#id_captcha_0').val(result['key'])
    });


});

function changeClass(first, second) {
    $(first).removeClass('show');
    $(second).addClass('show');
}

function changeColor(first, second) {
    $(first).css("background-color", '#DFDFDF');
    $(second).css("background-color", '#359EFF');
}


$('.next').click(function () {
    if ($('.first').hasClass('show')) {
        changeClass(".first", ".second");
        $('.back').css("opacity", '1');
        changeColor(".first_item", ".second_item");

    } else if ($('.second').hasClass('show')) {
        changeClass(".second", ".third");
        // $('.back').css("opacity", '1');
        changeColor(".second_item", ".third_item");
    } else if ($('.third').hasClass('show')) {
        changeClass(".third", ".forth");
        $('.next').css("opacity", '0');
        changeColor(".third_item", ".forth_item");
    }
});


$('.back').click(function () {
    if ($('.forth').hasClass('show')) {
        console.log("Hello");
        changeClass(".forth", ".third");
        $('.next').css("opacity", '1');
        changeColor(".forth_item", ".third_item");

    } else if ($('.third').hasClass('show')) {
        changeClass(".third", ".second");
        // $('.back').css("opacity", '1');
        changeColor(".third_item", ".second_item");
    } else if ($('.second').hasClass('show')) {
        changeClass(".second", ".first");
        $('.back').css("opacity", '0');
        changeColor(".second_item", ".first_item");
    }
});

$('.link').click(function () {
    $("html,body").stop().animate ({
        scrollTop: $("#mail_form").offset().top
    }, 20);
});

$('.sending_message').click(
    function () {
        document.location="http://pravonaadvokata.ru/";
    }
);