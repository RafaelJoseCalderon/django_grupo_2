
var panelRegion;
var containerRegion;

function setContainerClass(element, class_) {
    element.classList.remove(
        'width-0', 'width-1', 'width-2', 'width-3', 'width-4', 'width-5'
    );
    element.classList.add(class_);
}

function reziseUsereContent(width) {
    let panel = document.getElementById('panel');
    let container = document.getElementById('container');

    if (panel) {
        if (width >= 768 && panelRegion != 0) {
            panel.classList.add('panel-1'); panelRegion = 0;
        }
    
        if (width >= 0 && width < 768 && panelRegion != 1) {
            panel.classList.remove('panel-1'); panelRegion = 1;
        }
    }

    if (container) {
        if (width >= 1400 && containerRegion != 0) {
            setContainerClass(container, 'width-0'); containerRegion = 0;
        }
    
        if (width >= 1200 && width < 1400 && containerRegion != 1) {
            setContainerClass(container, 'width-1'); containerRegion = 1;
        }
    
        if (width >= 992 && width < 1200 && containerRegion != 2) {
            setContainerClass(container, 'width-2'); containerRegion = 2;
        }
    
        if (width >= 768 && width < 992 && containerRegion != 3) {
            setContainerClass(container, 'width-3'); containerRegion = 3;
        }
    
        if (width >= 576 && width < 768 && containerRegion != 4) {
            setContainerClass(container, 'width-4'); containerRegion = 4;
        }
    
        if (width >= 0 && width < 576 && containerRegion !== 5) {
            setContainerClass(container, 'width-5'); containerRegion = 5;
        }
    }
}

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