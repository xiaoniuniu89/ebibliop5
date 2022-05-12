# E-biblio 

## Table of contents
- <a href="#about">About E-biblio</a> 
- <a href="#ux">UX Design</a>
  - <a a href="#user-stories">User Stories</a>
  - <a href="#typography">Typography</a>
  - <a href="#color">Color</a>
  - <a href="#wireframes">Wireframes</a>
- <a href="#features">Features</a>
  - <a href="#navbar">Navbar</a>
  - <a href="#footer">Footer</a>
  - <a href="#cta">CTA</a>
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

<section id="ux">

# UX Design

I tried my best to avoid feature creep, stick to wireframes and features I planned before coding, and use Bootstrap which I have not done before on a personal project. I also tried to use the existing example code as a jumping off point wherever possible and not to "reinvent the wheel" for every design decision.

A full list of credits can be found at the bottom of this document as well as scattered throughout the codebase in the comments.


## User Stories <p id="user-stories"></p>

- <a href='https://github.com/xiaoniuniu89/ebibliop5/projects/1' target='_blank'>Account Creation</a>


  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/1' target='_blank'>As a user, I can create an account to access the site for easier checkout in the future.</a>

  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/2' target='_blank'> As a user, I can reset my password in case I lose it</a>

  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/3' target='_blank'> As a user, I can use Google to sign up to the site so I can create an account easier.</a>


- <a href='https://github.com/xiaoniuniu89/ebibliop5/projects/2' target='_blank'>Customer Service</a>


  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/6' target='_blank'>As a user, there is convenient access to a contact form or email for the bookshop incase I have a complaint or problem with my experience on the site.</a>

  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/17' target='_blank'> As the owner of the site I can make and apply promotions easily to offer discounts to my customers.</a>

- <a href='https://github.com/xiaoniuniu89/ebibliop5/projects/3' target='_blank'>Checkout</a>


  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/8' target='_blank'>As a user I can add items to a cart without receiving any annoying popups or prompts to keep shopping or checkout</a>

  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/7' target='_blank'> As a user I can pay by card in a secure manner to protect my sensitive information.</a>

  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/21' target='_blank'> As a user I want to have access to a download link as soon as I pay for my books.</a>

  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/23' target='_blank'> As a user, I can checkout as a guest, so I can buy books without setting up an account. </a>

  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/22' target='_blank'> As a user, i want to receive a confirmation email that contains a link to download my book, so I can have access to the book I just bought as well as a receipt.</a>

  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/7' target='_blank'> As a user I can pay by card in a secure manner to protect my sensitive information</a>

- <a href='https://github.com/xiaoniuniu89/ebibliop5/projects/4' target='_blank'>Site Interactions</a>


  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/12' target='_blank'>As a user, I can leave comments on products to give a detailed review and leave future customers more well-informed. </a>

  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/11' target='_blank'> As a user, I can log into my account, see and have access to download my purchases on my dashboard.</a>

  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/4' target='_blank'> As a user, I can browse books by topic as I would in a real bookstore to narrow in on what I like to read faster.</a>

  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/19' target='_blank'> As a user, I can receive notifications of promotions by email to keep up to date with promotions I might like in the store.</a>

  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/16' target='_blank'> As a user I can search for a book by title or author to find books I am interested in faster.</a>

  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/13' target='_blank'> As a user, I can leave a rating on books to let future customers be more informed.</a>

- <a href='https://github.com/xiaoniuniu89/ebibliop5/projects/5' target='_blank'>Customer Service</a>


  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/9' target='_blank'>As the owner of the site I can make staff level permission to update content so I can delegate work.</a>

  - <a href='https://github.com/xiaoniuniu89/ebibliop5/issues/10' target='_blank'> As a staff/admin I can easily upload new items including the image and pdf to the site in a user friendly admin page so I can complete the task easily.</a>


  

## Typography <p id="typography"></p>

- <a href="https://fonts.google.com/specimen/Roboto#about">Roboto</a> - Used for headings.

- <a href="https://fonts.google.com/specimen/Roboto+Slab#about">Roboto Slab</a> - text compliments Roboto very well. Used mostly for p tags.

## Color <p id="color"></p>

Colors were based off the CTA image on the landing page and the other colors were chosen with help from <a href='http://colormind.io/' target='_blank'>colormind ai</a>

Root Colors:

  - <span style="color: rgb(227, 178, 60);">orange</span>: rgb(227, 178, 60);
  - <span style="color: rgb(207, 162, 55)">orange-hover</span>: rgb(207, 162, 55);
  - white: white;
  - <span style="color: rgb(124, 132, 131)">grey</span>: rgb(124, 132, 131);
  - <span style="color: rgb(45, 49, 66)">blue</span>: rgb(45, 49, 66);
  - <span style="color: rgb(155, 106, 108)">rose</span>: rgb(155, 106, 108);

## Wireframes <p id="wireframes"></p>

Wireframes for the app 
- <a href="">Desktop & Tablet View</a>
- <a href="">Phone View</a>

</section>

<section id="features">

# Features
My last project suffered a lot from feature creep, and as a result, I tried my best to only implement the features I decided on in the planning stages of the project.

I was tempted from time to time to add a new cool feature, for example, a customer wishlist, commenting on reviews, or user book club groups, but by sticking to my original plan I believe the website is a lot stronger and I was able to finish it in roughly a month which is the time limit I gave myself.

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652347638/p5/Screenshot_from_2022-05-12_10-26-18_lmncuh.png">

<br>


# Existing Features <p id="general-features"></p>

## Navbar <p id="navbar"></p>
There are four different versions of the navbar depending on the users role, customer, admin or staff, logged in status.

