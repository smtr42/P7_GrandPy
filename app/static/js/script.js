console.log("sre efg")

let form = document.querySelector("#user-form");

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
            console.log(response);
        })
})

function initMap() {
    // The location of Uluru
    var uluru = {lat: -25.344, lng: 131.036};
    // The map, centered at Uluru
    var map = new google.maps.Map(
        document.getElementById('map'), {zoom: 4, center: uluru});
    // The marker, positioned at Uluru
    var marker = new google.maps.Marker({position: uluru, map: map});
}

Window.initMap = initMap