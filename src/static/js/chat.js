const form = {
    message: document.getElementById('message'),
    submit: document.getElementById('submit'),
};

var socket = new WebSocket('ws://localhost:8000/websocket/');

form.submit.addEventListener('click', (e) => {
    e.preventDefault();
    var message = form.message.value;
    socket.send(message);
});

socket.onmessage = function (event) {
    let data = JSON.parse(event.data);

    let node_login = document.createElement("LI");
    node_login.className += "login";
    node_login.appendChild(document.createTextNode(data.user_login));

    let node_message = document.createElement("LI");
    node_message.className += "message";
    node_message.appendChild(document.createTextNode(data.message));

    document.getElementById("myList").appendChild(node_login);
    document.getElementById("myList").appendChild(node_message);
};
