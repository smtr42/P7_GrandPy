let form = document.querySelector("#user-form");
let chatHistory = document.querySelector('.chat-history')
let map;


function initMap(lat = 43.397, lng = -4.644) {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: lat, lng: lng},
        zoom: 8
    });
}

function writeLine(user, text) {
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

        .then(function(response) {
            console.log(response)
            writeLine("me", response.input_raw)
            let text = "Ca se situe là : " + response.address + ". Je t'ai déjà raconté cette anecdote ? " + response.page_id_article + ". Pour en savoir plus regarde cette adresse : " + response.url
            writeLine("grand", text)
            let latitude = response.lat
            let longitude = response.lon
            console.log(response.lat, response.lon)
            initMap(latitude, longitude);
        })

        // .then(response => {
        //     console.log(response)
        //     writeLine("me", response.input_raw)
        //     let text = "Ca se situe là : " + response.address + ". Je t'ai déjà raconté cette anecdote ? " + response.page_id_article + ". Pour en savoir plus regarde cette adresse : " + response.url
        //     writeLine("grand", text);
        // })
})