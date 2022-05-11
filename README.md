# E-biblio 

## Table of contents
- <a href="#about">About E-biblio</a> 
- <a href="#ux">UX Design</a>
  - <a a href="#user-stories">User Stories</a>
  - <a href="#typography">Typography</a>
  - <a href="#color">Color</a>
  - <a href="#wireframes">Wireframes</a>
- <a href="#features">Features</a>
  - <a href="">feature</a>
  - <a href="">feature</a>
  - <a href="">feature</a>
  - <a href="">feature</a>
  - <a href="">feature</a>
  - <a href="">feature</a>
  - <a href="#features-left">Features Left to Impliment</a>
- <a href="#tech">Technologies Used</a>
- <a href="#test">Testing</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>


<section id="about">

# About E-biblio
  E-biblio is an online e-book store specializing in motivational, self-improvement, business and marketing books.

  E-biblio is primarily for two groups of people:

  - People interested in self-improvement - According to <a href='https://blog.marketresearch.com/10.4-billion-self-improvement-market-pivots-to-virtual-delivery-during-the-pandemic#:~:text=Self%2DImprovement%20Market%20Size%3A%20Marketdata,to%20%2414.0%20billion%20by%202025.'>marketresearch.com</a>, Self-Improvement Market Size: Marketdata estimates that the U.S. self-improvement market was worth $11.6 billion in 2019, and that it contracted by 10% to $10.5 billion in 2020. Marketdata forecasts a 7.7% rebound in 2021, to $11.3 billion, and forecasts 6.0% average annual growth to $14.0 billion by 2025. Life coaches and public speakers could find a lot of value in the content on E-biblio.

  - Entrepreneurs - According to <a href='https://www.salesforce.com/blog/small-business-pandemic-entrepreneurs/'>salesforce.com</a>, more than 4.4 million new businesses were created in the U.S. during 2020 — the highest total on record. For reference, that’s a 24.3% increase from 2019 and 51.0% higher than the 2010-19 average. Half a million new businesses were started in January 2021, alone. Data from our most recent B2B survey shares how and why new small business owners took the leap over this past year, and why many may reap the benefits. Ebiblio features many books about marketing and being an entrepreneur. 

  The site is deployed here:
  - https://e-biblio.herokuapp.com/


  <br>
  <img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652297282/p5/Screenshot_from_2022-05-11_20-24-27_t0s3ir.png">
  <br>
  <br>
</section>

<section id="tech">

# Technologies Used 

[Gitpod](https://www.gitpod.io) 
- IDE (Intigrated Development Environment)

[Github](https://www.github.com)
- remote repository hosting platform

[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) | [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) | [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) |  [python](https://www.python.org/) 

- Languages Used to make the site

[Jquery](https://jquery.com/) | [django](https://www.djangoproject.com/) | [coverage](https://coverage.readthedocs.io/en/6.3.2/) 

- libraries and framework used to make the site

[Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
- Used to check site responsiveness

[HTML Validator](https://validator.w3.org/)
- Check for HTML errors

[Jigsaw](https://jigsaw.w3.org/css-validator/)
- Check for CSS errors

[PEP8](http://pep8online.com/)
- Check for python errors

[jshint](https://jshint.com/)
- check for JavaScript errors

[Font Awesome](https://fontawesome.com/)
- for Icons

[Balsamiq](https://balsamiq.com/)
- to make wireframes

# Deployment <p id="deployment"></p>

The site is deployed on [Heroku](https://www.heroku.com/). The link is here:


Steps to deploy the site on Heroku:

- in code editor add requirements for Heroku to install by typing the following commands into the terminal:
  - pip3 freeze > requirements.txt

- create a Procfile in the same directory as manage.py and paste in the following:
  - foo

- in settings.py add Heroku to allowed hosts
  
- commit and push changes

- log in to Heroku or make an account
- click create a new app in the top right corner
- name your app and choose the region you live in
- in the resources tab of your app dashboard add the Postgres database resource
- in the settings tab click reveal config vars and add the following
  - aws
  - DATABASE_URL (added automatically)
  - EMAIL_PASS - the app uses google, steps to set up app passwords found [here](https://support.google.com/accounts/answer/185833?hl=en)
  - EMAIL_USER - Email account address
  - SECRET_KEY - can be anything

- go to the deploy tab and choose GitHub as deploy method
- search for the repo and connect
- click deploy branch
- if the build fails in the top right corner click the 'more' button and check logs to get an indication of the problem
- Click the view app button to see the app


How to fork the repository
- Go to [github.com](https://www.github.com) and log in.
- Click 
- in the top right of the page click the "fork" button
- you will now have a copy of the repository in your GitHub account.

How to clone the repository
- Go to [github.com](https://www.github.com)
- Log in to account
- Click repositories
- Click 
- Click the green code button that says Clone or download 
- to copy from HTTPS copy URL link "HTTPS". 
- open terminal
- go to the directory where you want to save the files
- type git clone and paste the link
- Press enter and the clone will be created
- To install the dependencies required to run the app, in the terminal type: pip3 install -r requirements.txt
- create a .env file in the root directory and in it, import os
- add the following environment variables in the .env file:
  - os.environ["SECRET_KEY"] = <'yourrandomsecretkeyhere'>
  - os.environ["EMAIL_USER"] = <'youremailaddresshere'>
  - os.environ["EMAIL_PASS"] = <'emaipassword'>
  - for the database there are two options:
    - 1) In settings.py use the commented out sql lite database
    - 2) os.environ["DATABASE_URL"] = <'postgresdatabaseurlhere'>
  - os.environ["CLOUDINARY_URL"] = <'yourcloudinaryurlhere'>
- create a superuser in the terminal by typing: python3 manage.py createsuperuser
- run the server by typing: python3 manage.py runserver
- use the superuser credentials to log into the site



More detailed instructions can be found [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository#cloning-a-repository-to-github-desktop)

