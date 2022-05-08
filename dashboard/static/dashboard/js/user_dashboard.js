const dash = document.querySelector('.dash-wrapper')
const dashContentDiv = document.querySelector('.dash-tab-content-wrapper')
const contentDivs = document.querySelectorAll('.content-div')
const dashTabs = document.querySelectorAll('.nav-link')

dash.addEventListener('click', (e) => {
    dashTabs.forEach((tab) => {
        tab.classList.remove('active')
        e.target.classList.add('active')
    })
    contentDivs.forEach((div) => {
        div.classList.remove('show')
        div.classList.add('hide')
    })
    
    document.querySelector(`#${e.target.id}-div`).classList.add('show')
})