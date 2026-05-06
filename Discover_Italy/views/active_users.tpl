% rebase('layout.tpl', title=title)

<div class="container booking-container" style="margin-top:120px;">

    <h1>Бронирование тура</h1>

    <p>Заполните форму, чтобы забронировать тур по Италии.</p>

    % if defined('error'):
        <p class="error">{{error}}</p>
    % end

    <form action="/active_users" method="post" class="booking-form">

        <input type="text" name="nickname"
               placeholder="Ник"
               class="form-control" required>

        <br>

        <input type="email" name="email"
               placeholder="Почта"
               class="form-control" required>

        <br>

       <input type="text" name="birthdate"
                placeholder="Дата (DD-MM-YYYY HH:MM)"
                class="form-control" required>

        <br>

        <select name="gender" class="form-control">
            <option value="male">Мужской</option>
            <option value="female">Женский</option>
        </select>

        <br>

        <input type="number" name="tour_number"
               placeholder="Номер тура"
               class="form-control" required>

        <br>

        <input type="submit"
               value="Забронировать"
               class="btn btn-primary booking-btn">

    </form>

    <hr>

    <h2>Список пользователей</h2>

    % for user in users:
        <div class="user-card">
            <h3>{{user['nickname']}}</h3>
            <p>Email: {{user['email']}}</p>
            <p>Дата рождения: {{user['birthdate']}}</p>
            <p>Пол: {{user['gender']}}</p>
            <p>Тур №{{user['tour_number']}}</p>
        </div>
    % end

</div>