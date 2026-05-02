% rebase('layout.tpl', title=title)

<link rel="stylesheet" href="/static/content/style_new_items.css">

<div class="new-items-page">

    <div class="content-grid">
        <div class="left-panel">

            <h1>Маршруты по Италии</h1>

            <p class="page-description">
                Выбирайте города,создавайте маршруты и делитесь ими с другими.
            </p>

            <p class="error">
                % if defined('error'):
                    {{error}}
                % end
            </p>

            <form action="/new_items" method="post" class="route-form">

                <input type="text" name="route_name"
                       placeholder="Название маршрута"
                       class="form-control" required>

                <textarea name="description"
                          placeholder="Описание маршрута"
                          class="form-control"
                          rows="3" required></textarea>

                <div class="cities-column">
                    <select name="city1" class="form-control">
                        % for city in cities:
                            <option>{{city}}</option>
                        % end
                    </select>

                    <select name="city2" class="form-control">
                        % for city in cities:
                            <option>{{city}}</option>
                        % end
                    </select>

                    <select name="city3" class="form-control">
                        % for city in cities:
                            <option>{{city}}</option>
                        % end
                    </select>
                </div>

                <input type="submit"
                       value="Добавить маршрут"
                       class="btn btn-primary">

            </form>
        </div>
        
        <div class="right-panel">

            % if routes:
                % for route in routes:
                    <div class="route-item">

                        <div class="route-header">
                            <h3>{{route['name']}}</h3>
                            <span class="route-date">{{route['date']}}</span>
                        </div>

                        <div class="route-path">
                            <span>{{route['city1']}}</span>
                            <span class="arrow">→</span>
                            <span>{{route['city2']}}</span>
                            <span class="arrow">→</span>
                            <span>{{route['city3']}}</span>
                        </div>

                        <p class="route-desc">{{route['description']}}</p>

                    </div>
                % end
            % else:
                <p>Маршрутов пока нет</p>
            % end

        </div>

    </div>

</div>