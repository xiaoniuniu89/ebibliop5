const addReview = (user, review, rating) => {
    document.querySelector('#add-review-modal-btn').disabled = true
    document.querySelector('.temp-review-wrapper').innerHTML = `
<div class="media row  text-muted pt-3">
    <strong class="d-block text-gray-dark">@${user} - </strong>
    <i class="fas fa-star mx-1 "><p class="c-rate">${rating}</p></i>
</div>
<div style="white-space: pre-wrap;" class="row new-line border-bottom pb-3 mb-0 border-gray">${review}</div>
`
}