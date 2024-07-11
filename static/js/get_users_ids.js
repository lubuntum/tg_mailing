$(document).ready(function() {
    $('.checkboxed-all').on('click', function() {
        var idList = [];
        var isChecked = $(this).is(':checked');
        if($('.checkboxed-all').is(':checked')) {
            $('.user-checkbox').each(function() {
                $('.user-checkbox').prop('checked',true);
                $('.user-checkbox').closest('td').css('background-color', '#818cd5');
            });
        } else {
            $('.user-checkbox').prop('checked',false);
            $('.user-checkbox').closest('td').css('background-color', '');
        };
        $('.user-checkbox').each(function() {
            if($('.user-checkbox').is(':checked')) {
                var id = $(this).closest('tr').find('td:eq(1)').text();
                idList.push({
                    'id': id
                });
            };
        });
        var data = {
            'idList': idList,
            'checked': isChecked}
        $.ajax({
            url: '/get_all_data',
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                console.log(response);
            }
        });
    });
});

$(document).ready(function() {
    $('.user-checkbox').on('click', function() {
        if($(this).is(':checked')) {
            $(this).closest('td').css('background-color', '#818cd5');
        } else {
            $(this).closest('td').css('background-color', '');
        };
        var id = $(this).closest('tr').find('td:eq(1)').text();
        var isChecked = $(this).is(':checked');
        var data = {
            'id': id,
            'checked': isChecked
        };
        $.ajax({
            url: '/get_data',
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                console.log(response);
            }
        });
    });
});
