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
    let data = event.data;
    var node = document.createElement("LI");
    var textnode = document.createTextNode(data);
    node.appendChild(textnode);
    document.getElementById("myList").appendChild(node);
};
