// Параллакс эффект для шапки сайта с использованием jQuery
$(document).ready(function() {
    // Проверяем наличие элемента шапки
    if ($('.header').length > 0) {
        // Получаем высоту шапки для ограничения параллакса
        var headerHeight = $('.header').outerHeight();
        
        // Обработчик прокрутки страницы
        $(window).scroll(function() {
            // Получаем позицию прокрутки
            var scrollPosition = $(this).scrollTop();
            
            // Применяем параллакс эффект к элементам шапки
            $('.header-parallax').each(function() {
                var speed = $(this).data('speed') || 0.5;
                var yPos = -(scrollPosition * speed);
                $(this).css('background-position', '50% ' + yPos + 'px');
            });
            
            // Анимация элементов шапки при прокрутке
            $('.header-element').each(function() {
                var speed = $(this).data('speed') || 0.3;
                var yPos = -(scrollPosition * speed);
                $(this).css('transform', 'translateY(' + yPos + 'px)');
            });
        });
        
        // Инициализация при загрузке страницы
        $(window).trigger('scroll');
    }
    
    // Дополнительный эффект для фона шапки
    if ($('.hero-section').length > 0) {
        $('.hero-section').each(function() {
            var $this = $(this);
            var bgImage = $this.data('bg-image');
            
            if (bgImage) {
                $this.css('background-image', 'url(' + bgImage + ')');
            }
        });
    }
});

// Функция для инициализации параллакса на других элементах
function initParallax() {
    $('.parallax-element').each(function() {
        var $this = $(this);
        var speed = $this.data('speed') || 0.5;
        
        $(window).scroll(function() {
            var scrollPosition = $(window).scrollTop();
            var yPos = -(scrollPosition * speed);
            $this.css('background-position', '50% ' + yPos + 'px');
        });
    });
}

// Инициализация при загрузке
$(window).on('load', function() {
    initParallax();
});
