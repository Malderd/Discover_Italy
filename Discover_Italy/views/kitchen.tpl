<!-- Подключение базового шаблона с заголовком и годом -->
% rebase('layout.tpl', title=title, year=year)

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/content/style_kitchen.css">
</head>
<body>

<!-- Главный контейнер с меню -->
<div class="menu-container">
    
    <!-- ОСНОВНОЙ ЗАГОЛОВОК -->
    <h1 class="menu-title">Итальянская кухня</h1>
    
    <!-- ========== РАЗДЕЛ ПИЦЦА ========== -->
    <h2 class="menu-title">🍕 Пицца</h2>
    
    <!-- Карточка с пиццей -->
    <div class="menu-item">
        <div class="menu-item-content">
            <div class="menu-item-text">
                <h3>Неополитанская пицца</h3>
                <p>Традиционная итальянская пицца из Неаполя с мягким, эластичным тестом, тонким центром и высокими воздушными бортиками. Выпекается в дровяной печи при высокой температуре всего 60-90 секунд. Настоящее искусство итальянских пиццайоло!</p>
            </div>
            <img src="/static/images/Pizza_napolitaine_maison.jpg" alt="Неополитанская пицца" class="menu-item-image">
        </div>
    </div>
    
    <hr> <!-- РАЗДЕЛИТЕЛЬ МЕЖДУ КАРТОЧКАМИ -->
    
    <!-- Карточка с пиццей пепперони -->
    <div class="menu-item">
        <div class="menu-item-content">
            <div class="menu-item-text">
                <h3>Пицца пепперони</h3>
                <p>Популярная пицца с острыми колбасками салями (пепперони), нежной моцареллой и ароматным томатным соусом. Идеальное сочетание для любителей пикантного вкуса.</p>
            </div>
            <img src="/static/images/peperoni.jpg" alt="Пицца пепперони" class="menu-item-image">
        </div>
    </div>
    
    <hr> <!-- РАЗДЕЛИТЕЛЬ МЕЖДУ КАРТОЧКАМИ -->
    
    <!-- ========== РАЗДЕЛ ПАСТА ========== -->
    <h2 class="menu-title">🍝 Паста</h2>
    
    <!-- Карточка с карбонарой -->
    <div class="menu-item">
        <div class="menu-item-content">
            <div class="menu-item-text">
                <h3>Паста карбонара</h3>
                <p>Спагетти с мелкими кусочками гуанчале (щековина) в нежном соусе из яиц, сыра пекорино романо и свежемолотого чёрного перца. Соус доходит до готовности от тепла только что сваренной пасты.</p>
            </div>
            <img src="/static/images/karbonara.jpg" alt="Паста карбонара" class="menu-item-image">
        </div>
    </div>
    
    <hr> <!-- РАЗДЕЛИТЕЛЬ МЕЖДУ КАРТОЧКАМИ -->
    
    <!-- Карточка с болоньезе -->
    <div class="menu-item">
        <div class="menu-item-content">
            <div class="menu-item-text">
                <h3>Паста болоньезе</h3>
                <p>Тальятелле с густым, насыщенным мясным соусом рагу. Соус готовится часами из говяжьего фарша, овощей, томатов и красного вина, создавая неповторимый богатый вкус.</p>
            </div>
            <img src="/static/images/boloneze.jpg" alt="Паста болоньезе" class="menu-item-image">
        </div>
    </div>

    <hr> <!-- РАЗДЕЛИТЕЛЬ МЕЖДУ КАРТОЧКАМИ -->

    <!-- Карточка с песто -->
    <div class="menu-item">
        <div class="menu-item-content">
            <div class="menu-item-text">
                <h3>Паста песто</h3>
                <p>Трофье с ароматным соусом песто из свежего базилика, кедровых орехов, пармезана и оливкового масла. Вкус солнечной Италии в каждой тарелке!</p>
            </div>
            <img src="/static/images/pesto.jpg" alt="Паста песто" class="menu-item-image">
        </div>
    </div>
    
    <hr> <!-- РАЗДЕЛИТЕЛЬ МЕЖДУ КАРТОЧКАМИ -->
    
    <!-- ========== РАЗДЕЛ ДЕСЕРТЫ ========== -->
    <h2 class="menu-title">🍰 Десерты</h2>

    <!-- Карточка с тирамису -->
    <div class="menu-item">
        <div class="menu-item-content">
            <div class="menu-item-text">
                <h3>Тирамису</h3>
                <p>Изысканный десерт из слоёв печенья савоярди, пропитанных эспрессо, и нежного крема маскарпоне. Посыпан горьким какао — идеальный баланс сладости и лёгкой горчинки.</p>
            </div>
            <img src="/static/images/tiramisu.jpg" alt="Тирамису" class="menu-item-image">
        </div>
    </div>

    <hr> <!-- РАЗДЕЛИТЕЛЬ МЕЖДУ КАРТОЧКАМИ -->

    <!-- Карточка с панна-коттой -->
    <div class="menu-item">
        <div class="menu-item-content">
            <div class="menu-item-text">
                <h3>Панна-котта</h3>
                <p>Нежный сливочный десерт с ванилью, подаваемый с ярким ягодным соусом. Название переводится как «вареные сливки» — тает во рту!</p>
            </div>
            <img src="/static/images/panna_cotta.jpg" alt="Панна-котта" class="menu-item-image">
        </div>
    </div>

    <hr> <!-- РАЗДЕЛИТЕЛЬ МЕЖДУ КАРТОЧКАМИ -->

    <!-- Карточка с джелато -->
    <div class="menu-item">
        <div class="menu-item-content">
            <div class="menu-item-text">
                <h3>Джелато</h3>
                <p>Традиционное итальянское мороженое с плотной кремообразной текстурой. Только натуральные ингредиенты — свежее молоко, ягоды, орехи и шоколад.</p>
            </div>
            <img src="/static/images/Gelato.jpg" alt="Джелато" class="menu-item-image">
        </div>
    </div>

    <hr> <!-- РАЗДЕЛИТЕЛЬ МЕЖДУ КАРТОЧКАМИ -->

    <!-- Карточка с кассатой -->
    <div class="menu-item">
        <div class="menu-item-content">
            <div class="menu-item-text">
                <h3>Кассата</h3>
                <p>Праздничный сицилийский десерт: сочный бисквит с ликёром, прослойка из сладкой рикотты с цукатами и шоколадом, покрытие из марципана.</p>
            </div>
            <img src="/static/images/kassata.jpg" alt="Кассата" class="menu-item-image">
        </div>
    </div>
    
    <!-- Подвал -->
    <p style="text-align: center; color: black; margin-top: 40px;">
        Buon appetito!
    </p>
    
</div>  

</body>
</html>