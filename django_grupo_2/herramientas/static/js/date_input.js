new Datepicker('#id_fecha', {
    classNames: { node: 'form-control border-0 p-0' },

    i18n: {
        months: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        weekdays: ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"],
        time: ["Tiempo", "Inicio", "Fin"]
    },

    min: (() => {
        return new Date();
    })(),

    max: (() => {
        var date = new Date();
        date.setDate(date.getDate() + 15);
        return date;
    })()
});