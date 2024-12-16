function updateCartUI(data) {
        let counters = document.getElementsByClassName("cart-counter");
        for (let c of counters)
            c.innerText = data.total_quantity;

        let amounts = document.getElementsByClassName("cart-amount");
        for (let c of amounts)
            c.innerText = data.total_amount.toLocaleString();
}

function addToCart(id, name, price) {
    fetch('/api/carts', {
        method: "POST",
        body: JSON.stringify({
            "id": id,
            "name": name,
            "price": price
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(res => res.json()).then(data => {
        updateCartUI(data);
    })
}

function updateCart(productId, obj) {
    fetch("/api/carts/${productId}", {
        method: "get",
        body: JSON.stringify({
            "quantity": obj.value
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(res => res.json()).then(data => {
        updateCartUI(data);
    })
}

function deleteCart(productId) {
    if (confirm("Bạn có chắc chắn muốn xóa không?") == true) {
        fetch("/api/carts/${productId}", {
        method: "delete"
    }).then(res => res.json()).then(data => {
        updateCartUI(data);

        document.getElementsById('cart${productId}').style.display = none;
    });
    }
}

//window.onload = function() {
//    let buttons = document.getElementsByClassName("booking");
//    for (let b of buttons)
//        b.onclick = function() {
//
//        }
//}