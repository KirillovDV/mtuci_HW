// Функция для сворачивания/разворачивания статей
function initFoldButtons() {
    // Находим все кнопки сворачивания
    const foldButtons = document.querySelectorAll('.fold-button');
    
    foldButtons.forEach(button => {
        // Получаем родительский элемент статьи
        const articleContainer = button.closest('.one-post');
        if (!articleContainer) return;

        const articleText = articleContainer.querySelector('.article-text');
        if (!articleText) return;

        const articleAuthor = articleContainer.querySelector('.article-author');
        const articleDate = articleContainer.querySelector('.article-created-date');
        
        // Чтобы не навешивать обработчик повторно
        if (button.dataset.listenerAdded === 'true') return;
        button.dataset.listenerAdded = 'true';

        button.addEventListener('click', function (e) {
            const isFolded = button.dataset.folded === 'true';
            
            if (isFolded) {
                // Разворачиваем
                articleText.style.display = 'block';
                articleAuthor.style.display = 'block';
                articleDate.style.display = 'block';
                button.textContent = 'Свернуть';
                button.dataset.folded = 'false';
            } else {
                // Сворачиваем
                articleText.style.display = 'none';
                articleAuthor.style.display = 'none';
                articleDate.style.display = 'none';
                button.textContent = 'Развернуть';
                button.dataset.folded = 'true';
            }
        });
    });
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function () {
    initFoldButtons();
});
