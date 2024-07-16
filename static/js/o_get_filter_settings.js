$(document).ready(function() {
    $('#submit-settings').click(function() {
        var filterData = {
            'selectInput': $('#person-type').val(),
            'fromTextInput': $('#age-from').val(),
            'toTextInput': $('#age-to').val(),
            'checkboxInput': $('.language-checkbox:checked').map(function() {
                return $(this).val();
            }).get()
        };
        $.ajax({
            url: '/filter_and_refresh_data',
            type: 'POST',
            data: JSON.stringify(filterData),
            contentType: 'application/json',
            success: function(data) {
                var table = $('#user-datatable');
                table.empty();
                $('#user-datatable').html(data);
            }
        });
    });
});

$(document).ready(function() {
    $('#reset-settings').click(function() {
        $('#person-type').val('empty');
        $('#age-from').val(1);
        $('#age-to').val(99);
        $('.language-checkbox').each(function() {
            $(this).prop('checked',false);
        });
        var filterData = {
            'selectInput': 'empty',
            'fromTextInput': '1',
            'toTextInput': '99',
            'checkboxInput': []
        };
        $.ajax({
            url: '/filter_and_refresh_data',
            type: 'POST',
            data: JSON.stringify(filterData),
            contentType: 'application/json',
            success: function(data) {
                var table = $('#user-datatable');
                table.empty();
                $('#user-datatable').html(data);
            }
        });
    });
});