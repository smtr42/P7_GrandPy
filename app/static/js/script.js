let form = document.querySelector("#user-form");
let chatHistory = document.querySelector('.chat-history')
let mess = document.querySelector(".chat-history")
let body = document.querySelector('body')
let map;


function initMap(lat = 43.397, lng = -4.644) {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: lat, lng: lng},
        zoom: 8
    });
}

function writeLine(user, text, url) {
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
    if (user == "grand") {
        let a = document.createElement('a')
        let link = document.createTextNode("Lien")
        a.appendChild(link)
        a.title = "Lien"
        a.href = url
        mess.appendChild(a)
    }
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

function linker (url) {
    let a = document.createElement('a');
    let link = document.createTextNode("Lien");
    a.appendChild(link);
    a.title = "Lien";
    a.href = url;
    return a;
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
    body.classList.add("wait")
    postFormData("/ajax", new FormData(form))

        .then(function(response) {
            console.log(response)
            writeLine("me", response.input_raw, "")
            if (response.error) {
                writeLine("grand", response.no_result, "")
            } else {
                writeLine("grand", response.formatted_message, response.url)
                writeline("grand", `<a href='${response.url}'>En savoir plus sur Wikipedia</a>`)
            }
            let latitude = response.lat
            let longitude = response.lon
            body.classList.remove('wait')
            initMap(latitude, longitude);
        })
})