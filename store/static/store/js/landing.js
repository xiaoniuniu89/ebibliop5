// remove fixed top for landing cta
document.querySelector('nav').classList.remove('fixed-top');
document.querySelector('body').style.paddingTop = '0px';


// intersection observers 
const cta = document.querySelector('.cta');
const ctaTxt = document.querySelector('.cta-txt');
const nav = document.querySelector('nav');

const heroOptions = {
    rootMargin: "-150px 0px 0px 0px"
};

// function to watch for scroll down to the popular this month book section on the landing page
// when that happens, the navbar will reappear and have a fixed top, it will also add padding to the body to
// prevent the navbar from suddenly obscuring the books.
const heroObserver = new IntersectionObserver((entries, heroObserver) => {
    entries.forEach(entry => {
        if(!entry.isIntersecting){
                nav.classList.add('fixed-top');
                nav.style.opacity = '1';
                cta.style.marginBottom = "110px";
            }

         else {
            nav.classList.remove('fixed-top');
        }
    });
}, heroOptions);

// this is to control the opacity of the navbar to allow it to fade in and out
const navObserver = new IntersectionObserver((entries, navObserver) => {
    entries.forEach(entry => {
        if(!entry.isIntersecting){
            nav.style.opacity = '0';
                
            }

         else {
            nav.style.opacity = '1';
        }
    });
}, heroOptions);



heroObserver.observe(cta);
navObserver.observe(ctaTxt);
