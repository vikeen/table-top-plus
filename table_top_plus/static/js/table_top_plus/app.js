$(document).ready(function () {
    $('.nav-tabs li a').click(function (e) {
        var $this = $(this);

        $this.parent().parent().find("li").removeClass("active")
        $this.parent().addClass('active');

        e.preventDefault();
    });
});