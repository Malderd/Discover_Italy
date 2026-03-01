% rebase('layout.tpl', title='Discover Italy')

<!-- Главная секция -->
<div class="main-section">
    <div class="main-content">
        <h1 class="main-title">Benvenuti in Italia!</h1>
        <p class="main-subtitle">Откройте для себя магию Италии — страны, где история встречается с современностью,    
        а страсть к жизни чувствуется в каждом уголке.</p>
        <a href="#discover" class="main-btn">Начните путешествие</a>
    </div>
</div>

<!-- Блок с тремя карточками -->
<div id="discover" class="features-section">
    <h2 class="section-title">Италия в трех красках</h2>
    <div class="features-cards">
        <!-- Зеленая карточка -->
        <div class="feature-card card-green">
            <div class="feature-icon">🌳</div>
            <h3>Природа</h3>
            <p>Живописные холмы Тосканы, озеро Комо, заснеженные Доломитовые Альпы и вулканические ландшафты Сицилии.</p>
            <ul class="feature-list">
                <li>🏞️ Озеро Комо</li>
                <li>🏖️ Чинкве-Терре</li>
                <li>⛰️ Доломиты</li>
            </ul>
        </div>
        
        <!-- Белая карточка -->
        <div class="feature-card card-white">
            <div class="feature-icon">🏛</div>
            <h3>Культура</h3>
            <p>Колизей в Риме, каналы Венеции, Римский форум, город Помпеи, Миланский собор  — величайшие шедевры искусства.</p>
            <ul class="feature-list">
                <li>🎭 Римский форум</li>
                <li>🛶 Каналы Венеции</li>
                <li>🏛 Помпеи</li>
            </ul>
        </div>
        
        <!-- Красная карточка -->
        <div class="feature-card card-red">
            <div class="feature-icon">🍝</div>
            <h3>Кухня</h3>
            <p>Аутентичная пицца из Неаполя, паста карбонара, пицца маргарита, тирамису, панна-котта, кьянти и настоящее джелато.</p>
            <ul class="feature-list">
                <li>🍕 Пицца Маргарита</li>
                <li>🍷 Кьянти</li>
                <li>🍰 Тирамису</li>
            </ul>
        </div>
    </div>
</div>

<div class="italy-flag"></div>

<!-- Популярные направления -->
<div class="destinations-section">
    <h2 class="section-title">Популярные направления</h2>
    <div class="destinations-grid">
        <!-- Рим -->
        <a href="/cities#rome" class="destination-card-link">
            <div class="destination-card">
                <img src="/static/images/rome.jpg" alt="Рим" class="destination-img">
                <div class="destination-overlay">
                    <h3>Рим</h3>
                    <p>Вечный город</p>
                    <span class="destination-tag">Колизей, Ватикан</span>
                </div>
            </div>
        </a>
        
        <!-- Флоренция -->
        <a href="/cities#florence" class="destination-card-link">
            <div class="destination-card">
                <img src="/static/images/florence.jpg" alt="Флоренция" class="destination-img">
                <div class="destination-overlay">
                    <h3>Флоренция</h3>
                    <p>Колыбель Ренессанса</p>
                    <span class="destination-tag">Уффици, Дуомо</span>
                </div>
            </div>
        </a>
        
        <!-- Венеция -->
        <a href="/cities#venice" class="destination-card-link">
            <div class="destination-card">
                <img src="/static/images/venecia.jpg" alt="Венеция" class="destination-img">
                <div class="destination-overlay">
                    <h3>Венеция</h3>
                    <p>Город на воде</p>
                    <span class="destination-tag">Каналы, Гранд-канал</span>
                </div>
            </div>
        </a>
    </div>
</div>

<div class="italy-flag"></div>

<!-- Цитата -->
<div class="quote-section">
    <div class="quote-container">
        <p class="quote-text">"Италия — это страна, где даже лимоны поют. Место, где искусство дышит в каждом камне."</p>
        <p class="quote-author">— Итальянская поговорка</p>
    </div>
</div>

<div class="italy-flag"></div>

<!-- Три кнопки навигации -->
<div class="nav-buttons">
    <a href="/cities" class="nav-btn" style="background-color: #008C45;">Города Италии</a>
    <a href="/kitchen" class="nav-btn white">Итальянская кухня</a>
    <a href="/contact" class="nav-btn" style="background-color: #CD212A;">Контакты</a>
</div>