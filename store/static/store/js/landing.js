
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

const booksWrapper = document.querySelector('.books-wrapper')
const loader = document.querySelector('.loader')
const loadBtn = document.querySelector('#load-btn')
const loadWrapper = document.querySelector('#loading-wrapper')
let visible = 4

const handleGetData = () => {
    $.ajax({
        type: 'GET',
        url: `/books-json/${visible}/`,
        success: function(response){
            loader.classList.add('d-none')
            loadBtn.classList.remove('d-none')
            maxSize = response.max
            const data = response.data
            
            data.map(book=>{
                booksWrapper.innerHTML += `<div class="col-lg-3 col-md-4 col-sm-6 col-xs-12 py-5">
                                            <a href="shop/${book.slug}/">
                                                <div class="card product_item">
                                                    <div class="body">
                                                        <div class="cp_img">
                                                            <img src="${book.image_url}" alt="Product" class="img-fluid">
                                                        </div>
                                                        <div class="product_details">
                                                            <h5 class="card-title">${book.title}</h5>
                                                            <p class="card-text text-muted">by ${book.author}</p>
                                                            <ul class="product_price list-unstyled">
                                                                <li class="price">€${book.price}</li>
                                                            </ul>
                                                        </div>
                                                    </div>
                                                </div>
                                                </a>
                                            </div>`
            })
            if(maxSize){
                console.log('done')
                loader.classList.add('d-none')
                loadBtn.classList.add('d-none')
            }
        
        },
        error: function(error){
            console.log(error)
        }
    })
}

handleGetData()

loadBtn.addEventListener('click', ()=>{
    loadBtn.classList.add('d-none')
    loader.classList.remove('d-none')
    visible += 4
    handleGetData()

})