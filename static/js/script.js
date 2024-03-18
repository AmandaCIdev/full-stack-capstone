// Selecting elements
const editButtons = document.querySelectorAll(".btn-edit-custom");
const reviewText = document.getElementById("id_body");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.querySelectorAll(".btn-delete-custom");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("review_id");
        let reviewContent = document.getElementById(`review${reviewId}`).innerText;
        reviewText.value = reviewContent;
        submitButton.innerText = "Update";
        reviewForm.setAttribute("action", `edit_review/${reviewId}`);
    });
}

/**
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("review_id");

        deleteConfirm.href = `delete_review/${reviewId}`;

        deleteModal.show();
    });
}

document.getElementsByClassName('flip-card-inner-custom').forEach(card => {
    card.addEventListener('click', function () {
        this.classList.toggle('flipped');
    });
});