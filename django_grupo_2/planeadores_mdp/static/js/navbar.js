function navbarColor() {
    let scrollTop = window.scrollY;
    let winHeight = window.innerHeight;

    let base = 2 * scrollTop / winHeight;
    let navbar = document.getElementById('navbar');

    if (scrollTop < 0.5 * winHeight){
        navbar.style.backgroundColor = `rgb(69, 82, 110, ${base})`;
    } else {
        navbar.style.backgroundColor = 'rgb(69, 82, 110)';
    }
}

function scrollListener() {
    document.addEventListener('scroll', () => {navbarColor()});
}

(() => {navbarColor(); scrollListener();})();