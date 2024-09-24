function count_end_price() {
    end_price = 0;
    items = document.getElementsByClassName('item');
    for (i=0; i<items.length; i++) {
        end_price += Number(items[i].querySelector('#big-price').innerHTML);
    }
    document.getElementById('end-price').innerHTML = `Итоговая цена: ${formatter.format(end_price)}`;
}


function bucket_response(response) {
    item = document.getElementById(`item-${response['order']}`);
    item.querySelector('#bucket-count').innerHTML = response['count'];
    price = item.querySelector('#small-price').innerHTML;
    big_price = response['count'] * price;
    item.querySelector('#big-price-text').innerHTML = "Цена заказа: " + formatter.format(big_price);
    item.querySelector('#small-price-text').innerHTML = "(" + formatter.format(price) + "/штука)";
    item.querySelector('#big-price').innerHTML = big_price;
    count_end_price();
}
function bucket(act, id, color, size, model) {
    send_data({id:id, color:color, size:size, model:model, act:act}, bucket_response);
}
function set_btn() {
    items = document.getElementById("items").children;
    for (i=0; i<items.length; i++) {
        id = items[i].querySelector("#id").innerHTML;
        color = items[i].querySelector("#color").innerHTML;
        size = items[i].querySelector("#size").innerHTML;
        model = items[i].querySelector("#model").innerHTML;
        bucket('act',id,color,size,model);
    }
}


function order_response(response) {
    if (response['success']) {
        window.location.href = "/user";
    }
}
function order() {
    adress = document.getElementById("adress").value;
    send_data({act:"order", adress:adress}, order_response);
}

set_btn();

map = new window.CDEKWidget({
    from: 'Тамбов',
    root: 'cdek-map',
    apiKey: 'd90168b6-e285-4154-be1a-993a71979fb3',
    servicePath: '/service.php',
    defaultLocation: 'Тамбов',
    popup: true,
    hideDeliveryOptions: {
        office: false,
        door: true,
    },
    onChoose() {
        alert('Доставка выбрана');
    },
});

map.open();
