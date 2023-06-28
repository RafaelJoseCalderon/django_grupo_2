function cleanLebel(id) {
    document.getElementById(id).value = '';
}

const classNames = {
    node: 'form-control border-0 p-0',
};

const i18n = {
    months: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
    weekdays: ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"],
    time: ["Tiempo", "Inicio", "Fin"],
}

const parseDate = (value, input) => {
    if (typeof value === 'string' || value instanceof String) {
        let array_ = input.value.split('-');
        return new Date(array_[0], array_[1] - 1, array_[2]);
    } else {
        return value;
    }
};

const serialize = (data, input) => {
    let data_ = parseDate(data, input);
    return data_.getFullYear() + '-' + (data_.getMonth() + 1) + '-' + data_.getDate();
}

const deserialize = (string, input) => {
    return new Date(parseDate(string, input));
}

function setDatepickers(inputs) {
    inputs.forEach(input => {
        let attrs = {
            classNames: classNames,
            i18n: i18n,
            serialize: (data) => serialize(data, input),
            deserialize: (string) => deserialize(string, input),
        };

        if (input.getAttribute('date-picker-min')) {
            attrs.min = input.getAttribute('date-picker-min');
        }

        if (input.getAttribute('date-picker-max')) {
            attrs.min = input.getAttribute('date-picker-max');
        }

        new Datepicker(`#${input.id}`, attrs);
    });
}

let inputs = document.querySelectorAll('input[date-picker="simple"]');
(() => {setDatepickers(inputs)})();
