/**
 * Created by mykola.dekhtiarenko on 30.03.17.
 */
$(document).ready(function () {

    $('.form').find('input, textarea').on('keyup blur focus change', function (e) {

        var $this = $(this),
            label = $this.prev('label');

        if (e.type === 'keyup') {
            if ($this.val() === '') {
                label.removeClass('active highlight');
            } else {
                label.addClass('active highlight');
            }
        } else if (e.type === 'blur') {
            if ($this.val() === '') {
                label.removeClass('active highlight');
            } else {
                label.removeClass('highlight');
            }
        } else if (e.type === 'focus') {

            if ($this.val() === '') {
                label.removeClass('highlight');
            }
            else if ($this.val() !== '') {
                label.addClass('highlight');
            }
        } else if (e.type === 'change') {
            if ($("#login-label") !== '') {
                $("#login-label").addClass(' active highlight');
            }
             if ($("#password-label") !== '') {
                $("#password-label").addClass(' active highlight');
            }
        }

    });

    $('.tab a').on('click', function (e) {

        e.preventDefault();

        $(this).parent().addClass('active');
        $(this).parent().siblings().removeClass('active');

        target = $(this).attr('href');

        $('.tab-content > div').not(target).hide();

        $(target).fadeIn(600);

    });

    $("#register").on('click', function () {
       registerOnClick();
    });
});

