const hour__ = 1;
const min__ = 5;

const template = [
    '<div class="triangle"></div>',
    '<div class="d-flex flex-row mp--0">',

        '<div class="d-flex flex-column">',
            '<button type="button" class="btn" time-picker="up-hour">',
                '<i class="fas fa-chevron-up"></i>',
            '</button>',
            '<span class="form-control time" time-picker="sp-hour"></span>',
            '<button type="button" class="btn" time-picker="down-hour">',
                '<i class="fas fa-chevron-down"></i>',
            '</button>',
        '</div>',

        '<span class="d-flex align-items-center">:</span>',

        '<div class="d-flex flex-column">',
            '<button type="button" class="btn" time-picker="up-min">',
                '<i class="fas fa-chevron-up"></i>',
            '</button>',
            '<span class="form-control time" time-picker="sp-min"></span>',
            '<button type="button" class="btn" time-picker="down-min">',
                '<i class="fas fa-chevron-down"></i>',
            '</button>',
        '</div>',

        '<div class="d-flex flex-column justify-content-center">',
            '<button type="button" class="btn btn-outline-secondary m-1 me-0" time-picker="now">',
                'Ahora',
            '</button>',
            '<button type="button" class="btn btn-outline-secondary m-1 me-0" time-picker="close">',
                'Cerrar',
            '</button>',
        '</div>',
    '</div>',
].join('');

function showTimepicker(input) {
    let parent = input.parentElement;
    let box = document.getElementById(`${input.id}_picker`);

    if (!box) {
        box = (new Box(input)).render();

        parent.after(box);
        setTimeout(() => box.classList.add('show'), 75);
    } else {
        box.classList.remove('show');
        setTimeout(() => box.remove(), 75);
    }
}

class Box {
    constructor(input) {
        this.input = input

        this.box = document.createElement('div');
        this.box.id = `${input.id}_picker`;
        this.box.classList.add('timepicker-content', 'fade');
        this.box.innerHTML = template;

        this.labelHour = getSpan(this.box, 'sp-hour');
        this.lableMin = getSpan(this.box, 'sp-min');

        this.values = this.getValues();
        this.setValues(this.values);

        setButton(this.box, 'up-hour', this.upHour.bind(this));
        setButton(this.box, 'down-hour', this.downHour.bind(this));

        setButton(this.box, 'up-min', this.upMin.bind(this));
        setButton(this.box, 'down-min', this.downMin.bind(this));

        setButton(this.box, 'now', this.now.bind(this));
        setButton(this.box, 'close', this.close.bind(this));
    }

    setValues(values) {
        let hour_ = ('00' + values.hour).slice(-2);
        let min_ = ('00' + values.min).slice(-2);

        this.input.value = `${hour_}:${min_}:00`;
        this.labelHour.innerHTML = `${hour_}`;
        this.lableMin.innerHTML = `${min_}`;

        this.values = values;
    };

    getValues() {
        let values = this.input.value.split(':');
        return { hour: parseInt(values[0]), min: parseInt(values[1]) };
    };

    upHour() {
        this.setValues({
            hour: this.values.hour < 23 ? this.values.hour + hour__ : this.values.hour,
            min: this.values.min
        });
    };

    downHour() {
        this.setValues({
            hour: this.values.hour > 0 ? this.values.hour - hour__ : this.values.hour,
            min: this.values.min
        });
    };

    upMin() {
        let min = this.values.min < 59 ? this.values.min + min__ : this.values.min;
        this.setValues({
            hour: this.values.hour,
            min: min === 60 ? 55 : min
        });
    };

    downMin() {
        this.setValues({
            hour: this.values.hour,
            min: this.values.min > 0 ? this.values.min - min__ : this.values.min
        });
    };

    now() {
        let date = new Date();
        this.setValues({
            hour: date.getHours(),
            min: min__ * Math.floor(date.getMinutes() / min__)
        });
    };

    close() {
        this.box.remove()
    }

    render() {
        return this.box;
    }
}

function setButton(parent, name, fnctn) {
    parent
        .querySelectorAll(`button[time-picker="${name}"]`)[0]
        .addEventListener("click", fnctn);
}

function getSpan(parent, name) {
    return parent.querySelectorAll(`span[time-picker="${name}"]`)[0];
}
