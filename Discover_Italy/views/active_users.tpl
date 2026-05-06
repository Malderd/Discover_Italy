% rebase('layout.tpl', title=title)

<h3> Бронирование </h3>
<form action="/home" method="post">
        <p><textarea rows="2" cols="50" name="Имя" placeholder="Ваше имя" style="resize: none;"></textarea></p> 
        <p><input type="text" size="30" name="Почта" placeholder="Ваша почта"></p>
        <p><input type="text" size="50" name="Номер телефон" placeholder="Ваш номер телефон"></p>
         <p><input type="text" size="50" name="Номер тура" placeholder="Ваш номер тура"></p>
        <p><input type="submit" value="Забронированить"></p>
</form>