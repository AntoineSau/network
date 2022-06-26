function editpost(postid) {
    
    console.log(postid);
    console.log(`I want to change content of button${postid}`);
    
    // Get button and change its text (innerHTML)
    let buttontochange = document.getElementById(`button${postid}`);

    // Get post and change its text (innerHTML)
    let posttochange = document.getElementById(`post${postid}`);
    let postcontent = posttochange.innerHTML;

    // If user clicks on "edit psot", change the post to a text area prefileld with current post
    
    if (buttontochange.innerHTML === "Edit post") {
        buttontochange.innerHTML = `Save changes on button nº ${postid}`;
        buttontochange.className = "buttonedit btn btn-secondary mb-2";
        posttochange.innerHTML = `<textarea id="${postid}new">${postcontent}</textarea>`;
    
    // Give the user the possibility to edit theri psot and save it with JS
    } else {
        buttontochange.innerHTML = "Edit post";
        buttontochange.className = "buttonedit btn btn-primary mb-2";
        // TODO Save new content in DB by fetch  
        let postchanged = document.getElementById(`${postid}new`);
        posttochange.innerHTML = postchanged.value; 

    // TODO: need to udapte post content on database
    
    }

    
}