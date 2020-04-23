let form = document.querySelector("#user-form");
let chatHistory = document.querySelector('.chat-history')


function writeLine(user, text) {
    let li = document.createElement("li")
    let head = document.createElement("div")
    let message = document.createElement("div")
    head.classList.add("message-head")
    message.classList.add("message")
    message.classList.add(user)
    let headText = document.createTextNode(user)
    let messageText = document.createTextNode(text)
    head.appendChild(headText)
    message.appendChild(messageText)
    chatHistory.appendChild(head)
    chatHistory.appendChild(message)
    chatHistory.scrollTop = chatHistory.scrollHeight;
}


function postFormData(url, data) {
    return fetch(url, {
        method: "POST",
        body: data
    })
        .then(response => response.json())
        .catch(error => console.log(error));
}

form.addEventListener("submit", function (event) {
    event.preventDefault();
    postFormData("/ajax", new FormData(form))
        .then(response => {
            console.log(response)
            console.log("lkklzd zd lkzd ld")
            writeLine("me", response.input_raw)
            let text = "Ca se situe là : " + response.address + ". " + response.page_id_article
            writeLine("grand", text);
        })
})


let map;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: 43.397, lng: 4.644},
      zoom: 8
    });
}
Window.initMap = initMap