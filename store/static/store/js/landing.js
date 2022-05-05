
// intersection observers 
const cta = document.querySelector('.cta')
const ctaTxt = document.querySelector('.cta-txt')
const nav = document.querySelector('nav')

const heroOptions = {
    rootMargin: "-150px 0px 0px 0px"
};

const heroObserver = new IntersectionObserver((entries, heroObserver) => {
    entries.forEach(entry => {
        if(!entry.isIntersecting){
                nav.classList.add('fixed-top')
                nav.style.opacity = '1'
                cta.style.marginBottom = "115px"
            }

         else {
            nav.classList.remove('fixed-top')
        }
    })
}, heroOptions)

const navObserver = new IntersectionObserver((entries, navObserver) => {
    entries.forEach(entry => {
        if(!entry.isIntersecting){
            nav.style.opacity = '0'
                
            }

         else {
            nav.style.opacity = '1'
        }
    })
}, heroOptions)



heroObserver.observe(cta)
navObserver.observe(ctaTxt)


const appearOptions = {
    threshold: 0,
    rootMargin: "0px 0px -200px 0px"
}