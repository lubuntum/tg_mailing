var filter = document.getElementById('select-filter');
var send = document.getElementById('select-send');
var filterInput = document.getElementById('filter-input');
var sendInput = document.getElementById('send-input');
var fileName = document.getElementById('file-name');

filter.addEventListener('change', function() {
    if (this.checked) {
        send.checked = false;
    }
});

send.addEventListener('change', function() {
    if (this.checked) {
        filter.checked = false;
    }
});

window.addEventListener('scroll', function() {
    filter.checked = false;
    send.checked = false;
});

filter.addEventListener('change', function() {
    if (this.checked) {
        function clickHandler(event) {
            if (!filterInput.contains(event.target)) {
                filter.checked = false;
                document.removeEventListener('click', clickHandler);
            }
        };
        document.addEventListener('click', clickHandler);
    }
});

send.addEventListener('change', function() {
    if (this.checked) {
        function clickHandler(event) {
            if (!sendInput.contains(event.target)) {
                send.checked = false;
                document.removeEventListener('click', clickHandler);
            }
        };
        document.addEventListener('click', clickHandler);
    }
});