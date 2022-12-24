Array.from(document.getElementsByClassName("link")).forEach(function (link) {
    let animationName = "link-flickering-animation-";

    "webkitAnimationEnd mozAnimationEnd animationend".split(" ").forEach(function (event) {
        // Makes link available for another animation on hover
        link.addEventListener(event, function () {
            for (let n = 1; n <= 3; n++) {
                link.classList.remove(animationName + n);
            }
        });
    });

    link.addEventListener('mouseover', function () {
        // Sets a random animation on hover
        let randomNumberAnimation = Math.floor(Math.random() * 3 + 1);
        link.classList.add(animationName + randomNumberAnimation);
    }, false);
});

function changeBackground() {
    let element = document.getElementById("landing")
    let backgroundUrl = getComputedStyle(element, "::before").getPropertyValue("background-image");
    let currentBackgroundNumber = parseInt(backgroundUrl.charAt(backgroundUrl.length - 7))
    let nextBackgroundNumber = currentBackgroundNumber < 4 ?  currentBackgroundNumber + 1 : 1

    console.log(nextBackgroundNumber)
    console.log(backgroundUrl)

    element.style.setProperty("--background-url", `url(\"/static/images/background-${nextBackgroundNumber}.jpg\")`)
}

setInterval(changeBackground, 5750);

document.addEventListener("mousemove", function (event) {
    // Parallax background image
    let x = (event.pageX - window.innerWidth / 2) / 35 * -1
    let y = (event.pageY - window.innerHeight / 2) / 35 * -1

    document.getElementById("landing").style.setProperty("--background-transform", `translateX(${x}px) translateY(${y}px) scale(1.1)`)
})
