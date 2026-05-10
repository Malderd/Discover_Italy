% rebase('layout.tpl', title=title)
% from files_active_users.storage_active_users import get_active_users
<head>
    <link rel="stylesheet" href="/static/content/style_active_user.css">
</head>
<div style="margin-top:140px;">

    <h1 style="text-align:center;">Бронирование тура</h1>

    <p style="text-align:center;">
        Заполните форму, чтобы забронировать тур по Италии.
    </p>

    <!-- Форма -->
    <div class="booking-wrapper">

        <form action="/active_users" method="post" class="booking-form">

            <input type="text" name="nickname"
                   value="{{form_data.get('nickname','')}}"
                   placeholder="Ник"
                   class="form-control">

            % if 'nickname' in errors:
                <p class="error">{{errors['nickname']}}</p>
            % end

            <br>

            <input type="text" name="email"
                   value="{{form_data.get('email','')}}"
                   placeholder="Почта"
                   class="form-control">

            % if 'email' in errors:
                <p class="error">{{errors['email']}}</p>
            % end

            <br>

            <select name="gender" class="form-control">
                <option value="male">Мужской</option>
                <option value="female">Женский</option>
            </select>

            % if 'gender' in errors:
                <p class="error">{{errors['gender']}}</p>
            % end

            <br>

            <input type="number" name="tour_number"
                   value="{{form_data.get('tour_number','')}}"
                   placeholder="Номер тура"
                   class="form-control">

            % if 'tour_number' in errors:
                <p class="error">{{errors['tour_number']}}</p>
            % end

            <br>

            <input type="text" name="tour_date"
                   value="{{form_data.get('tour_date','')}}"
                   placeholder="Дата тура (ГГГГ-ММ-ДД)"
                   class="form-control">

            % if 'tour_date' in errors:
                <p class="error">{{errors['tour_date']}}</p>
            % end

            <br>

            <input type="submit"
                   value="Забронировать"
                   class="btn booking-btn">

        </form>
    </div>

    <!-- Список активных пользователей -->
    <h2 style="text-align:center">
        Список активных пользователей за последние полгода
    </h2>

    <div class="users-table">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Ник</th>
                    <th>Пол</th>
                    <th>№ последнего тура</th>
                    <th>Дата последнего бронирования</th>
                    <th>Всего туров</th>
                </tr>
            </thead>
            <tbody>
                % for user in users:
                    <tr>
                        <td>{{user['nickname']}}</td>
                        <td>
                            % if user['gender'] == 'male':
                                Мужской
                            % else:
                                Женский
                            % end
                        </td>
                        <td>
                            % if user.get('recent_tours'):
                                {{user['recent_tours'][-1]['tour_number']}}
                            % else:
                                -
                            % end
                        </td>
                        <td>
                            % if user.get('recent_tours'):
                                {{user['recent_tours'][-1]['booking_date']}}
                            % else:
                                -
                            % end
                        </td>
                        <td>{{len(user.get('recent_tours', []))}}</td>
                    </tr>
                % end
            </tbody>
        </table>
    </div>
</div>