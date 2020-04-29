<h1 align="center">
  <br>

  <br>
  Project 7 - GrandPy
  <br>
</h1>
<p align="center">
  <a href="">
    <img src="https://upload.wikimedia.org/wikipedia/fr/0/0d/Logo_OpenClassrooms.png" alt="Logo" width="100" height="100">
  </a>
</p>

<p align="center">
  <a href="">
    <img src="https://img.shields.io/badge/Python-3.7-green.svg">
  </a>
  <a href="https://www.linkedin.com/in/teiva-s/">
    <img src="https://img.shields.io/badge/linkedin-Simonnet-blue.svg">
  </a>
</p>
  <h3 align="center">Return</h3>

 <p align="center">
    A simple flask application as part as an <a href="https://openclassrooms.com/en" target="_blank">OpenClassrooms</a> project
    <br />
  </p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
* [Links](#links)
* [Authors](#authors)

<!-- ABOUT THE PROJECT -->
## About The Project

<p align="center">
  <a href="https://fr.openfoodfacts.org/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Wikipedia-logo-v2-fr.svg/langfr-225px-Wikipedia-logo-v2-fr.svg.png" width="150" height="170">
  </a>
  <a href="https://fr.openfoodfacts.org/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Google_Maps_Logo_2020.svg/langfr-150px-Google_Maps_Logo_2020.svg.png" >
  </a>
  <a href="https://fr.openfoodfacts.org/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/langfr-330px-Flask_logo.svg.png">
  </a>
</p>

The goal is to create an application that gives localisation from a place and related informations from Wikipedia.

This project is the 7th assignment for the Python developer diploma from OpenClassrooms.
The goal is to learn about:
* ![#c5f015](https://bit.ly/2wgCZTL) REST APIs,
* ![#c5f015](https://bit.ly/2wgCZTL) Test Driven Development,
* ![#c5f015](https://bit.ly/2wgCZTL) Agile development using Trello,
* ![#f03c15](https://bit.ly/2wgCZTL) Flask Framework,
* ![#f03c15](https://bit.ly/2wgCZTL) HTML / CSS,
* ![#f03c15](https://bit.ly/2wgCZTL) Javascript & AJAX,
* ![#f03c15](https://bit.ly/2wgCZTL) Heroku PaaS,
* ![#c5f015](https://bit.ly/2wgCZTL) Common good practices.

Personal challenges and technical choices :
* ![#c5f015](https://bit.ly/2wgCZTL) Use logging
* ![#c5f015](https://bit.ly/2wgCZTL) Not using Jquery or Bootstrap to learn basics


### Functionality

* The user search a place
* The app is deployed on Heorku

<!-- GETTING STARTED -->
## Getting Started

### Installation
I use Python 3.7.
I use pipenv to manage dependencies.

1. Clone the repo
```sh
git clone https://github.com/smtr42/P7_GrandPy.git
```
2. Install required dependencies
```sh
pipenv install
```
To use it in local, you must create a *.env* in `app/config/`file where your put your API identifiers like this :
```.env
google_api = "your_api_key"
FRONT_API_KEY = "your_api_key"
```
To run the application in local :
```sh
python -m main
```
Open your webbrowser and go to `http://127.0.0.1:5000/`

The application can be used online at https://p7grandpy.herokuapp.com/

## Links
* [French Stop Words](https://github.com/6/stopwords-json/blob/master/dist/fr.json)
* [Flask](https://github.com/pallets/flask)
* [Pytest](https://github.com/pytest-dev/pytest)
* [Requests: HTTP for Humans™](https://requests-fr.readthedocs.io/en/latest/)
* [Heroku](https://www.heroku.com/)
* [Trello](https://trello.com/)
* [Wikipedia](https://en.wikipedia.org/)
* [Google maps](https://www.google.fr/maps)


## Authors

* **Simonnet T** - [smtr42](https://github.com/smtr42)
   
  <a href="https://www.linkedin.com/in/teiva-s/">
   <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Logo.svg.original.svg" alt="linkedin" width="200" height="54">
 </a>
<br>