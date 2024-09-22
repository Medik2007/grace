function bucket_response(response) {
    document.getElementById('bucket-count').innerHTML = response['count'];
}
function bucket(act) {
    id = document.getElementById(`id`).innerHTML;
    color = document.getElementById(`color`).innerHTML;
    size = document.getElementById(`size`).innerHTML;
    model = document.getElementById(`model`).innerHTML;
    send_data({id:id, color:color, size:size, model:model, act:act}, bucket_response);
}


function url_vars()
{
    vars = [];
    hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(i=0; i<hashes.length; i++)
    {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}
function set_btn() {
    vars = url_vars();
    document.getElementById(`button-${vars['c']}`).click();
    document.getElementById(`button-${vars['s']}`).click();
    document.getElementById(`button-${vars['m']}`).click();
    bucket('load');
}


function change_color(id, input) {
    document.getElementById("main-image").src = input;
    document.getElementById("color").innerHTML = id;
    bucket('load');
    btn(id);
}
function change_model(id, input) {
    document.getElementById("price-text").innerHTML = formatter.format(input);
    document.getElementById("model").innerHTML = id;
    bucket('load');
    btn(id);
}
function change_size(id) {
    document.getElementById("size").innerHTML = id;
    bucket('load');
    btn(id);
}


set_btn();
set_price("price-text");
