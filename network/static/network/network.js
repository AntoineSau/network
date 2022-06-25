function editpost(postid) {
    
    console.log(postid);
    console.log(`I want to change content of button${postid}`);
    
    // Get button and change its text (innerHTML)
    let buttontochange = document.getElementById(`button${postid}`);

    // CONDITION "on-off" If button html is Save [...] / else [...]
    
    if (buttontochange.innerHTML === "Edit post") {
        buttontochange.innerHTML = `Save changes on button nº ${postid}`;
        buttontochange.className = "buttonedit btn btn-secondary mb-2"
        
    } else {
        buttontochange.innerHTML = "Edit post";
        buttontochange.className = "buttonedit btn btn-primary mb-2"
    }

    //buttontochange.innerHTML = `Save changes on button nº ${postid}`;
    // buttontochange.className = "buttonedit btn btn-secondary mb-2"

    // TODO - change class for putting button background as grey
    

    // Change POST CONTENT BY textarea

    


}