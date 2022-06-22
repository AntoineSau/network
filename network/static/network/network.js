// Wait for page to loaded:
document.addEventListener('DOMContentLoaded', function() {

    // Check if user clicked on edit post
    document.querySelectorAll('.buttonedit').forEach(button => {

        // When a button is clicked, change data
        button.onclick = function() {
            
            // Trying to get element by ID and change its properties
            // Retrieving at the same time the id of the post we want to modify
            const id = document.getElementById(this.dataset.id);
            const post = document.getElementById(this.dataset.post);
            // alert(this.dataset.page);
            console.log(`Click on post ${this.dataset.post}`);
            // Change current by pre-fileld text area
            post.innerHTML = `<textarea>${this.dataset.id}</textarea>`;
            // Modify text on existing save button 
            id.innerHTML = `<button data-post="{{post.id}}" data-page="{{post.post}}" class="buttonedit btn btn-secondary mb-2">Save changes in post ${this.dataset.post}</button>`
            
            // CREATE NEW FORM WITH FETCH ACTION

            // Stop forms form submitting -> return false
            
        }
    })

    

});