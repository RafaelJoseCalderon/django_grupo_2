const navbar = document.getElementById('navbar');
const navbarContainer = document.getElementById('navbar-container');

const navbarColor = () => {
    let scrollTop = window.scrollY;
    let winHeight = window.innerHeight;
    let base = 2 * scrollTop / winHeight;

    if (scrollTop < 0.5 * winHeight) {
        navbar.style.backgroundColor = `rgb(69, 82, 110, ${base})`;
    } else {
        navbar.style.backgroundColor = 'rgb(69, 82, 110)';
    }
}

class NavBarCollapsebles {
    constructor(varargin) {
        this.button = document.getElementById(varargin.button);
        this.container = document.getElementById(varargin.container);
        this.layerColor = varargin.containerColor;
        this.layerClassColor = varargin.containerClassColor;

        this.button.addEventListener('click', this.toggle);
    }

    toggle = () => {
        if (this.button.getAttribute('data-collapsed') === 'true') {
            this.button.setAttribute('data-collapsed', 'false');
            this.layerColor.classList.add(this.layerClassColor);

            this.show(this.container);
        } else {
            this.button.setAttribute('data-collapsed', 'true');
            this.layerColor.classList.remove(this.layerClassColor);

            this.hide(this.container);
        }
    }

    show = element => {
        element.classList.remove('collapse');
        element.classList.add('collapsing');
        element.style.height = '0px';
    
        this.executeAfterTransition(() => {
            element.classList.remove('collapsing');
            element.classList.add('collapse', 'show');
            element.style.height = '';
        }, element);
    
        element.style.height = element.scrollHeight + 'px';
    };
    
    hide = element => {
        element.style.height = element.scrollHeight + 'px';
        element.offsetHeight;
        element.classList.add('collapsing');
        element.classList.remove('collapse', 'show');
    
        element.style.height = '';
        this.executeAfterTransition(() => {
            element.classList.remove('collapsing');
            element.classList.add('collapse');
        }, element);
    };

    executeAfterTransition = (callback, transitionElement) => {
        const emulatedDuration = this.getTransitionDurationFromElement(transitionElement) + 5;
    
        let called = false;
        const handler = ({ target }) => {
            if (target !== transitionElement) return;
            called = true;
            transitionElement.removeEventListener('transitionend', handler);
            callback();
        };
    
        transitionElement.addEventListener('transitionend', handler);
        setTimeout(() => {
            if (!called) transitionElement.dispatchEvent(new Event('transitionend'));
        }, emulatedDuration);
    };

    getTransitionDurationFromElement = element => {
        let { transitionDuration, transitionDelay } = window.getComputedStyle(element);
    
        const floatTransitionDuration = Number.parseFloat(transitionDuration);
        const floatTransitionDelay = Number.parseFloat(transitionDelay);
    
        if (!floatTransitionDuration && !floatTransitionDelay) return 0;
    
        transitionDuration = transitionDuration.split(',')[0];
        transitionDelay = transitionDelay.split(',')[0];
    
        return (Number.parseFloat(transitionDuration) + Number.parseFloat(transitionDelay)) * 1000;
    };
}

(() => {
    if (document.getElementById('img-head')) {
        navbarColor();

        document.addEventListener('scroll', () => {
            navbarColor();
        });
    } else {
        let header = document.getElementById('header');

        header.classList.add('sticky-top');
        header.classList.remove('fixed-top');
        navbar.classList.add('navbar-color');
    }

    new NavBarCollapsebles(
        {
            button: 'button-toggler',
            container: 'navbar-collapse',
            containerColor: navbarContainer,
            containerClassColor: 'layer-collapse-color'
        }
    );

    new NavBarCollapsebles(
        {
            button: 'button-dropdown',
            container: 'dropdown-collapse',
            containerColor: navbarContainer,
            containerClassColor: 'layer-dropdown-color'
        }
    );

})();
