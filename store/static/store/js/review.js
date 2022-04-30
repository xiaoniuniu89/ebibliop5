const addReview = (user, review, rating) => {
    document.querySelector('#add-review-modal-btn').disabled = true
    document.querySelector('.temp-review-wrapper').innerHTML = `
<div class="media row  text-muted pt-3">
    <p class="media-body pb-3 mb-0 small lh-125 ">
    <strong class="d-block text-gray-dark">@${user} - ${rating}.0</strong>
    </p>
</div>
<div style="white-space: pre-wrap;" class="row new-line border-bottom pb-3 mb-0 border-gray">${review}</div>
`
}