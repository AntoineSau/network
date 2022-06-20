// Wait for page to loaded:
document.addEventListener('DOMContentLoaded', function() {

    // Check if user clicked on edit post
    document.querySelectorAll('.buttonedit').forEach(button => {

        // When a button is clicked, switch to that page
        button.onclick = function() {
            // alert(this.dataset.page);

            // Trying to get element by ID and change its properties
            const elem = document.getElementById(this.dataset.page);
            elem.innerHTML = `<textarea>${this.dataset.page}</textarea> <br> <button class="buttonsave btn btn-primary mb-2">SAVE</button>`;

            // How do I retreive post's id?

        }
    })
});