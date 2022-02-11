let menutoggle = document.querySelector('.toggle');
menutoggle.onclick = () => {
    menutoggle.classList.toggle('active')
}
let header = document.querySelector(".header")
let header__link = document.querySelectorAll(".header__link")
let flag = 0
let burger = document.querySelector(".header__burger")
console.log(burger.getAttribute);

window.onscroll = () => {
    if (pageYOffset >= 450) {
        header.style.color = 'black'
        for (let item of header__link) {
            item.style.color = 'black'
        }
    } else {
        header.style.color = 'white'
        for (let item of header__link) {
            item.style.color = 'white'
        }
    }

    if (pageYOffset >= 3800 && flag == 0) {
        flag = 1
        $('.count_number').each(function() {
            $(this).prop('Counter', 0).animate({
                Counter: $(this).text()
            }, {
                duration: 4000,
                easing: 'swing',
                step: function(now) {
                    $(this).text(Math.ceil(now));
                }
            });
        });
    }
}

let news = document.querySelectorAll(".news-item")

for(let item of news) {
    item.onclick = () => {
        let et = event.target
        et.classList.toggle("news_active")
        et.lastElementChild.classList.toggle("news_active")
        et.lastElementChild.previousElementSibling.classList.toggle("news_active")
    }
}

let questions = document.querySelectorAll(".question")

for( let item of questions) {
    item.onclick = () => {
        let et = event.target
        let answer = et.lastElementChild.previousElementSibling.firstElementChild.lastElementChild
        let button = et.lastElementChild.previousElementSibling.lastElementChild
        if ($(".questions-wrapper").hasClass("one")) {
            $(".answer").slideUp(300)
            $(".answer-button").removeClass("button_active")
            $(".question").not($(et)).removeClass("active")
        }
        if ($(et).hasClass("active")) {
            $(answer).slideUp(100)
            button.classList.remove("button_active")
            et.classList.remove("active")
        } else {
            et.classList.add("active")
            button.classList.add("button_active")
            $(answer).slideToggle(300)
        }
    }
}

const anchors = document.querySelectorAll('a.scroll-to')

for (let anchor of anchors) {
  anchor.addEventListener('click', function (e) {
    e.preventDefault()
    
    const blockID = anchor.getAttribute('href')
    
    document.querySelector(blockID).scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    })
  })
}

let burger_button = document.querySelector(".toggle")

burger_button.onclick = () => {
    let menu = document.querySelector(".header__menu")
    menu.classList.toggle("burger_active")
    event.target.classList.toggle("active")
}