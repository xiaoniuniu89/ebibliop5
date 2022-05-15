// this is called from store/templates/snippets/modals/create_review.html
// as part of ajax success post function 
const addReview = (user, review, rating) => {
    
    // disable so user can't submit a second review
    document.querySelector('#add-review-modal-btn').disabled = true;
    if(document.getElementById('user-review-info-wrapper')){
        //check if there was already a review when page was loaded
        if(! document.getElementById('user-review-info-wrapper').innerHTML == ''){
            document.getElementById('user-review-info-wrapper').innerHTML = '';
        }
    }
    // add json response variables to the DOM in the review section
    document.querySelector('.temp-review-wrapper').innerHTML = `
<div class="media row  text-muted py-3 col-12 bg-light border-top">
    <strong class="d-block text-gray-dark">@${user} - </strong>
    <i class="fas fa-star mx-1 "><span class="c-rate">${rating}</span></i>
    <div class="edit-delete-comment">
        <i data-toggle="modal" data-target="#review-modal" id="edit-review-btn" class="fas px-2 fa-edit"></i>
        <i data-toggle="modal" data-target="#delete-review-modal" id="delete-review-btn" class="fas fa-trash-alt"></i>
    </div>  
</div>
<div id="temp-review" style="white-space: pre-wrap;" class="row new-line border-bottom pb-3 mb-0 border-gray bg-light col-12">${review}</div>
`;
};

const updateReview = (user, review, rating) => {
    // check if there is a div from a review from page load
    if(document.getElementById('user-review-info-wrapper')){

        // if there is a review there, empty the div
        if(! document.getElementById('user-review-info-wrapper').innerHTML == ''){
            document.getElementById('user-review-info-wrapper').innerHTML = '';
        }
    }
    // add review to a seperate div that stores the review in a temp div
    document.querySelector('.temp-review-wrapper').innerHTML = `
<div class="media row  text-muted py-3 col-12 bg-light border-top">
    <strong class="d-block text-gray-dark">@${user} - </strong>
    <i class="fas fa-star mx-1 "><span class="c-rate">${rating}</span></i>
    <div class="edit-delete-comment">
        <i data-toggle="modal" data-target="#update-review-modal" id="edit-review-btn" class="fas px-2 fa-edit"></i>
        <i data-toggle="modal" data-target="#delete-review-modal" id="delete-review-btn" class="fas fa-trash-alt"></i>
    </div>  
</div>
<div style="white-space: pre-wrap;" class="row new-line border-bottom pb-3 mb-0 border-gray bg-light col-12">${review}</div>
`;

};

const deleteReview = () => {
    // check for review div from page load
    if(document.getElementById('user-review-info-wrapper')){
        // if its got something inside then empty the div
        if(! document.getElementById('user-review-info-wrapper').innerHTML == ''){
            document.getElementById('user-review-info-wrapper').innerHTML = '';

        }else{
        // incase of div from page load, but subsequently deleted and another review was added in temp review div
        document.querySelector('.temp-review-wrapper').innerHTML = '';
        // empty it and make the add review button usable again
        document.querySelector('#add-review-modal-btn').disabled = false;
    }    
    }else{
        // incase no div from page load, this means the review is in the temporary div for reviews
        document.querySelector('.temp-review-wrapper').innerHTML = '';
        // empty it and make the add review button usable again
        document.querySelector('#add-review-modal-btn').disabled = false;
    }
    document.querySelector('#add-review-modal-btn').disabled = false;
    elem.setAttribute('data-action', 'post');
    let action = elem.getAttribute('data-action');
};