// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
var stripe = Stripe('pk_test_51KpZBDIaE0NFUuueBYiW9whBxPp9gNq5VDqAJztk6gqjwAIvhGp6SoAJJqbNTThnOqJ0nn0ggEQnjnOcNTbCBkpk00M0XbQDYX');
const elem = document.getElementById('submit');
let clientSecret = elem.getAttribute('data-secret');


// Set up Stripe.js and Elements to use in checkout form
var elements = stripe.elements();
var style = {
base: {
  color: "#000",
  lineHeight: '2.4',
  fontSize: '16px'
}
};

var card = elements.create("card", { hidePostalCode: true, style: style });
card.mount("#card-element");


card.on('change', ({error}) => {
  let displayError = document.getElementById('card-errors');
  if (error) {
    displayError.textContent = error.message;
  } else {
    displayError.textContent = '';
  }
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
  ev.preventDefault();

var fName = document.getElementById("firstName").value;
var lName = document.getElementById("lastName").value;
var email = document.getElementById("email").value;
var addOne = document.getElementById("address").value;
var addTwo = document.getElementById("address2").value;
var country = document.getElementById("country").value;
var city = document.getElementById("state").value;
var postCode = document.getElementById("post-code").value;

$.ajax({
    type: "POST",
    url: addOrderUrl,
    data: {
      order_key: clientSecret,
      csrfmiddlewaretoken: CSRF_TOKEN,
      action: "post",
      name: `${fName} ${lName}`,
      email: email,
      address1: addOne,
      address2: addTwo,
      city: city,
      postcode: postCode,
      country: country
    },
    success: function (json) {
      console.log(json.success)

  
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
      billing_details: {
        name: `${fName} ${lName}`,
        email: email,
        address: {
          // country: country,
          line1: addOne,
          line2: addTwo,
          state: state,
          postal_code: postCode
        }
      }
    }
  }).then(function(result) {
    if (result.error) {
      // Show error to your customer (for example, insufficient funds)
      console.log(result.error.message);
    } else {
      // The payment has been processed!
      if (result.paymentIntent.status === 'succeeded') {
        console.log('payment processed')
        window.location.replace(checkoutCompleteUrl)
        // Show a success message to your customer
        // There's a risk of the customer closing the window before callback
        // execution. Set up a webhook or plugin to listen for the
        // payment_intent.succeeded event that handles any business critical
        // post-payment actions.
      }
    }
  });
    },
    error: function (xhr, errmsg, err) {},
});
});

// const promoBtn = document.querySelector('#promo-btn')
// const promoCodeInput = document.querySelector('#promo-code-input')
// const promoTextArea = document.querySelector('#promo-text-area')

// promoBtn.addEventListener('click', (e) => {
//   e.preventDefault()
//   code = promoCodeInput.value
//   promoTextArea.innerHTML = code
// })
