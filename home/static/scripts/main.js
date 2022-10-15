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

// let lastCursorPosition = [0, 0];
// let isRight = false;
//
// document.addEventListener("mousemove", (event) => {
//     const X = event.pageX;
//     const Y = event.pageY;
//
//     if (lastCursorPosition[0] === 0 || lastCursorPosition[1] === 0) {
//         lastCursorPosition[0] = event.pageX;
//         lastCursorPosition[1] = event.pageY;
//         return;
//     }
//
//     const distance = Math.sqrt(
//         Math.pow(
//             X - lastCursorPosition[0], 2
//         ) + Math.pow(
//             Y - lastCursorPosition[1], 2
//         ));
//
//     if (distance < 20) {
//         return;
//     }
//
//     const foot = document.createElement("div");
//     document.body.append(foot);
//     foot.classList.add("paw");
//     foot.style.top = event.pageY + "px";
//     foot.style.left = event.pageX + "px";
//
//     if (isRight === true) {
//         foot.classList.add("paw-right");
//     }
//     isRight = !isRight;
//
//     const rotateAngle = -Math.atan2(
//         lastCursorPosition[0] - event.pageX,
//         lastCursorPosition[1] - event.pageY
//     )
//     foot.style.transform = `rotate(${rotateAngle}rad)`;
//
//     setTimeout(function () {
//         foot.style.opacity = "0";
//         setTimeout(function () {
//             foot.remove();
//         }, 300);
//     }, 400);
//
//     lastCursorPosition = [event.pageX, event.pageY];
// });