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
  - <a href="#popular">Popular Books</a>
  - <a href="#categories">Category Pages</a>
  - <a href="#product">Product Page</a>
  - <a href="dashboard">Dashboard</a>
  - <a href="basket">Basket</a>
  - <a href="checkout">Checkout</a>
  - <a href="newsletter">Newsletter</a>
  - <a href="#features-left">Features Left to Impliment</a>
- <a href="#testing">Testing</a>
- <a href="#tech">Technologies Used</a>
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

The footer contains links to important site links as well as privacy and cookie policies. It also features a collapsable accordian containing the contact us form and the subscribe to newletter form.

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652476290/p5/Screenshot_from_2022-05-13_21-55-11_1_nyzb9i.png">

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652476432/p5/Screenshot_from_2022-05-13_22-13-17_jmevas.png">

## CTA <p id="cta"></p>

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652347438/p5/Screenshot_from_2022-05-12_10-23-25_g467y0.png">

The call to action is quite simple. I used a picture full of bright oranges that influenced the rest of the site's colors a lot. The aim is to make the user feel a sense of freedom by using ebooks.


The cta text is a simple piece of text describing the site, encouraging customers to buy something by providing a promo code, and a call to action to sign up.


## Popular Books <p id="popular"></p>

The landing page also features a selection of the 8 most popular books on the site by rating score"

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652392495/p5/Screenshot_from_2022-05-12_22-53-28_mc6m5b.png">


## Category Pages <p id="categories"></p>

The category pages allow the user to browse books by category. They are paginated in blocks of 12 books.

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652392971/p5/Screenshot_from_2022-05-12_23-02-04_ihhjqs.png">


## Product Page <p id="product"></p>

The product detail page has a lot of functionality.

Users can add the book to their basket. The book features a rating out of 5 stars based on user reviews, if you are admin there is a link to edit the book information.

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652394656/p5/Screenshot_from_2022-05-12_23-26-37_tjy1ki.png">

the page also features a review section. Users can add a rating and review, update and delete it. the reviews are handled by an ajax request and do not require page refresh to view.

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652394761/p5/Screenshot_from_2022-05-12_23-27-00_rdocv7.png">

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652394802/p5/Screenshot_from_2022-05-12_23-27-09_mm09kf.png">

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652394846/p5/Screenshot_from_2022-05-12_23-27-28_qgb5l0.png">


## Dashboard <p id="dashboard"></p>

The user dashboard is for all non staff users as staff and admin both use the built in django admin panel.

From here users can access the pdf links of all purchases.

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652393779/p5/Screenshot_from_2022-05-12_23-10-33_rtj5sl.png">

There is a list of past orders with links to a pdf of the order invoice

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652393904/p5/Screenshot_from_2022-05-12_23-10-38_lvubeu.png">


<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652393854/p5/Screenshot_from_2022-05-12_23-10-46_oheg2j.png">

There is also a list of all the users' past reviews is also in the dashboard.

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652394000/p5/Screenshot_from_2022-05-12_23-10-59_eyqjy7.png">

The billing modal allow the user to update their billing information


<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652394141/p5/Screenshot_from_2022-05-12_23-11-16_dmdqb0.png">




## Basket Summary <p id="basket"></p>

The basket summary page contains a list of all items in the users basket. Items can be removed from the basket and if it is empty, the user can not proceed to checkout as minimum purchase is 50 cent. Promo codes can also be applied here.

<image src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652476651/p5/Screenshot_from_2022-05-13_22-17-01_zatn5t.png">

<image src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652476874/p5/Screenshot_from_2022-05-13_22-20-17_oe3qad.png">


## Checkout Page <p id="checkout"></p>

The checkout page is a standard billing form with a stripe card element. On successful payment a webhook marks the order as payed and a confirmation email is sent.

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652477225/p5/Screenshot_from_2022-05-13_22-25-59_imeku5.png">

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652477273/p5/Screenshot_from_2022-05-13_22-26-27_wev39g.png">

