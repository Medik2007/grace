const formatter = new Intl.NumberFormat('ru-RU', {
    style:'currency',
    currency:'RUB',
});

function send_data(data, success, url='', csrf=true) {
    if (csrf) {data.csrfmiddlewaretoken=document.getElementById("csrf").value;}
    $.ajax({
        type: 'POST',
        url: url,
        data: data,
        success: success,
        error: function(error) {
            console.log('Send data error:', error);
        }
    });
}

function btn(id) {
    obj = document.getElementById(`button-${id}`)
    buttons = obj.parentNode.children;
    for (i=0; i<buttons.length; i++) {
        buttons[i].style.background = "#ddd";
    }
    obj.style.background = "#bbb";
}
