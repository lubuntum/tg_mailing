$(document).ready(function() {
    $('#all-user-checkbox').change(function(){
        if(this.checked) {
            $('.user-checkbox').prop('checked', true);
        } else {
            $('.user-checkbox').prop('checked', false);
        }
    });
    console.log(true);
})