It features a basket icon to keep track of purchases, a searchbar, links to all the pages in the site. 

The admin/staff navbar in particular makes use of nested dropdown menus.

Nav - not logged in
<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652348738/p5/Screenshot_from_2022-05-12_10-40-30_lshsnk.png">

Nav - customer
<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652348798/p5/Screenshot_from_2022-05-12_10-44-24_wsxos4.png">

Nav - staff
<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652348854/p5/Screenshot_from_2022-05-12_10-41-32_madrm8.png">

Nav - admin
<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652348942/p5/Screenshot_from_2022-05-12_10-40-47_bqgbn1.png">

## Footer <p id="footer"></p>

The footer contains links to important site links as well as privacy and cookie policies. It also features a contact form so as to be accessible from all pages..

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652349070/p5/Screenshot_from_2022-05-12_10-50-35_vjp5vr.png">

## CTA <p id="cta"></p>

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652347438/p5/Screenshot_from_2022-05-12_10-23-25_g467y0.png">

The call to action is quite simple. I used a picture full of bright oranges that influenced the rest of the site's colors a lot. The aim is to make the user feel a sense of freedom by using ebooks.


The cta text is a simple piece of text describing the site, encouraging customers to buy something by providing a promo code, and a call to action to sign up.


## Logo <p id="logo"></p>

<img src="assets/images/logo.png">

The logo text was a very important consideration, because I wanted the text to look somewhat like the logo of the <a href="https://www.wordmillgames.com/mythic-rpg.html"> source book</a>.

## How to section <p id="how-to"></p>

### Button
<img src="assets/images/how-to-btn.png">

### Modal
<img src="assets/images/how-to-modal.png">


All of the text explaining how to use the app is found in a modal window that the user can open without going to a new page. Overall I wanted it to feel like a rulebook, as many users of this app would be familiar with having 1-2 rulebooks open at all times to play a game. 

It will darken the background to create contrast with the app and it has its own unique scrollbar which I feel will not distract from the aesthetics of the app.

This gave me a lot of freedom to write as much content as I wanted for the how-to-use section without cluttering up the site and affecting the user experience. unfortunately, the how to section is to cramped on mobile view, so at smaller screen widths, the iframes are replaced with clickable links and some of the less important paragraphs will not be displayed.

  The app can be quite complicated to use, so I am very pleased with the how-to section and how in-depth it went with explaining everything and giving examples of use. 



## Emulator <p id="emulator"></p>

<img src="assets/images/emulator.png">

### Tabs

<image src="assets/images/tabs.png">

The three tabs each display different content. The active tab is also a brighter color to remind users where they are. 

## Oracle Tab <p id="oracle"></p>

### Chaos Number

<img src="assets/images/chaos.png">

The chaos number starts at 5. It can go as low as 1 and as high as 9. The chaos number represents how in control the players are of the adventure. When it reaches level 9 a color animation will make the chaos number flash a blood red to highlight how out of control the players are of the adventure. 

### Fate Buttons

<img src="assets/images/fate-btns.png">

The three buttons at the bottom of the oracle tab are the main ways users interact with mythic. 

The start scene button is used whenever the user starts a new scene/chapter. The higher the chaos number the higher the chance of something random happening at the start of a scene. 

The question button lets users ask Mythic yes/no questions. When clicked users are prompted to select the odds of their question being yes. The higher the chaos number, the higher the chance the question will be yes. There is also the possibility of a random event happening here. It is  
referred to as the Fate chart in the source material. 

<img src="assets/images/fate-chart.png">

The event button generates two random keywords that the user will interpret to give direction to the story or to flesh out a yes/no answer.


<img src="assets/images/event-keywords.png">

each random keyword is stored in an array containing 100 words. In the source material, a user accesses these by rolling percentile dice. 



<img src="assets/images/display-ex.png">

When an answer is displayed - the emulator window will display a blur effect animation with the text in the center of the window. 

## Journal Tab <p id="journal"></p>

 <img src="assets/images/journal-tab.png"></section>

 The journal tab is a place the user can chronicle their adventure. 

<img src="assets/images/add-scene.png">

users can add a scene box. It has space for a title and for the body of the scene text also. It is scrollable so a user can make it as short or long as desired. 

## Lists Tab <p id="lists"></p>

 <img src="assets/images/lists-tab.png">

 The lists tab is a place to keep track of any non-playable characters/groups and 
threads(plot points) that are relevant to the adventure.

 <img src="assets/images/lists-ex.png">

 The input from both lists will be stored in an array that the oracle will randomly select from in some cases of random events. If they are empty nothing will be selected. 

## Footer <p id="footer"></p>

 <img src="assets/images/footer.png">

 The footer is extremely simple. It has links to some social media sites about me. 

## Features to Impliment <p id="features-left"></p>

 ### NPC Generator 
 A feature to generate non-playable characters with names and backstories. This is so the user will not have to pause the game and think of one by themselves. 

 ### Encounter Generator 
 A feature to generate encounters for the players. This would be an extension of the random event and event button. Ideally, encounters should be fleshed out more so the players do not need to interpret an answer.

 ### Scene/Mission Generator 
 A feature to auto-generate the scene action for the players so they have a goal without the need for planning.

 ### Monster Stats 
 This would involve a database of monsters and their stats from some of the more popular RPG systems like dungeons and dragons and pathfinder. 

### Music 
Music and background sounds - A simple music player to provide more atmosphere. 

### 3D dice 
This would be useful for players who want to play but don't have access to dice

### Mythic Variations 1 & 2 
There are another 2 books in the Mythic GM series that provide more options to players for using mythic. It would be great to implement them into this app. 

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

