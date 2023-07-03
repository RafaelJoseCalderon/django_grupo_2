const hour__ = 1;
const min__ = 5;

function showTimepicker(input) {
    let parent = input.parentElement;
    let box = document.getElementById(`${input.id}_picker`);

    if (!box) {
        box = newBox(input)

        parent.after(box);
        setTimeout(() => box.classList.add('show'), 75);
    } else {
        box.classList.remove('show');
        setTimeout(() => box.remove(), 75);
    }
}

function newBox(input) {
    let box = document.createElement('div');
    box.id = `${input.id}_picker`;
    box.classList.add('timepicker-content', 'fade');

    box.innerHTML = [
        '<div class="triangle"></div>',
        '<div class="d-flex flex-row mp--0">',
            '<div class="d-flex flex-column" time-picker="column"></div>',
            '<span class="d-flex align-items-center">:</span>',
            '<div class="d-flex flex-column" time-picker="column"></div>',
            '<div class="d-flex flex-column justify-content-center" time-picker="column"></div>',
        '</div>'
    ].join('');

    let list = box.querySelectorAll('div[time-picker]');
    let initVal = getValues(input);
    let labelHour = newLabel(initVal.hour);
    let lableMin = newLabel(initVal.min);

    list[0].appendChild(upHour(input, labelHour));
    list[0].appendChild(labelHour);
    list[0].appendChild(downHour(input, labelHour));

    list[1].appendChild(upMin(input, lableMin));
    list[1].appendChild(lableMin);
    list[1].appendChild(downMin(input, lableMin));

    list[2].appendChild(now(input, labelHour, lableMin));
    list[2].appendChild(close(box));
    return box;
}

function newLabel(value) {
    let label = document.createElement('span')
    label.classList.add('form-control', 'time');
    label.innerHTML = ('00' + value).slice(-2);

    return label;
}

function newButton(inner, classList, fnctn) {
    let button = document.createElement('button');

    button.type = 'button';
    button.innerHTML = inner;
    button.addEventListener('click', fnctn);

    classList.forEach(element => {
        button.classList.add(element);
    });

    return button;
}

function getValues(input) {
    let values = input.value.split(':');
    return { hour: parseInt(values[0]), min: parseInt(values[1]) };
}

function upHour(input, label) {
    return newButton('<i class="fas fa-chevron-up"></i>', ['btn'], () => {
        let values = getValues(input);
        setHour(input, label, {
            hour: values.hour < 23 ? values.hour + hour__ : values.hour,
            min: values.min
        });
    });
}

function downHour(input, label) {
    return newButton('<i class="fas fa-chevron-down"></i>', ['btn'], () => {
        let values = getValues(input);
        setHour(input, label, {
            hour: values.hour > 0 ? values.hour - hour__ : values.hour,
            min: values.min
        });
    });
}

function setHour(input, label, values) {
    let hour_ = ('00' + values.hour).slice(-2);
    let min_ = ('00' + values.min).slice(-2);

    input.value = `${hour_}:${min_}:00`;
    label.innerHTML = `${hour_}`;
}

function upMin(input, label) {
    return newButton('<i class="fas fa-chevron-up"></i>', ['btn'], () => {
        let values = getValues(input);
        setMin(input, label, {
            hour: values.hour,
            min: values.min < 59 ? values.min + min__ : values.min
        });
    });
}

function downMin(input, label) {
    return newButton('<i class="fas fa-chevron-down"></i>', ['btn'], () => {
        let values = getValues(input);
        setMin(input, label, {
            hour: values.hour,
            min: values.min > 0 ? values.min - min__ : values.min
        });
    });
}

function setMin(input, label, values) {
    let hour_ = ('00' + values.hour).slice(-2);
    let min_ = ('00' + values.min).slice(-2);

    input.value = `${hour_}:${min_}:00`;
    label.innerHTML = `${min_}`;
}

function now(input, labelHour, lableMin) {
    return newButton('Ahora', ['btn', 'btn-outline-secondary', 'm-1', 'me-0'],
        () => {
            let date = new Date();
            let values = {
                hour: date.getHours(),
                min: min__ * Math.floor(date.getMinutes() / min__)
            }
            
            setHour(input, labelHour, values);
            setMin(input, lableMin, values);
        }
    );
}

function close(box) {
    return newButton('Cerrar', ['btn', 'btn-outline-secondary', 'm-1', 'me-0'],
        () => {
            box.remove();
        }
    );
}