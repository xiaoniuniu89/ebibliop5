const addReview = (user, review, rating) => {
    document.querySelector('#add-review-modal-btn').disabled = true
    document.querySelector('.temp-review-wrapper').innerHTML = `
<div class="media row  text-muted py-3 col-12 bg-light border-top">
    <strong class="d-block text-gray-dark">@${user} - </strong>
    <i class="fas fa-star mx-1 "><p class="c-rate">${rating}</p></i>
    <div class="edit-delete-comment">
        <i data-toggle="modal" data-target="#update-review-modal" id="edit-review-btn" class="fas px-2 fa-edit"></i>
        <i data-toggle="modal" data-target="#delete-review-modal" id="delete-review-btn" class="fas fa-trash-alt"></i>
    </div>  
</div>
<div id="temp-review" style="white-space: pre-wrap;" class="row new-line border-bottom pb-3 mb-0 border-gray bg-light col-12">${review}</div>
`
}

const updateReview = (user, review, rating) => {
    if(document.getElementById('user-review-info-wrapper')){

        if(! document.getElementById('user-review-info-wrapper').innerHTML == ''){
            document.getElementById('user-review-info-wrapper').innerHTML = ''
        }
    }
    document.querySelector('.temp-review-wrapper').innerHTML = `
<div class="media row  text-muted py-3 col-12 bg-light border-top">
    <strong class="d-block text-gray-dark">@${user} - </strong>
    <i class="fas fa-star mx-1 "><p class="c-rate">${rating}</p></i>
    <div class="edit-delete-comment">
        <i data-toggle="modal" data-target="#update-review-modal" id="edit-review-btn" class="fas px-2 fa-edit"></i>
        <i data-toggle="modal" data-target="#delete-review-modal" id="delete-review-btn" class="fas fa-trash-alt"></i>
    </div>  
</div>
<div style="white-space: pre-wrap;" class="row new-line border-bottom pb-3 mb-0 border-gray bg-light col-12">${review}</div>
`

}

const deleteReview = () => {
    if(document.getElementById('user-review-info-wrapper')){
        if(! document.getElementById('user-review-info-wrapper').innerHTML == ''){
            document.getElementById('user-review-info-wrapper').innerHTML = ''

        }else{
        document.querySelector('.temp-review-wrapper').innerHTML = ''
        document.querySelector('#add-review-modal-btn').disabled = false
    }    
    }else{
        document.querySelector('.temp-review-wrapper').innerHTML = ''
        document.querySelector('#add-review-modal-btn').disabled = false
    }
    document.querySelector('#add-review-modal-btn').disabled = false
}