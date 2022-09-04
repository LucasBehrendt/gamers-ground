 // Decrement quantity button
 document.querySelectorAll('.decrement-qty').forEach((button) => {
    button.addEventListener('click', (event) => {
        event.preventDefault();
        let itemId = button.getAttribute('data-item_id');
        let closestInput = button.closest('.input-group').querySelector('.qty-input');
        let currentValue = parseInt(closestInput.value);
        closestInput.value = currentValue - 1;
        let form = document.getElementById(`update-qty-form-${itemId}`);
        form.submit();
    });
});

// Increment quantity button
document.querySelectorAll('.increment-qty').forEach((button) => {
    button.addEventListener('click', (event) => {
        event.preventDefault();
        let itemId = button.getAttribute('data-item_id');
        let closestInput = button.closest('.input-group').querySelector('.qty-input');
        let currentValue = parseInt(closestInput.value);
        if (currentValue < closestInput.getAttribute('max')) {
            closestInput.value = currentValue + 1;
        }
        let form = document.getElementById(`update-qty-form-${itemId}`);
        form.submit();
    });
});

// update manual input in quantity form
document.querySelectorAll('.qty-input').forEach((itemQty) => {
    let currentValue = itemQty.value;
    itemQty.onchange = function() {
        if (parseInt(itemQty.value) || itemQty.value == 0) {
            if (parseInt(itemQty.value) >= 0 && parseInt(itemQty.value) <= parseInt(itemQty.getAttribute('max'))) {
                let itemId = itemQty.getAttribute('data-item_id');
                let form = document.getElementById(`update-qty-form-${itemId}`);
                form.submit();
            } else {
                itemQty.value = currentValue;
            }
        } else {
            itemQty.value = currentValue;
        }
    };
});