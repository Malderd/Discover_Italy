% rebase('layout.tpl', title=title)

<link rel="stylesheet" href="/static/content/style_new_items.css">

<div class="new-items-page">

    <div class="content-grid">
        <div class="left-panel">

            <h1>Маршруты по Италии</h1> <!-- заголовок страницы -->

            <p class="page-description">
                Выбирайте города,создавайте маршруты и делитесь ими с другими.
            </p> <!-- описание страницы -->

            <p class="error">
                % if defined('error'):
                    {{error}}
                % end
            </p> <!-- блок ошибки -->

            <form action="/new_items" method="post" class="route-form">

                <input type="text" name="route_name"
                       placeholder="Название маршрута"
                       class="form-control" required> <!-- поле названия -->

                <textarea name="description"
                          placeholder="Описание маршрута"
                          class="form-control"
                          rows="3" required></textarea> <!-- поле описания -->

                <div class="cities-column">
                    <select name="city1" class="form-control">
                        % for city in cities:
                            <option>{{city}}</option>
                        % end
                    </select> <!-- город 1 -->

                    <select name="city2" class="form-control">
                        % for city in cities:
                            <option>{{city}}</option>
                        % end
                    </select> <!-- город 2 -->

                    <select name="city3" class="form-control">
                        % for city in cities:
                            <option>{{city}}</option>
                        % end
                    </select> <!-- город 3 -->
                </div> <!-- блок выбора городов -->

                <input type="submit"
                       value="Добавить маршрут"
                       class="btn btn-primary"> <!-- кнопка отправки -->

            </form>
        </div>
        
        <div class="right-panel">

            % if routes:
                % for route in routes:
                    <div class="route-item">

                        <div class="route-header">
                            <h3>{{route['name']}}</h3> <!-- название маршрута -->
                            <span class="route-date">Добавлено: {{route['date']}}</span> <!-- дата добавления -->
                        </div>

                        <div class="route-path">
                            <span>{{route['city1']}}</span> <!-- город 1 -->
                            <span class="arrow">→</span>
                            <span>{{route['city2']}}</span> <!-- город 2 -->
                            <span class="arrow">→</span>
                            <span>{{route['city3']}}</span> <!-- город 3 -->
                        </div> <!-- путь маршрута -->

                        <p class="route-desc">{{route['description']}}</p> <!-- описание маршрута -->

                    </div> <!-- карточка маршрута -->
                % end
            % else:
                <p>Маршрутов пока нет</p> <!-- пустой список -->
            % end

        </div>

    </div>

</div>