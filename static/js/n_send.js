
var allFiles = []

function addFilesToFormData(formData) {
    if (allFiles.length !== 0) {
        for (var i = 0; i < allFiles.length; i++) {
            formData.append('files', allFiles[i])
            console.log(allFiles)
        }
    }
}

$(document).ready(function() {
    var fileInput = document.getElementById('file-input')
    fileInput.addEventListener('change', function(event) {
        var files = event.target.files
        if (allFiles.length + files.length > 5) {
            alert('Только 5 файлов!')
            return
        }
        for (var i = 0; i < files.length; i++) {
            var file = files[i]
            if (file.size > 10 * 1024 * 1024) {
                continue
            }
            $('#file-output').append(`<li class="file-name" id="file-name"><button class="btn-file-delete" id="btn-file-delete">Удалить</button>${file.name}</li>`)
            allFiles.push(file)
        }
        console.log('Pushed files: ', allFiles)
    })

    $('#file-output').on('click', '#btn-file-delete', function() {
        var fileName = $(this).parent().text().trim().replace('Удалить', '')

        $(this).parent().remove()
        var index = allFiles.findIndex(function(file) {
            return file.name === fileName
        })
        if (index !== -1) {
            allFiles.splice(index, 1)
        }
        var fileInput = document.getElementById('file-input')
        fileInput.value = ''
        console.log('Pushed files: ', allFiles)
    })
})
//Добавить массив выбранных user
$(document).ready(function() {
    $('#send-message').click(function() {
        if (ids.length === 0) {
            alert("Выберите пользователей")
            return
        }
        var formData = new FormData()

        addFilesToFormData(formData)

        var messageText = $('#text-area').val()
        if (messageText === '') {
            alert('Введите сообщение!')
            return
        }
        formData.append('message', messageText)
        formData.append('ids', JSON.stringify(ids))

        handleFormData(formData, '/send_message')
    })
})
//Добавить массив выбранных user
$(document).ready(function() {
    $('#delay-send-message').click(function() {
        if (ids.length === 0) {
            alert("Выберите пользователей")
            return
        }
        var formData = new FormData()

        addFilesToFormData(formData)
        
        var datetimeValue  = $('#date-input').val()
        var date = moment(datetimeValue, 'YYYY-MM-DDTHH:mm').toDate()
        var formatDate = moment(date).format('DD.MM.YYYY')
        var formatTime = moment(date).format('HH:mm')
        formData.append('date', formatDate)
        formData.append('time', formatTime)

        var messageText = $('#text-area').val()
        if (messageText === '') {
            alert('Введите сообщение!')
            return
        }
        formData.append('message', messageText)
        formData.append('ids', JSON.stringify(ids))
        handleFormData(formData, '/delay_message')
    })
})

function handleFormData(formData, url) {
    $.ajax({
        url: url,
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
            console.log(response)
            alert('Сообщение доставлено!')
            clearCheckBoxes()
        }
    })
}

function clearCheckBoxes(){
    ids = []
    $('.user-checkbox').each(function() {$('.user-checkbox').prop('checked', false)})
    $('#all-user-checkbox').prop('checked', false)
}