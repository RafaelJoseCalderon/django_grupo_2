
var width_fl;
function reziseUsereContent(width) {
    if (width >= 768 && width_fl === undefined) {
        width_fl = true; horizontal();
    }

    if (width < 768 && width_fl === undefined) {
        width_fl = false; vertical();
    }

    if (width >= 768 && width_fl) {
        width_fl = false; horizontal();
    }

    if (width < 768 && !width_fl) {
        width_fl = true; vertical();
    }
}

function horizontal() {
    if(document.getElementById('ctn')) {
        let pane = document.getElementById('ctn').classList;

        pane.remove('vertical')
        pane.add('horizontal')
    }
}

function vertical() {
    if(document.getElementById('ctn')) {
        let pane = document.getElementById('ctn').classList;

        pane.remove('horizontal')
        pane.add('vertical')
    }
}

// notas diacionales en 'ss_base.html'
const resizeObserver = new ResizeObserver((entries) => {
    entries.forEach(entry => {
        if (entry && entry.contentRect) {
            let width = entry.contentRect.width;
            let x = entry.contentRect.x;
    
            reziseUsereContent(width + 2 * x);
        }
    })
});

(() => resizeObserver.observe(document.getElementById('usuario')))();