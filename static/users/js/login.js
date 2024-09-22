var is_register = 1;

function error(input) {
    if (input) {
        document.getElementById("error").innerHTML = input;
    } else {
        document.getElementById("error").innerHTML = "";
    }
}

function register_response(response) {
    if (response['success']) {
        window.location.href = "/user";
    } else {
        error("Почта уже занята");
    }
}
function login_response(response) {
    if (response['success']) {
         window.location.href = "/user";
    } else {
        error("Неверная почта или пароль");
    }
}

function send(event) {
    event.preventDefault();
    error();
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    if (is_register) {
        let name = document.getElementById("name").value;
        let phone = document.getElementById("phone").value;
        let repeat_password = document.getElementById("repeat_password").value;

        if (!name) {
            error("Вы не ввели ФИО");
        } else if (!email) {
            error("Вы не ввели почту");
        } else if (!phone) {
            error("Вы не ввели номер телефона");
        } else if (!password) {
            error("Вы не ввели пароль");
        } else if (password != repeat_password) {
            error("Пароли не совпадают");
        } else {
            send_data({
                act:"register",
                name:name,
                email:email,
                phone:phone,
                password:password,
                repeat_password:repeat_password,
            }, register_response);
        }
    } else {
        if (!email) {
            error("Вы не ввели почту");
        } else if (!password) {
            error("Вы не ввели пароль");
        } else {
            send_data({
                act:"login",
                email:email,
                password:password,
            }, login_response);
        }
    }
}

function register() {
    error();
    document.getElementById("big-text").innerHTML = "Регистрация";
    document.getElementById("small-text").innerHTML = "Вход";
    document.getElementById("small-text").onclick = login;
    document.getElementById("name").style.display = 'block';
    document.getElementById("phone").style.display = 'block';
    document.getElementById("repeat_password").style.display = 'block';
    is_register = 1;
}

function login() {
    error();
    document.getElementById("big-text").innerHTML = "Вход";
    document.getElementById("small-text").innerHTML = "Регистрация";
    document.getElementById("small-text").onclick = register;
    document.getElementById("name").style.display = 'none';
    document.getElementById("phone").style.display = 'none';
    document.getElementById("repeat_password").style.display = 'none';
    is_register = 0;
}
