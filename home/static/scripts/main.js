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
