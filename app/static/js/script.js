let form = document.querySelector("#user-form");
let chatHistory = document.querySelector('.chat-history')
let body = document.querySelector('body')
let map;


function initMap(lat = 43.397, lng = -4.644) {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: lat, lng: lng},
        zoom: 8
    });
}

/**
 * Handle the creation of html blocs with relevant data
 * @param user : tells if grandpy or user
 * @param text : what to write in the message
 */

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

/**
 *
 * @param url : the url for the flask view
 * @param data :
 * @returns {Promise<any | void>}
 */
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
            writeLine("me", response.input_raw)
            if (response.error) {
                writeLine("grand", response.no_result)
            } else {
                writeLine("grand", response.formatted_message)
            }
            // writeLine("grand", response.formatted_message)
            let latitude = response.lat
            let longitude = response.lon
            body.classList.remove('wait')
            initMap(latitude, longitude);
        })
})