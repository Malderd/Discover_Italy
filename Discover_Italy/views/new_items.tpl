% rebase('layout.tpl', title=title)

<div class="container" style="margin-top:120px;color:white;">

    <h1>Маршруты по Италии</h1>

    <p>Создавайте свои маршруты и делитесь идеями путешествий.</p>

    % if defined('error'):
        <p style="color:red;">{{error}}</p>
    % end

    <form action="/new_items" method="post">

        <input type="text" name="route_name"
               placeholder="Название маршрута"
               class="form-control" required>

        <br>

        <textarea name="description"
                  placeholder="Описание маршрута"
                  class="form-control"
                  rows="3" required></textarea>

        <br>

        <select name="city1" class="form-control">
            % for city in cities:
                <option>{{city}}</option>
            % end
        </select>

        <br>

        <select name="city2" class="form-control">
            % for city in cities:
                <option>{{city}}</option>
            % end
        </select>

        <br>

        <select name="city3" class="form-control">
            % for city in cities:
                <option>{{city}}</option>
            % end
        </select>

        <br>

        <input type="submit"
               value="Добавить маршрут"
               class="btn btn-primary">

    </form>

    <hr>

    % if routes:
        % for route in routes:
           <div class="card" style="margin-bottom:20px; padding:15px; color:white;">
                <h3>{{route['name']}}</h3>

                <p>{{route['description']}}</p>

                <p>
                    {{route['city1']}} →
                    {{route['city2']}} →
                    {{route['city3']}}
                </p>

                <small>Добавлено: {{route['date']}}</small>
            </div>
        % end
    % else:
        <p>Маршрутов пока нет</p>
    % end

</div>