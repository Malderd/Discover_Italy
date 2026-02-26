% rebase('layout.tpl', title=title, year=year)

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/static/content/style.css"
</head>
<body>

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>

<div class="menu-container">
    <h2 class="menu-title">Меню итальянской пиццы</h2>
    <p class="image-credit">Изображения из Freepik</p>
    
    <div class="menu-item">
        <h3>Пицца с сыром</h3>
        <p>Приобретите нашу классическую сырную пиццу «Манхэттен» с соусом и корочкой на ваш выбор.</p>
        <p class="price"><strong>$15.95</strong></p>
    </div>
    
    <hr>
    
    <div class="menu-item">
        <h3>Пицца пепперони</h3>
        <p>Приобретите нашу классическую пиццу «Пепперони» с соусом и корочкой на ваш выбор.</p>
        <p class="price"><strong>$16.35</strong></p>
    </div>
    
    <hr>
    
    <div class="menu-item">
        <h3>Вегетарианская пицца</h3>
        <p>Томатный соус, моцарелла, зеленый перец, лук, свежие грибы, помидоры и черные оливки.</p>
        <p class="price"><strong>$19.95</strong></p>
    </div>
</div>

<p>Use this area to provide additional information.</p>