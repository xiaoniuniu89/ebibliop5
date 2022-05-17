# Code Validation

## HTML

HTML was validated through <a href='https://validator.w3.org/#validate_by_input' target='_blank'>The W3C Markup Validator</a>. There are no errors in the HTML.

- <a href='https://validator.w3.org/nu/?doc=https%3A%2F%2Fe-biblio.herokuapp.com%2F' target='_blank'>Landing</a>

- <a href='https://validator.w3.org/nu/?doc=https%3A%2F%2Fe-biblio.herokuapp.com%2Fshop%2Fhow-to-build-your-brand-with-instagram-images-5f705bd2-1657-4966-aa6f-975c57fce585%2F' target='_blank'>Product Detail Page</a>

- <a href='https://validator.w3.org/nu/?doc=https%3A%2F%2Fe-biblio.herokuapp.com%2Fbrowse%2Fmotivation%2F' target='_blank'>Category</a>

- <a href='https://validator.w3.org/nu/?doc=https%3A%2F%2Fe-biblio.herokuapp.com%2Fbasket%2F' target='_blank'>Basket</a>


- checkout

<img src='https://res.cloudinary.com/daniel-callaghan/image/upload/v1652623960/p5/Screenshot_from_2022-05-15_15-11-38_fdkr0b.png'/>

- checkout complete 

<img src='https://res.cloudinary.com/daniel-callaghan/image/upload/v1652624207/p5/Screenshot_from_2022-05-15_15-16-16_jqkjob.png'/>

- <a href='https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fe-biblio.herokuapp.com%2Fcheckout%2F404' target='_blank'>Error - eg: 404</a>

- User Dashboard 

<img src='https://res.cloudinary.com/daniel-callaghan/image/upload/v1652624446/p5/Screenshot_from_2022-05-15_15-20-15_anog7u.png'/>

## CSS

The css was validated through the <a href='https://jigsaw.w3.org/css-validator/'>W3 Jigsaw</a> validator. There are no errors in the css.

- <a href='https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fe-biblio.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#warnings' target='_blank'>Landing</a>

- <a href='https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fe-biblio.herokuapp.com%2Fshop%2Fhow-to-build-your-brand-with-instagram-images-5f705bd2-1657-4966-aa6f-975c57fce585%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en' target='_blank'>Product Detail</a>

- <a href='https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fe-biblio.herokuapp.com%2Fbasket%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en' target='_blank'>Basket</a>

Table of individual CSS files by direct input method in Jigsaw Validator. 

<img src='https://res.cloudinary.com/daniel-callaghan/image/upload/v1652626097/p5/Screenshot_from_2022-05-15_15-47-38_aciiod.png'/>

## Javascript

Javascript was tested using <a href='https://jshint.com/'>JS Hint</a>. To accommodate the Jquery and ES6 used on the site you must click configuration in the top right of JS Hint landing page and add these to the config. 

The JS can only be validated by direct input which causes some unused variable errors. This only arises because the templates are very compartmentalized. A variable may be declared in one snippet and referenced in a different JS file. An example of this is getting the CSRF token or Stripe client secret. The variable is accessed in the django template and set as a js variable. Then in a seperate js file the variable may be used. Testing the JS file will say the variable does not exist when in fact it does exist, and can be referenced from the django template.

- navbar.js

<img src='https://res.cloudinary.com/daniel-callaghan/image/upload/v1652627287/p5/Screenshot_from_2022-05-15_16-05-36_xdintr.png'/>

- footer.js

<img src='https://res.cloudinary.com/daniel-callaghan/image/upload/v1652627367/p5/Screenshot_from_2022-05-15_16-06-44_bistha.png'/>

- store/landing.js

<img src='https://res.cloudinary.com/daniel-callaghan/image/upload/v1652627645/p5/Screenshot_from_2022-05-15_16-13-34_qvzkqn.png'/>

- store/review.js

<img src='https://res.cloudinary.com/daniel-callaghan/image/upload/v1652628399/p5/Screenshot_from_2022-05-15_16-25-36_o30l65.png'/>

- dashboard/user_dashboard.js

<img src='https://res.cloudinary.com/daniel-callaghan/image/upload/v1652628664/p5/Screenshot_from_2022-05-15_16-30-04_pemgbr.png'/>


- checkout/checkout.js

<img src='https://res.cloudinary.com/daniel-callaghan/image/upload/v1652628906/p5/Screenshot_from_2022-05-15_16-34-26_yk5o4d.png'/>


## Python

I used <a href='https://pypi.org/project/autopep8/'>Auto pep8</a> to fix validation errors with any of the python files I, myself wrote. I then went through each file and manually inputed them into <a href='http://pep8online.com/'>pep8 online</a>. There are no errors in any of my custom written python code, although there would be in some of the files set up by django, eg. SETTINGS.py.

