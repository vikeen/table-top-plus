$(document).ready(function () {
    "use strict";

    window.tableTopPlus = new TableTopPlus();
});

window.TableTopPlus = function () {
    this.setupTabNavigation();
};

TableTopPlus.prototype.setupTabNavigation = function () {
    $('.nav-tabs li a').click(function (e) {
        var $this = $(this);

        $this.parent().parent().find("li").removeClass("active")
        $this.parent().addClass('active');

        e.preventDefault();
    });
};


TableTopPlus.prototype.renderPdfPage = function (pageNum) {
    var pageRendering = false,
        pageNumPending = null,
        scale = 1.3,
        canvas = document.getElementById('the-canvas'),
        ctx = canvas.getContext('2d');

    PDFJS.getDocument('/static/characters/images/dnd-5e-character-sheet_' + pageNum + '.pdf').then(function (pdf) {
        pageRendering = true;

        pdf.getPage(1).then(function (page) {
            var viewport = page.getViewport(scale);

            canvas.height = viewport.height;
            canvas.width = viewport.width;

            var renderContext = {
                canvasContext: ctx,
                viewport: viewport
            };
            var renderTask = page.render(renderContext);
            // Wait for rendering to finish
            renderTask.promise.then(function () {
                pageRendering = false;
                if (pageNumPending !== null) {
                    // New page rendering is pending
                    renderPage(pageNumPending);
                    pageNumPending = null;
                }
            });
        });
    });
};
