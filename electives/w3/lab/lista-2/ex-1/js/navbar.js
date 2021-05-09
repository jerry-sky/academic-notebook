const bodyElement = document.body;
const navbarElement = document.querySelector("nav > .standard");
const navbarListElement = document.querySelector("nav > .standard > .main");
const navbarButtonElement = document.querySelector(
    "nav > .standard > .dropdown-button"
);

navbarElement.style.display = "initial";

navbarButtonElement.onclick = function () {

    navbarListElement.classList.toggle("open");

};

const navbarApply = function (documentWidth) {

    if (documentWidth < 600) {
        navbarButtonElement.style.display = "initial";
        bodyElement.classList.remove("offset");
    } else {
        navbarButtonElement.style.display = "none";
        bodyElement.classList.add("offset");
    }

};

navbarApply(document.documentElement.offsetWidth);

window.onresize = function () {
    navbarApply(document.documentElement.offsetWidth);
};
