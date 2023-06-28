function setLebel(id, files) {
    if (files) {
        document.getElementById(`${id}_label`).innerHTML = files.name;
    }
};