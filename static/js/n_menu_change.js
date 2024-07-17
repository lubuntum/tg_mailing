var filter = document.getElementById('select-filter');
var send = document.getElementById('select-send');

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