- [store](https://youtu.be/WSpHSB5V7-0)
- [promotions](https://youtu.be/Ncmuh-3Ib08)
- [orders](https://youtu.be/bx4meVcUWDA)
- [dashboard](https://youtu.be/YjdWUqPF6Bk)
- [checkout](https://youtu.be/bKSyAsvHgTA)
- [basket](https://youtu.be/PBagkZnhLhE)

# Automated Testing <p id="automated"></p>

Automated testing was done using the Django built in testing and with a library called <a href='https://coverage.readthedocs.io/en/6.3.3/'>coverage</a> to help pinpoint some areas of code that were not being reached by my tests.

Coverage provides a handy report and html file containing all code covered by tests.

The HTML can be found in htmlcov/index.html

To run tests, in the termianl type: 
- python3 manage.py test



Coverage Report

<img src='https://res.cloudinary.com/daniel-callaghan/image/upload/v1652631045/p5/Screenshot_from_2022-05-15_17-07-36_yxbtyz.png'/>

<img src='https://res.cloudinary.com/daniel-callaghan/image/upload/v1652631105/p5/Screenshot_from_2022-05-15_17-07-42_ovzwvt.png'/>


# Manual Testing <p id="manual"></p>

For the purposes of manual testing I will test the user stories.

- As a user, I can create an account to access the site for easier checkout in the future.
  - User clicks sign-up
  - User enters details and checks email confirmation
  - User follows email confirmation link and can now use their details to sign in.

- As a user, I can reset my password in case I lose it
  - User clicks login
  - User clicks forgot password
  - User enters email and checks email
  - User follows password reset link and changes password

- As a user, I can use Google to sign up to the site so I can create an account easier.
  - User clicks login
  - User clicks Google button
  - User is redirected to google login

- As a user, there is convenient access to a contact form or email for the bookshop incase I have a complaint or problem with my experience on the site.
  - User clicks contact us link in the footer.
  - User fills in details
  - Admin is notified of contact message by email

- As the owner of the site I can make and apply promotions easily to offer discounts to my customers.
  - Admin clicks navbar link admin/promo/add promo
  - Admin fills in form
  - Promo is created

- As a user I can add items to a cart without receiving any annoying popups or prompts to keep shopping or checkout
  - User adds item to cart in product page
  - A flash message appears and fades away at 3 seconds.

- As a user I can pay by card in a secure manner to protect my sensitive information.
  - User clicks proceed to checkout from basket summary.
  - User can fill out billing details and pay by card at the end of form.

- As a user I want to have access to a download link as soon as I pay for my books.
  - User pays with card
  - User is redirected to success page.
    - If logged in success page will have link to Dashboard containing books. Will also receive email with links.
    - If not logged in user will receive an email with download links to book. 

- As a user, I can checkout as a guest, so I can buy books without setting up an account.
  - User adds books to basket
  - User clicks proceed to checkeout from basket summary
  - User pays with card
  - User gets an email with download links to purchases.

- As a user, i want to receive a confirmation email that contains a link to download my book, so I can have access to the book I just bought as well as a receipt.
  - When user completes purchase an email is sent automatically to their inbox.

- As a user, I can leave comments on products to give a detailed review and leave future customers more well-informed.
  - User navigates to product page.
  - If logged in User can leave review of a book.

- As a user, I can log into my account, see and have access to download my purchases on my dashboard.
  - user logs in
  - User goes to dashboard
  - User has access to all purchases from here.

- As a user, I can browse books by topic as I would in a real bookstore to narrow in on what I like to read faster.
  - In navbar, User clicks "Browse Selection"
  - A list of all categories of book will appear in a dropdown.

- As a user, I can receive notifications of promotions by email to keep up to date with promotions I might like in the store.
  - User clicks subscribe to our newsletter link in footer and fills in details.
  - Admin logs into admin panel and creates a new newsletter.
  - User receives newsletter in their email inbox.

- As a user I can search for a book by title or author to find books I am interested in faster.
  - User clicks search bar in navbar
  - User enters term
  - User is redirected to a page with their search results

- As a user, I can leave a rating on books to let future customers be more informed.
  - From product page, User clicks add review
  - User can leave a rating out of 5 stars here

- As the owner of the site I can make staff level permission to update content so I can delegate work.
  - In the admin panel, the admin superuser navigates to Users in the sidebar
  - Admin selects the user they would like to promote and adds to user gorup staff.

- As a staff/admin I can easily upload new items including the image and pdf to the site in a user friendly admin page so I can complete the task easily.
  - Admin or staff click admin in navbar
  - Navigate to promo or add product
  - From here can easily upload a new promo or product to the site

# Browser Testing <p id="browser"></p>

The app was tested on the following browsers:

- [Google Chrome](https://www.google.com/chrome/?brand=FHFK&gclid=CjwKCAjw092IBhAwEiwAxR1lRnrDJkW2rc2m-_DsqG2ISAAChH0tbKgopfm-3BMuide3ikPssZgvWhoCsVUQAvD_BwE&gclsrc=aw.ds)

- [Firefox](https://www.mozilla.org/en-US/firefox/) 

- [Opera](www.opera.com) 

- [Safari](https://www.apple.com/uk/safari/)

A video of site responsivness on Chrome:

https://youtu.be/U5z8nHkoJ5I

Chrome
- The site was designed and teted using Chrome from the beginning and is the standard to compare to.

Firefox
- Everything works great except for one flaw. The intersection observers don't quite work on Firefox and as a result the opacity animation is not here. When the navbar appears it is a sudden appearance rather that a gradual fade in.

Opera
- The site works and looks the same on Opera as in Chrome. No noticable difference to speak of.

Safari
- Safari has perhaps the biggest difference, especially on mobile. The style in the footer contact forms does not work so much and the buttons blend into the color of the footer which isn't great.

<img src='https://res.cloudinary.com/daniel-callaghan/image/upload/v1652634489/p5/IMG_6431_i0kemr.jpg'/>

# Bugs

- At the moment the only way to see updated rating score on a product is to refresh the page. 

- Login from the product page when clicking login to add review button brings you back to home page. This is because I want visitors to have access to as many pages as possible. A lot of pages have no @login_required decorators.

- Nothing to stop users from using a promo code over and over.

- If you try to log in using an email used through google all auth login, it does not work. Not sure how to resolve this.

<img src='https://res.cloudinary.com/daniel-callaghan/image/upload/v1652812151/p5/Screenshot_from_2022-05-17_19-28-00_pdg1pm.png'/>
