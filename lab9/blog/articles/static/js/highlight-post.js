$(document).ready(function () {
    // --- Увеличение логотипа при наведении (ширина +20px, высота пропорционально) ---
    var $logo = $('.header img');
    
    function initLogoHover() {
        var w0 = parseInt($logo.css('width')) || 60;
        var h0 = parseInt($logo.css('height')) || 60;
        var ratio = h0 / w0;

        $('.header').hover(
            function () {
                $logo.stop(true).animate({
                    width: (w0 + 20) + "px",
                    height: ((w0 + 20) * ratio) + "px"
                }, 200);
            },
            function () {
                $logo.stop(true).animate({
                    width: w0 + "px",
                    height: h0 + "px"
                }, 200);
            }
        );
    }

    // если картинка уже загружена — сразу
    if ($logo[0] && $logo[0].complete) {
        initLogoHover();
    } else {
        $logo.on('load', initLogoHover);
    }
});
