let prefixFrom = 0;

function inserForm() {
    let empty_form_clone = inline_formset.get('empty_form').cloneNode(true);
    let totalForms = inline_formset.get('totalForms')

    let list = empty_form_clone.querySelectorAll('input, select');
    let newRow = inline_formset.get('tbody').insertRow(0);

    list.forEach(element => {
        element.id = element.id.replace('__prefix__', prefixFrom);
        element.name = element.name.replace('__prefix__', prefixFrom);

        if (element.id.includes("DELETE") || element.name.includes("DELETE")) {
            let newCell = newRow.insertCell();
            let i = document.createElement('i');

            i.onclick = () => newRow.remove();

            i.classList.add('btn');
            i.classList.add('fas');
            i.classList.add('fa-times-circle');

            newCell.appendChild(i);
            newCell.classList.add('text-center');
            newCell.classList.add('align-middle');
        } else if (element.type !== 'hidden') {
            let newCell = newRow.insertCell();

            newCell.appendChild(element);
            newCell.classList.add('text-center');
            newCell.classList.add('align-middle');
        } else {
            newRow.appendChild(element);
        }
    });

    prefixFrom++;
    totalForms.value = parseInt(totalForms.value) + 1;
}

let inline_formset = new Map();
(() => {
    let table = document.getElementById('inline_formset');

    inline_formset.set('empty_form', document.getElementById('empty_form'));
    inline_formset.set('tbody', table.getElementsByTagName('tbody')[0]);

    inline_formset.set('initialForms', document.getElementById('id_actividades-INITIAL_FORMS'));
    inline_formset.set('totalForms', document.getElementById('id_actividades-TOTAL_FORMS'));
    inline_formset.set('minNumForms', document.getElementById('id_actividades-MIN_NUM_FORMS'));
    inline_formset.set('maxNumForms', document.getElementById('id_actividades-MAX_NUM_FORMS'));

    inline_formset.forEach(element => {
        element.setAttribute('autocomplete', 'off');
    })

    prefixFrom = parseInt(inline_formset.get('initialForms').value);
})();