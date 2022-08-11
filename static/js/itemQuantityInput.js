 // Decrement quantity button
 document.querySelector('.decrement-qty').onclick = function(event) {
    event.preventDefault();
    let closestInput = this.closest('.input-group').querySelector('.qty-input');
    let currentValue = parseInt(closestInput.value);
    // if (currentValue > closestInput.getAttribute('min')) {
    //     closestInput.value = currentValue - 1;
    // }
    closestInput.value = currentValue - 1;
    let form = document.getElementById('update-qty-form')
    // form.submit()
}

// Increment quantity button
document.querySelector('.increment-qty').onclick = function(event) {
    event.preventDefault();
    let closestInput = this.closest('.input-group').querySelector('.qty-input');
    let currentValue = parseInt(closestInput.value);
    if (currentValue < closestInput.getAttribute('max')) {
        closestInput.value = currentValue + 1;
    }
    let form = document.getElementById('update-qty-form')
    // form.submit()
}