var ids = []

$(document).ready(function() {
    $('#all-user-checkbox').on('click', function() {
        if (this.checked) {
            ids = []
            $('.user-checkbox').each(function() {
                $('.user-checkbox').prop('checked', true)
                idToPush = $(this).closest('tr').find('td:eq(1)').text()
                ids.push(parseInt(idToPush))
            })
            console.log(ids)
        } else {
            $('.user-checkbox').each(function() {
                $('.user-checkbox').prop('checked', false)
                ids = []
            })
            console.log(ids)
        }
    })
})

$(document).ready(function() {
    $('.user-checkbox').on('click', function() {
        if (this.checked) {
            $(this).prop('checked', true)
            idToPush = $(this).closest('tr').find('td:eq(1)').text()
            ids.push(parseInt(idToPush))
            console.log(ids)
        } else {
            $(this).prop('checked', false)
            indexToDelete = ids.indexOf(parseInt($(this).closest('tr').find('td:eq(1)').text()))
            if (indexToDelete > -1) {
                ids.splice(indexToDelete, 1)
            }
            console.log(ids)
        }
    })
})