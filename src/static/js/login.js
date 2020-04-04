const form = {
    login: document.getElementById('login'),
    password: document.getElementById('password'),
    submit: document.getElementById('submit'),
};

form.submit.addEventListener('click', (e) => {
    e.preventDefault();
    const request = new XMLHttpRequest();

    request.onload = () => {
        let responseObj = null;
        let cookiestring = null;

        responseObj = JSON.parse(request.responseText);
        cookiestring = "Authorization=" + responseObj.token + "; path=/";
        document.cookie = cookiestring;
        alert(responseObj.message);
        if (responseObj.redirect_link) {
            window.location.href = responseObj.redirect_link;
        }
    };

    const data = {
        login: form.login.value,
        password: form.password.value,
    };

    const json_data = JSON.stringify(data);

    request.open('post', '/login/');
    request.setRequestHeader('Content-Type', 'application/json');
    request.send(json_data);
});