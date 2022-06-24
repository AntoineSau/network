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
            const postedby  = document.getElementById(this.dataset.postedby);
            const date  = document.getElementById(this.dataset.date);
            const time  = document.getElementById(this.dataset.time);
            const likes  = document.getElementById(this.dataset.likes);

            // alert(this.dataset.page);
            console.log(`Click on post ${this.dataset.post}`);
            console.log(`Click on post ${this.dataset.id}`);

            // Modify current post to a NEW FORM with pre-filled data
            id.innerHTML = 
            `
                <form id="editedform"">
                    <b>Posted by: ${this.dataset.postedby}</a>
                    <!-- Test of putting id to post so we can modify it later wiht its id -->
                    <input name="postid" type="hidden" value="${this.dataset.id}">
                    <textarea class="form-control" name="modifiedpost" rows="3" required>${this.dataset.post}</textarea >
                    <p></p>
                    <br>
                    <b>Date:</b> ${this.dataset.date}
                    <br>
                    <b>Time:</b> ${this.dataset.time}
                    <br>
                    <b>Likes:</b> ${this.dataset.likes}
                    <br>
                    <button type="button" onclick="console.log('I want to save change on ${this.dataset.id}')" id="new ${this.dataset.id}" class="buttonsave btn btn-secondary mb-2">Save changes</button>

                </form>
                
            `;

            

        }
    })

    

    
});