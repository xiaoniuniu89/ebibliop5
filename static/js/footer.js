const emailInput = document.querySelector('#email-input');

// add user email into into contact form automatically on click
emailInput.addEventListener('click', () => {
    emailInput.value = userEmail;
});