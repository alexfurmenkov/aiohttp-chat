const logout_button = {
    button: document.getElementById('login-button'),
};
if (logout_button.button.textContent === 'Logout') {
    logout_button.button.addEventListener('click', (e) => {
        e.preventDefault();
        document.cookie = "Authorization=; path=/";
        window.location.href = "/";
    });
}