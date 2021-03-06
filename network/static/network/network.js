function editpost(postid) {
    
    console.log(postid);
    console.log(`I want to change content of button${postid}`);

    // Get button and change its text (innerHTML)
    let buttontochange = document.getElementById(`button${postid}`);

    // Get post and change its text (innerHTML)
    let posttochange = document.getElementById(`post${postid}`);
    let postcontent = posttochange.innerHTML;
  
    // If user clicks on "edit post", change the post to a text area prefilled with current post
    
    if (buttontochange.innerHTML === "Edit post") {
        // Backup buttontochange.innerHTML = `Save changes on button nº ${postid}`;
        buttontochange.innerHTML = 'Save changes';
        buttontochange.className = "buttonedit btn btn-success mb-2";
        posttochange.innerHTML = `<textarea id="${postid}new">${postcontent}</textarea>`;

        
    
    
    // Give the user the possibility to edit their post and save it with JS
    } else {
        buttontochange.innerHTML = "Edit post";
        buttontochange.className = "buttonedit btn btn-light mb-2";
        let postchanged = document.getElementById(`${postid}new`);
        posttochange.innerHTML = postchanged.value;
        postchangedvalue = postchanged.value

        csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value
        

        // Update post content on database with fetch
        fetch(`/post/${postid}/${postchangedvalue}`, {
            method: 'PUT',
            body: JSON.stringify({
            "post": postchangedvalue
            }),
            headers: { "X-CSRFToken": csrftoken },
            credentials : 'same-origin',
        
        })
        .then(response => {
            console.log(response);
        })
    
    }

}

function addlike(postid) {
    console.log(`Want to Like ${postid}`);
    let likecount = document.getElementById(`likecount${postid}`);
    
    let buttonlike = document.getElementById(`buttonlike${postid}`);
    if (buttonlike.innerHTML === 'Like Post') {
        likecount.innerHTML = parseInt(likecount.innerHTML) + 1;
        buttonlike.innerHTML = 'Unlike Post';
        buttonlike.className = "buttonedit btn btn-secondary mb-2";

        // POST MODEL : add 1 to the total amount of likes for this post
        fetch(`/addlike/${postid}`, {
            method: 'PUT'            
        })
        .then(response => {
            console.log(response);
        })

    } else {
        likecount.innerHTML = parseInt(likecount.innerHTML) - 1;
        buttonlike.innerHTML = 'Like Post';
        buttonlike.className = "buttonedit btn btn-primary mb-2";

        // POST MODEL : delete 1 to the total amount of likes for this post
        fetch(`/deletelike/${postid}`, {
            method: 'PUT'            
        })
        .then(response => {
            console.log(response);
        })

    }

}

function deletelike(postid) {
    console.log(`Want to Unlike ${postid}`);
    let likecount = document.getElementById(`likecount${postid}`);
    
    let buttonlike = document.getElementById(`buttonlike${postid}`);
    if (buttonlike.innerHTML === 'Like Post') {
        likecount.innerHTML = parseInt(likecount.innerHTML) + 1;
        buttonlike.innerHTML = 'Unlike Post';
        buttonlike.className = "buttonedit btn btn-secondary mb-2";

        // POST MODEL : add 1 to the total amount of likes for this post
        fetch(`/addlike/${postid}`, {
            method: 'PUT'            
        })
        .then(response => {
            console.log(response);
        })


    } else {
        likecount.innerHTML = parseInt(likecount.innerHTML) - 1;
        buttonlike.innerHTML = 'Like Post';
        buttonlike.className = "buttonedit btn btn-primary mb-2";

        // POST MODEL : delete 1 to the total amount of likes for this post
        fetch(`/deletelike/${postid}`, {
            method: 'PUT'            
        })
        .then(response => {
            console.log(response);
        })

    }

    
}