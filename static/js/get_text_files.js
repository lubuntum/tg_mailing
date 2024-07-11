var allFiles = [];
$(document).ready(function() {
    var fileInput = document.getElementById('file-input');

    fileInput.addEventListener('change', function(e) {
        var files = e.target.files;

        if (allFiles.length + files.length > 5) {
            alert('Вы можете загрузить только 5 файлов');
            return;
        }

        for (var i = 0; i < files.length; i++) {
            var file = files[i];
            if (file.size > 10 * 1024 * 1204) {
                continue;
            }
            var listItem = $(`<li class="file-name"><button class="file-delete" id="file-delete">Удалить</button>${file.name}</li>`)
            $('#file-output').append(listItem);
            allFiles.push(file);
        }
        updateFilesCounter();
    });

    $('#file-output').on('click', '#file-delete', function() {
        var fileName = $(this).parent().text().trim().replace('Удалить', '');
        $(this).parent().remove();
        var index = allFiles.findIndex(function(file) {
            return file.name === fileName;
        });
        if (index !== -1) {
            allFiles.splice(index, 1)
        }
        updateFilesCounter();
    });

    function updateFilesCounter() {
        var counter = allFiles.length;
        $('#files-counter').text(counter)
    }
});

$(document).ready(function() {
    $('#delay-send-message').click(function(){
        alert('Ты нажал на кнопку');
        var datetimeValue = $('#date-input').val();
        var date = moment(datetimeValue, 'YYYY-MM-DDTHH:mm').toDate();
        var formatedDate = moment(date).format('DD.MM.YYYY');
        var formatedTime = moment(date).format('HH:mm')

        var formData = new FormData();
        formData.append('date', formatedDate);
        formData.append('time', formatedTime);

        var messageText = $('#text-area').val();
        if (messageText === '') {
            alert('Чтобы отправить сообщение сначала нужно его ввсети в поле "Текст рассылки"!');
            return;
        }
        formData.append('messageText', messageText)

        addFilesToFormData(formData)

        $.ajax({
            url: '/delay_message',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                console.log(response);
                if (response === '_war: /send_message. Список пользователей пуст!') {
                    alert('Не выбран(ы) пользователи для отправки сообщения!');
                } else {
                    alert('Сообщение успешно доставлено пользователям!');
                }
            }
        });
    })
    $('#send-message').click(function() {
        
        var formData = new FormData();
        addFilesToFormData(formData);
        /*
        if (allFiles.length !== 0) {
            for (var i = 0; i < allFiles.length; i++) {
                formData.append('files', allFiles[i]);
                console.log(allFiles[i])
            }
        }
        */
        var messageText = $('#text-area').val();
        if (messageText === '') {
            alert('Чтобы отправить сообщение сначала нужно его ввсети в поле "Текст рассылки"!');
            return;
        }
        formData.append('messageText', messageText);

        $.ajax({
            url: '/send_message',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                console.log(response);
                if (response === '_war: /send_message. Список пользователей пуст!') {
                    alert('Не выбран(ы) пользователи для отправки сообщения!');
                } else {
                    alert('Сообщение успешно доставлено пользователям!');
                }
            }
        });
    });
});

function addFilesToFormData(formData) {
        if (allFiles.length !== 0) {
            for (var i = 0; i < allFiles.length; i++) {
                formData.append('files', allFiles[i]);
                console.log(allFiles[i])
            }
        }
}

