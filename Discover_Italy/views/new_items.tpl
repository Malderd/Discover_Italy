% rebase('layout.tpl', title=title)

<link rel="stylesheet" href="/static/content/style_new_items.css">

<div class="new-items-page">

    <div class="content-grid">
        <div class="left-panel">

            <h1>Маршруты по Италии</h1>

            <p class="page-description">
                Выбирайте города, создавайте маршруты и делитесь ими с другими.
            </p>

            <div class="error">
                % if errors:
                    {{list(errors.values())[0]}}
                % end
            </div>

            <form action="/new_items" method="post" class="route-form" novalidate>

                <!-- name -->
                <input type="text" name="route_name"
                       value="{{form_data.get('route_name','')}}"
                       placeholder="Название маршрута"
                       class="form-control % if errors.get('route_name'): input-error % end"
                       required>

                <!-- description -->
                <textarea name="description"
                          placeholder="Описание маршрута"
                          class="form-control % if errors.get('description'): input-error % end"
                          rows="3">{{form_data.get('description','')}}</textarea>

                <!-- date -->
                <input type="text" name="date"
                       value="{{form_data.get('date','')}}"
                       placeholder="Дата (ГГГГ-ММ-ДД ЧЧ:ММ)"
                       class="form-control % if errors.get('date'): input-error % end"
                       required>

                <!-- cities -->
                <div class="cities-column % if errors.get('cities'): input-error % end">

                    <select name="city1" class="form-control">
                        % for city in cities:
                            <option value="{{city}}"
                                % if form_data.get('city1') == city:
                                    selected
                                % end
                            >{{city}}</option>
                        % end
                    </select>

                    <select name="city2" class="form-control">
                        % for city in cities:
                            <option value="{{city}}"
                                % if form_data.get('city2') == city:
                                    selected
                                % end
                            >{{city}}</option>
                        % end
                    </select>

                    <select name="city3" class="form-control">
                        % for city in cities:
                            <option value="{{city}}"
                                % if form_data.get('city3') == city:
                                    selected
                                % end
                            >{{city}}</option>
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
                            <span class="route-date">Дата: {{route['date']}}</span>
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
                <p class="empty-routes">Маршрутов пока нет</p>
            % end

        </div>

    </div>

</div>