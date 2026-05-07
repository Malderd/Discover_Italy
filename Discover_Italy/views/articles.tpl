% rebase('layout.tpl', title=title)

<link rel="stylesheet" href="/static/content/style_articles.css">

<!-- Добавляем блок с затемнённым фоном -->
<div class="background-overlay"></div>

<div class="article-page">
    <big><h1 class="article-front">Интересные статьи</h1></big>
    <big><h4 class="article-front">Пишите интересные статьи, делитель впечатлениями и интересными местами</h4></big>

    % if error:
    <div class="errors">
        {{error}}
    </div>
    % end

    <div class="two-columns">
        
        <!-- ПРАВАЯ КОЛОНКА: ФОРМА -->
        <div class="form-column">
            <div class="menu-container">
                <form action="/articles" method="post" class="article-form">
                    <p>
                        <input type="text" name="author" placeholder="Автор"
                        value="{{old.get('author','')}}">
                    </p>
                    <p>
                        <input type="text" name="title" placeholder="Заголовок"
                        value="{{old.get('title','')}}">
                    </p>
                    <p>
                        <textarea name="content" placeholder="Текст статьи">{{old.get('content','')}}</textarea>
                    </p>
                    <p>
                        <input type="date" name="date"
                        value="{{old.get('date','')}}">
                    </p>
                    <p>
                        <button type="submit">Добавить</button>
                    </p>
                </form>
            </div>
        </div>

        <!-- ЛЕВАЯ КОЛОНКА: КАРУСЕЛЬ -->
        <div class="carousel-column">
            % if articles:
            <div class="carousel-wrapper">
                <button class="arrow-btn" onclick="move(-1)">&#10094;</button>
                
                <div class="carousel-container">
                    <div class="carousel-track" id="track">
                        % for a in articles:
                        <div class="card-item">
                            <h3>{{a['title']}}</h3>
                            <big><big><b>{{a['author']}}</b></big></big>
                            <p>{{a['content']}}</p>
                            <small>{{a['date']}}</small>
                        </div>
                        % end
                    </div>
                </div>
                
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

<script>
let currentIndex = 0;
let track = null;
let items = [];

function updateCarousel() {
    if (!track || items.length === 0) return;
    const width = items[0].offsetWidth;
    track.style.transform = `translateX(-${currentIndex * width}px)`;
}

function move(direction) {
    if (!items.length) return;
    
    // БЕСКОНЕЧНАЯ КАРУСЕЛЬ (по кругу)
    currentIndex += direction;
    
    if (currentIndex < 0) {
        currentIndex = items.length - 1;
    } else if (currentIndex >= items.length) {
        currentIndex = 0;
    }
    
    updateCarousel();
}

window.addEventListener('load', function() {
    track = document.getElementById('track');
    if (track) {
        items = Array.from(track.children);
        window.addEventListener('resize', updateCarousel);
        updateCarousel();
    }
});
</script>