const form = {
    message: document.getElementById('message'),
    submit: document.getElementById('submit'),
};

var socket = new WebSocket('ws://localhost:8000/websocket/');

form.submit.addEventListener('click', (e) => {
    e.preventDefault();
    var message = form.message.value;
    socket.send(message);
    form.message.value = '';
});

function scrollDiv() {
    var element = document.getElementById("messages-holder");
    element.scrollTop = element.scrollHeight;
}

scrollDiv();

socket.onmessage = function (event) {
    let data = JSON.parse(event.data);

    if (data.type === 'service') {
        let service_message = document.createElement("LI");
        service_message.className += "service-message";
        service_message.appendChild(document.createTextNode(data.message + " at " + data.time));
        document.getElementById("myList").appendChild(service_message);
    } else if (data.type === 'message') {
        let login = document.createElement("LI");
        let time = document.createElement("LI");
        login.className += "login";
        time.className += "time";
        login.appendChild(document.createTextNode(data.user_login));
        time.appendChild(document.createTextNode(data.time));

        let message = document.createElement("LI");
        message.className += "message";
        message.appendChild(document.createTextNode(data.message));

        document.getElementById("myList").appendChild(login);
        document.getElementById("myList").appendChild(message);
        document.getElementById("myList").appendChild(time);
    }

    scrollDiv();
};