Declined payments are redirected back to the basket summary after giving the user reason for declined payment.

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652477439/p5/Screenshot_from_2022-05-13_22-30-11_qzqcuh.png">


## Newsletter <p id="newletter"></p>

I decided to make the admin panel a more integrated and useful part of the site. In one sense I felt like it would be great to design a custom admin dashboard but on the other, the admin panel is such a strong out of the box feature of django and it seemed a little redundant to reinvent the wheel so to speak. 

The site makes use of signals for a few things, but a good example is the admin newsletter. Anybody in the subscription list will be sent a post save signal email.Neat and elegant solution.

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652477742/p5/Screenshot_from_2022-05-13_22-00-15_o3llud.png">

<img src="https://res.cloudinary.com/daniel-callaghan/image/upload/v1652477787/p5/Screenshot_from_2022-05-13_22-01-28_sugmjy.png">

## Features to Impliment <p id="features-left"></p>

### Wishlist
This was a feature I almost included in the project but I decided to leave it out as it was not part of my original plans/user stories. My last project had a lot of feature creep and it was a goal not to repeat that for this project.

### Book Club 
I would like to set up django channels and a forum to allow users to set up and host book club meetings. 

### Instant Chat 
A bot or real person to be available to answer customer questions in real time.

### Subscription based model of payment 
A monthly subscription for access to all books would be a great idea. 

</section>

<section id="testing"> 

# Testing 

Testing can be found [here](TESTING.md)

</section>


<section id="tech">

# Technologies Used 

