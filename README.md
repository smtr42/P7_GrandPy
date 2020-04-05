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
* [Usage](#usage)
* [Contact](#contact)

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
* ![#c5f015](https://bit.ly/2wgCZTL) Flask Framework,
* ![#c5f015](https://bit.ly/2wgCZTL) HTML / CSS,
* ![#c5f015](https://bit.ly/2wgCZTL) Javascript & AJAX,
* ![#c5f015](https://bit.ly/2wgCZTL) Heroku PaaS,
* ![#c5f015](https://bit.ly/2wgCZTL) Common good practices.

Personal challenges and technical choices :
* ![#1589F0](https://placehold.it/15/1589F0/000000?text=+) Use logging
* ![#1589F0](https://placehold.it/15/1589F0/000000?text=+) Not using Jquery or Bootstrap to learn basics


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
git clone https://github.com/smtr42/P5_openfoodfact.git
```
2. Install required dependencies
```sh
pipenv install
```
### Database creation
The user must create himself the MySQL database. Open a MySQL Command Line Client.
```sql
CREATE DATABASE your-database-name CHARACTER SET 'utf8';
```

You must enter the name of the database in the file **configuration/constant.py** as well as your username and your password.

![#f03c15](https://placehold.it/15/f03c15/000000?text=+) `#f03c15`

![#c5f015](https://placehold.it/15/c5f015/000000?text=+) This a

![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `#1589F0`

<!-- USAGE EXAMPLES -->
## Usage
Open a Command Line Interface and launch the main.py script with Python.
```shell script
python -m main
```
### Specifications

When prompted, answer the question by typing the appropriate number or letter.
For a first start you must download data from the API and reset the database. 
Here is an example of usage :
* Type "y" to donwload data
* Type "y" to reset the database
* Type "1" to search for food to substitute
* Select a category
* Select food
* Select healthy food
* You can either go back or save the food in the database for later use.
<br>

All along you can write "r" for going back, "q" to quit, "m" to go back to the first menu.
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

* **Simonnet T** - *Initial work* - [smtr42](https://github.com/smtr42)
   
  <a href="https://www.linkedin.com/in/teiva-s/">
   <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Logo.svg.original.svg" alt="linkedin" width="200" height="54">
 </a>
<br>