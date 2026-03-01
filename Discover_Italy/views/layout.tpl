<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

     <!-- Заголовок страницы, динамически подставляется из контекста -->
    <title>{{ title }} - Discover Italy</title>

    <!-- Подключение фреймворка Bootstrap -->
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />

        <!-- Пользовательские стили для сайта -->
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <link rel="stylesheet" href="/static/content/style_home.css">
    <link rel="stylesheet" type="text/css" href="/static/content/style.css" />

    <!-- Подключение шрифта Poppins с Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>

<body>
    <!-- Навигационная панель с фиксацией сверху -->
    <div class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <!-- Логотип/название сайта, ведущее на главную -->
                <a href="/" class="navbar-brand">Discover Italy</a>
            </div>

            <!-- Основное меню навигации -->
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li><a href="/cities">Города</a></li>
                    <li><a href="/kitchen">Кухня</a></li>
                    <li><a href="/contact">Контакты</a></li>
                </ul>
            </div>
        </div>
    </div>

     <!-- Основной контейнер для контента страниц -->
    <div class="container body-content">
        {{!base}}
    </div>

     <!-- Основной контейнер для контента страниц -->
    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>
