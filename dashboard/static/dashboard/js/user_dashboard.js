const contentDivs = document.querySelectorAll('.content-div');
const dashTabs = document.querySelectorAll('.nav-link');

// simple function to add/remove active class in dashboard tabs
// active will show contents of that tab and make the tab oranage.
dashTabs.forEach((tab) => {
    tab.addEventListener('click', (e) => {
    dashTabs.forEach((tab) => {
        tab.classList.remove('active');
        e.target.classList.add('active');
    });
    contentDivs.forEach((div) => {
        div.classList.remove('show');
        div.classList.add('hide');
    });
    
    document.querySelector(`#${e.target.id}-div`).classList.add('show');
    });
});