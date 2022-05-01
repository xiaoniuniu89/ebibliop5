const addReview = (user, review, rating) => {
    document.querySelector('#add-review-modal-btn').disabled = true
    document.querySelector('.temp-review-wrapper').innerHTML = `
<div class="media row  text-muted py-3 col-9">
    <strong class="d-block text-gray-dark">@${user} - </strong>
    <i class="fas fa-star mx-1 "><p class="c-rate">${rating}</p></i>
    <div class="edit-delete-comment">
        <i id="edit-review-btn" class="fas px-2 fa-edit"></i>
        <i data-toggle="modal" data-target="#delete_review_modal" id="delete-review-btn" class="fas fa-trash-alt"></i>
    </div>  
</div>
<div style="white-space: pre-wrap;" class="row new-line border-bottom pb-3 mb-0 border-gray">${review}</div>
`
}

const deleteReview = () => {
    if(document.getElementById('user-review-wrapper')){
        document.getElementById('user-review-wrapper').innerHTML = ''
    }else{
        document.querySelector('.temp-review-wrapper').innerHTML = ''
    }
    
    document.querySelector('#add-review-modal-btn').disabled = false
}