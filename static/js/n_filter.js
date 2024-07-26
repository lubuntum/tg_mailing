var filterData = {};

/*Применить фильтрацию*/
$(document).ready(function() {
    $('#submit-filter').click(function(){
        filterData = {
            'filterType': 0,
            'personAgeFrom': $('#age-range-from').val(),
            'personAgeTo': $('#age-range-to').val(),
            'childAgeFrom': $('#child-age-range-from').val(),
            'childAgeTo' : $('#child-age-range-to').val(),
            'languages': $('.language-checkbox:checked').map(function() {
                return $(this).attr('id')
            }).get()
        }
        console.log(filterData);
        handleFilterData(filterData);
    });
})


/*Сбросить фильтрацию*/
$(document).ready(function() {
    $('#reset-filter').click(function(){
        $('#age-range-from').val(1);
        $('#age-range-to').val(99);
        $('.language-checkbox').each(function() {
            $(this).prop('checked',false);
        });
        filterData = {
            'filterType': 1,
            'personAgeFrom': $('#age-range-from').val(),
            'personAgeTo': $('#age-range-to').val(),
            'languages': $('.language-checkbox:checked').map(function() {
                return $(this).attr('id')
            }).get()
        }
        console.log(filterData);
        handleFilterData(filterData);
    });
})


/*Отправка запроса на бэк и получение новых данных для таблицы и дальнейшего ее отображения*/
function handleFilterData(filterData) {
    $('#all-user-checkbox').prop('checked',false);
    $('.user-checkbox').each(function() {
        $(this).prop('checked',false);
    });
    $.ajax({
        url: '/filter_data',
        type: 'POST',
        data: JSON.stringify(filterData),
        contentType: 'application/json',
        success: function(htmlData) {
            var table = $('.reset-table');
            table.empty();
            $('.reset-table').html(htmlData);
        }
    })
}