function set_btn() {
    lists = document.getElementsByClassName("button-list");
    for (i=0; i<lists.length; i++) {
        lists[i].children[0].style.background = "#bbb";
    }
    prices = document.getElementsByClassName("item-price");
    for (i=0; i<prices.length; i++) {
        prices[i].innerHTML=formatter.format(prices[i].innerHTML);
    }
}

function click_item(id) {
    color = document.getElementById(`color-${id}`).innerHTML;
    size = document.getElementById(`size-${id}`).innerHTML;
    model = document.getElementById(`model-${id}`).innerHTML;
    window.location.href = `/${id}?c=${color}&s=${size}&m=${model}`;
}

function change_color(id, parent, input) {
    btn(id);
    document.getElementById(`image-${parent}`).src = input;
    document.getElementById(`color-${parent}`).innerHTML = id;
}

function change_model(id, parent, input) {
    btn(id);
    document.getElementById(`price-${parent}`).innerHTML = formatter.format(input);
    document.getElementById(`model-${parent}`).innerHTML = id;
}

function change_size(id, parent) {
    btn(id);
    document.getElementById(`size-${parent}`).innerHTML = id;
}

set_btn();
