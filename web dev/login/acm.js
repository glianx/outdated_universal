users = ["a@a","a2@a","a3@a"]
passwords = ["1","2","3"]
skill_levels = ["Advanced","Beginner","Medium"]

current_user = ""
current_userindex = -1

const login_form = document.querySelector("#login_form")
const new_user_form = document.querySelector("#new_user_form")

const login_nav = document.getElementById("login_nav")
const logout_nav = document.getElementById("logout_nav")
const math_nav = document.getElementById("math_nav")
const history_nav = document.getElementById("history_nav")

const home_content = document.getElementById("home")
const math_content = document.getElementById("math")
const history_content = document.getElementById("history")

document.addEventListener('DOMContentLoaded', function() {

    options = {
        startingTop: "0%",
        endingTop: "20%",
        inDuration: 50,
        outDuration: 50,
    };

    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, options);
});


new_user_form.addEventListener("submit", (e) => {

    e.preventDefault()
    email = new_user_form["user_name2"].value
    pw = new_user_form["user_password2"].value
    pwc = new_user_form["user_password_c"].value
    skill_level = new_user_form["group1"].value
    console.log(skill_level)
     
    new_email = true
    // check if email used
    for (i=0;i<users.length;i++) {
        if (email===users[i]) {
            new_email = false
            break
        }
    }

    if (new_email===true) {
        // check if passwords match
        if (pw===pwc) {
            alert("new user created!")
            users.push(email)
            passwords.push(pw)
            skill_levels.push(skill_level)
            console.log(users)
            console.log(passwords)
            console.log(skill_levels)
        }
        else {
            alert("passwords don't match")
        }
    }
    else {
        alert("email already used")
    }

    var singleModalElem = document.querySelector('#new_user_modal');
    var instance = M.Modal.getInstance(singleModalElem); 
    instance.close(); 
});

login_form.addEventListener("submit", (e) => {

    e.preventDefault();

    email = login_form["user_name"].value
    password = login_form["user_password"].value

    login_form["user_name"].value = ""
    login_form["user_password"].value = ""
    // login_form.reset()
    
    valid = false;

    // check if username and password in array
    for (i = 0; i < users.length; i = i + 1) {
        if (users[i] === email && passwords[i] === password) {
            valid = true;
            current_user = email;
            current_userindex = i;
            break;
        }
    }

    //Step 3: 
    //	If valid - update page 
    //	If not valid - notify user.
    if (valid === true) {
        alert("you're in!");
        var singleModalElem = document.querySelector('#login_modal');
        var instance = M.Modal.getInstance(singleModalElem); 
        instance.close(); 
    }
    else {
        alert("wrong")
    }


});

math_nav.addEventListener("click",(e) => {
    //console.log(e);

    //Step 1: Hide all sections that contain content
    home_content.style.display = "none"
    history_content.style.display = "none"

    math_content.style.display = "block"
});

//To have the system logout we need to bind a click event to the logout button and then 
//reset the state of the nav bar. What we have not done in this project is store the
//user information.  This could be userful later if you need to remember what the user is doing

logout_nav.addEventListener("click",(e) => {

        nav_objects = [math_nav,history_nav,logout_nav];
            for (let i = 0; i < nav_objects.length; i++) {
                nav_objects[i].style.display = "none"
            }

        login_nav.style.display = "block"
        new_user_nav.style.display = "block"

        current_user = ""
        current_userindex = -1			
});