[Gitpod](https://www.gitpod.io) 
- IDE (Intigrated Development Environment)

[Github](https://www.github.com)
- remote repository hosting platform

[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) | [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) | [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) |  [python](https://www.python.org/) 

- Languages Used to make the site

[Jquery](https://jquery.com/) | [django](https://www.djangoproject.com/)  

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

The site is deployed on [Heroku](https://www.heroku.com/). The link is here: https://e-biblio.herokuapp.com/


Steps to deploy the site on Heroku:

- in code editor add requirements for Heroku to install by typing the following commands into the terminal:
  - pip3 freeze > requirements.txt

- create a Procfile in the same directory as manage.py and paste in the following:
  - web: gunicorn ebiblio.wsgi

- create a runtime.txt file and add the following:
  - python-3.8.13

- in settings.py add Heroku to allowed hosts
  
- commit and push changes

- log in to Heroku or make an account
- click create a new app in the top right corner
- name your app and choose the region you live in
- in the resources tab of your app dashboard add the Postgres database resource
- in the settings tab click reveal config vars and add the following
  - DATABASE_URL (added automatically)
  - EMAIL_PASS - the app uses google, steps to set up app passwords found [here](https://support.google.com/accounts/answer/185833?hl=en)
  - EMAIL_USER - Email account address
  - SECRET_KEY - can be anything
  - Stripe variables: Create or log into your stripe account and in the developer section find the following variables.
    - STRIPE_ENDPOINT_SECRET - your stripe endpoint secret
    - STRIPE_PUBLISH_KEY - your stripe publishable key
    - STRIPE_SECRET_KEY - your stripe secret key
  - For AWS services you will need the following. Log into aws or create an account.
    - AWS_ACCESS_KEY_ID - your access key
    - AWS_SECRET_ACCESS_KEY - secret aws access key
    - AWS_STORAGE_BUCKET_NAME - an s3 storage bucket
    - a full walkthrough can be found [here](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html)
- Install the Heroku CLI
- in the terminal type: heroku git:remote -a yourappname
- save and commit to git then type: git push heroku main to start building
- More details can be found [here](https://devcenter.heroku.com/articles/git)
- if the build fails in heroku dashboard of your app, in the top right corner click the 'more' button and check logs to get an indication of the problem
- In  stripe you will also need to set up a webhook.
    - click webhooks, add
    - select listen for intent.payment_succeded in the dropdown
    - add your website url + /webhook
- Click the view app button to see the app


How to fork the repository
- Go to [github.com](https://www.github.com) and log in.
- Search Ebibliop5 or go to https://github.com/xiaoniuniu89/ebibliop5
- in the top right of the page click the "fork" button
- you will now have a copy of the repository in your GitHub account.

How to clone the repository
- Go to [github.com](https://www.github.com)
- Log in to account
- navigate to https://github.com/xiaoniuniu89/ebibliop5
- Click the green code button that says Clone or download 
- to copy from HTTPS copy URL link "HTTPS". 
- open terminal
- go to the directory where you want to save the files
- type git clone and paste the link
- Press enter and the clone will be created
- To install the dependencies required to run the app, in the terminal type: pip3 install -r requirements.txt
- create a .env file in the root directory and in it, import os
- add the following environment variables in the .env file, refer to deployment to heroku section above for advice on obtaining the values for these environment variables:
  - os.environ["SECRET_KEY"] =
  - os.environ["EMAIL_USER"] =
  - os.environ["EMAIL_PASS"] =
  - os.environ["AWS_ACCESS_KEY_ID"] =
  - os.environ["AWS_SECRET_ACCESS_KEY"] =
  - os.environ["AWS_STORAGE_BUCKET_NAME"] =
  - os.environ['DEVELOPMENT'] = 'DEVELOPMENT'
  - os.environ['STRIPE_PUBLISH_KEY'] =
  - os.environ['STRIPE_SECRET_KEY'] =
  - os.environ['STRIPE_ENDPOINT_SECRET'] =
  - for the database there are two options:
    - 1) In settings.py use the commented out sql lite database
    - 2) os.environ["DATABASE_URL"] = <'postgresdatabaseurlhere'>
- create a superuser in the terminal by typing: python3 manage.py createsuperuser
- run the server by typing: python3 manage.py runserver
- use the superuser credentials to log into the site

More detailed instructions can be found [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository#cloning-a-repository-to-github-desktop)


# Credits <p id="credits"></p>

## Media

### Images

CTA image: https://unsplash.com/photos/VEoUWF2iQlQ

404 image: https://unsplash.com/photos/Guo9gNFpwgw

### Books

All books, including their pdf and covers were gotten from the following website:

https://www.idplr.com/141-ebooks


They are all from the free ebooks section

## Code

I had a lot of help from tutorials and bootstrap examples throughout this project. 

- [very academy](https://www.youtube.com/watch?v=UqSJCVePEWU&list=PLOLrQ9Pn6caxY4Q1U9RjO1bulQp5NDYS_)
  - This is a brilliant walkthrough of a bookstore. It was full of help on how to make a django site more dynamic and I learned how to make ajax calls from this tutorial, a lot about database design and setting up stripe webhooks. 
- [Corey Schafer](https://www.youtube.com/watch?v=kt3ZtW9MXhw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=16)
  - A great walkthrough of django basics that I still go back to. I used his walkthrough to help me set up my AWS bucket.
- [star rating](https://bbbootstrap.com/snippets/star-rating-pure-css-19646372)
  - A great bootstrap example I was able to work into my project.
- [Bootstrap Examples](https://getbootstrap.com/docs/5.2/examples/checkout/)
  - I used a lot of the examples on the bootstrap site, a good example is this checkout page I modified for my purposes.
- [bootstrap snippets](https://snippets.wrappixel.com/bootstrap-basic-feature/)
  - A great site full of snippets to give inspiration and borrow from and work into your own project. Borrowed heavily for CTA.
- [Image resize](https://blog.soards.me/posts/resize-image-on-save-in-django-before-sending-to-amazon-s3/)
  - Solution to resize images before uploading to S# bucket


## Aknowledgements
- My mentor Precious who is always so patient and full of great ideas and can always find a way to break my site and help me find bugs.
- My wife CC for testing the site and listening to my blah blah blah about the technical aspects of the site.



