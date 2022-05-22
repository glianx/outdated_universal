function createCard(img_src,title,content) {
    const card =    
    `
    <div class="col s12 m4">
        <div class="card my_width">
            <div class="card-image my_height">
                <img src="images/${img_src}.png">
            </div>
        <div class="my_padding red white-text">
            <h6 style='font-weight: bold;'>${title}</h6>
        </div>
        <div class="my_padding red darken-3 white-text">
            <p>${content}</p>
        </div>
    </div>
    </div>
    `;
    return card

}

const course_imgs = ["ms","py2","yh2"]
const course_titles = ["Magic Square","Pythagorean Theorem","Yang Hui's Triangle"]
const course_descriptions = ["Learn to solve an interactive Magic Square",
                             "Find a geometric proof for the Pythagorean Theorem",
                             "Learn to find patterns in Yang Hui's Triangle"]
const cd = document.getElementById("cardDisplay")

for (i=0;i<course_imgs.length;i++) {
    new_card_div = document.createElement("div")
    new_card_div.innerHTML = createCard(course_imgs[i],course_titles[i],course_descriptions[i]);
    cd.appendChild(new_card_div)
}


