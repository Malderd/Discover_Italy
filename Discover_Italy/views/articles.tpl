% rebase('layout.tpl', title=title)  


<link rel="stylesheet" href="/static/content/style_articles.css">

<div class="background-overlay"></div>

<div class="article-page">
    
    <!-- ЗАГОЛОВКИ СТРАНИЦЫ -->
    <big><h1 class="article-front">Интересные статьи</h1></big>
    <big><h4 class="article-front">Пишите интересные статьи, делитесь впечатлениями и интересными местами</h4></big>

    <!-- ДВЕ КОЛОНКИ: форма (справа) + карусель статей (слева) -->
    <div class="two-columns">
        
        <!-- ПРАВАЯ КОЛОНКА: ФОРМА ДОБАВЛЕНИЯ СТАТЬИ -->
        <div class="form-column">
            <div class="menu-container">
               
                <form action="/articles" method="post" class="article-form">
                    
                    <!-- ПОЛЕ: Автор статьи -->
                    <p>
                        <!-- Поле ввода текста. value="{{old.get('author', '')}}" сохраняет введённое значение после отправки -->
                        <input type="text" name="author" placeholder="Автор"
                               value="{{old.get('author', '')}}"
                               class="form-control % if field_errors.get('author'): input-error % end">
                        <!-- Если есть ошибка для поля 'author' - выводим сообщение об ошибке -->
                        % if field_errors.get('author'):
                            <br><span class="field-error">{{field_errors['author']}}</span>
                        % end
                    </p>
                    
                    <!-- ПОЛЕ: Заголовок статьи -->
                    <p>
                        <input type="text" name="title" placeholder="Заголовок"
                               value="{{old.get('title', '')}}"
                               class="form-control % if field_errors.get('title'): input-error % end">
                        % if field_errors.get('title'):
                            <br><span class="field-error">{{field_errors['title']}}</span>
                        % end
                    </p>
                    
                    <!-- ПОЛЕ: Текст статьи  -->
                    <p>
                        <textarea name="content" placeholder="Текст статьи"
                                  class="form-control % if field_errors.get('content'): input-error % end">{{old.get('content', '')}}</textarea>
                        % if field_errors.get('content'):
                            <br><span class="field-error">{{field_errors['content']}}</span>
                        % end
                    </p>
                    
                    <p>
                        <input type="date" name="date"
                               value="{{old.get('date', '')}}"
                               class="form-control % if field_errors.get('date'): input-error % end">
                        % if field_errors.get('date'):
                            <br><span class="field-error">{{field_errors['date']}}</span>
                        % end
                    </p>
                    
                    <!-- КНОПКА ОТПРАВКИ ФОРМЫ -->
                    <p>
                        <button type="submit">Добавить</button>
                    </p>
                </form>
            </div>
        </div>

        <!-- ЛЕВАЯ КОЛОНКА: КАРУСЕЛЬ СТАТЕЙ -->
        <div class="carousel-column">
            % if articles:
            <div class="carousel-wrapper">
                <!-- Кнопка "влево" для прокрутки карусели -->
                <button class="arrow-btn" onclick="move(-1)">&#10094;</button>
                
                <!-- Контейнер карусели (область, в которой видна одна статья) -->
                <div class="carousel-container">
                    <!-- Трек карусели (все статьи, которые прокручиваются) -->
                    <div class="carousel-track" id="track">
                        <!-- Цикл по всем статьям: выводим каждую как отдельную карточку -->
                        % for a in articles:
                        <div class="card-item">
                            <h3><b>{{a['title']}}</b></h3>                      
                            <big><big><b>{{a['author']}}</b></big></big> 
                            <p>{{a['content']}}</p>                       
                            <small>{{a['date']}}</small>                  
                        </div>
                        % end
                    </div>
                </div>
                
                <!-- Кнопка "вправо" для прокрутки карусели -->
                <button class="arrow-btn" onclick="move(1)">&#10095;</button>
            </div>
            % else:
            <div class="empty-message">
                <p>Пока нет статей</p>
                <p>Добавьте первую статью!</p>
            </div>
            % end
        </div>
        
    </div>
</div>

<!-- Логика работы карусели -->
<script>
// Текущий индекс (какая статья сейчас видна)
let currentIndex = 0;

// Ссылки на элементы DOM
let track = null;      // контейнер-трек с карточками статей
let items = [];        // массив карточек (дочерних элементов трека)

// Функция обновления положения карусели (сдвигает трек)
function updateCarousel() {
    if (!track || items.length === 0) return;          // если нет элементов - выходим
    const width = items[0].offsetWidth;                // ширина одной карточки
    track.style.transform = `translateX(-${currentIndex * width}px)`;  // сдвигаем трек
}

// Функция перемещения карусели (direction: -1 - влево, 1 - вправо)
function move(direction) {
    if (!items.length) return;                         // если нет статей - выходим
    
    // Меняем индекс с учётом направления
    currentIndex += direction;
    
    // БЕСКОНЕЧНАЯ КАРУСЕЛЬ (зацикливание)
    if (currentIndex < 0) {
        currentIndex = items.length - 1;               // если ушли влево за первую - идём к последней
    } else if (currentIndex >= items.length) {
        currentIndex = 0;                              // если ушли вправо за последнюю - идём к первой
    }
    
    updateCarousel();                                  // применяем новый сдвиг
}

// При полной загрузке страницы инициализируем карусель
window.addEventListener('load', function() {
    track = document.getElementById('track');          // находим элемент трека
    if (track) {
        items = Array.from(track.children);            // получаем все карточки статей
        window.addEventListener('resize', updateCarousel);  // при изменении размера окна пересчитываем
        updateCarousel();                              // первоначальная установка позиции
    }
});
</script>