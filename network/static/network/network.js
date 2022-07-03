function editpost(postid) {
    
    console.log(postid);
    console.log(`I want to change content of button${postid}`);

    // Get button and change its text (innerHTML)
    let buttontochange = document.getElementById(`button${postid}`);

    // Get post and change its text (innerHTML)
    let posttochange = document.getElementById(`post${postid}`);
    let postcontent = posttochange.innerHTML;
  
    // If user clicks on "edit post", change the post to a text area prefileld with current post
    
    if (buttontochange.innerHTML === "Edit post") {
        // Backup buttontochange.innerHTML = `Save changes on button nº ${postid}`;
        buttontochange.innerHTML = 'Save changes';
        buttontochange.className = "buttonedit btn btn-success mb-2";
        posttochange.innerHTML = `<textarea id="${postid}new">${postcontent}</textarea>`;
    
    // Give the user the possibility to edit their post and save it with JS
    } else {
        buttontochange.innerHTML = "Edit post";
        buttontochange.className = "buttonedit btn btn-light mb-2";
        // TODO Save new content in DB by fetch  
        let postchanged = document.getElementById(`${postid}new`);
        posttochange.innerHTML = postchanged.value;
        postchangedvalue = postchanged.value

        // Update post content on database
        // Test Fetch PUT form P3-mail --- post_id, newcontent
        fetch(`/post/${postid}/${postchangedvalue}`, {
            method: 'PUT',
            body: JSON.stringify({
            "post": postchangedvalue
            })
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

        // TODO fetch / Update DB
        // POST MODEL : add 1 to the total amount of likes for this post
        fetch(`/addlike/${postid}`, {
            method: 'PUT'            
        })
        .then(response => {
            console.log(response);
        })

        // LIKE MODEL : add entry with this user liking this post

    } else {
        likecount.innerHTML = parseInt(likecount.innerHTML) - 1;
        buttonlike.innerHTML = 'Like Post';
        buttonlike.className = "buttonedit btn btn-primary mb-2";

        // TODO fetch / Update DB
        // POST MODEL : delete 1 to the total amount of likes for this post
        fetch(`/deletelike/${postid}`, {
            method: 'PUT'            
        })
        .then(response => {
            console.log(response);
        })
        // LIKE MODEL : delete the existing entry with this user liking this post

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

        // TODO fetch / Update DB
        // POST MODEL : add 1 to the total amount of likes for this post
        fetch(`/addlike/${postid}`, {
            method: 'PUT'            
        })
        .then(response => {
            console.log(response);
        })

        // LIKE MODEL : add entry with this user liking this post

    } else {
        likecount.innerHTML = parseInt(likecount.innerHTML) - 1;
        buttonlike.innerHTML = 'Like Post';
        buttonlike.className = "buttonedit btn btn-primary mb-2";

        // TODO fetch / Update DB
        // POST MODEL : delete 1 to the total amount of likes for this post
        fetch(`/deletelike/${postid}`, {
            method: 'PUT'            
        })
        .then(response => {
            console.log(response);
        })
        // LIKE MODEL : delete the existing entry with this user liking this post

    }

    
}