(function($) {
    $(document).on('formset:added', function(event, $row, formsetName) {
        if (formsetName == 'opcao_set') {
            form_idx = $row['0']['rowIndex'] - 1;
            console.log(formsetName);
            var stringOfHtml = $('#'+$row['0']['id']).html().replace(/__prefix__/g, form_idx)
            $('#'+$row['0']['id']).html(stringOfHtml);
            $('#'+$row['0']['id']).find('.ql-toolbar').first().remove()
        }
    });
})(django.jQuery);