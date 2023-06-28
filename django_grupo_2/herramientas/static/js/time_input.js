function get_values(id) {
    let input_values = document.getElementById(id).value.split(':');
    return { hour: parseInt(input_values[0]), min: parseInt(input_values[1]) }
}

function set_values(id, hour, min) {
    document.getElementById(id).value = `${hour}:${min}:00`;
    document.getElementById(`${id}_hour`).innerHTML = ('00' + hour).slice(-2);
    document.getElementById(`${id}_min`).innerHTML = ('00' + min).slice(-2);
}

function up_hour(id) {
    let values = get_values(id);
    let hour = values.hour < 23 ? values.hour + 1 : values.hour;
    set_values(id, hour, values.min);
}

function down_hour(id) {
    let values = get_values(id);
    let hour = values.hour > 0 ? values.hour - 1 : values.hour;
    set_values(id, hour, values.min);
}

function up_min(id) {
    let values = get_values(id);
    let min = values.min < 59 ? values.min + 1 : values.min;
    set_values(id, values.hour, min);
}

function down_min(id) {
    let values = get_values(id);
    let min = values.min > 0 ? values.min - 1 : values.min;
    set_values(id, values.hour, min);
}
