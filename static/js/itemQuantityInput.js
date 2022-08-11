 // Decrement quantity button
 document.querySelectorAll('.decrement-qty').forEach((button) => {
    button.addEventListener('click', (event) => {
        event.preventDefault();
        let closestInput = button.closest('.input-group').querySelector('.qty-input');
        let currentValue = parseInt(closestInput.value);
        if (currentValue > closestInput.getAttribute('min')) {
            closestInput.value = currentValue - 1;
        }
        let form = document.getElementById('update-qty-form');
        // form.submit();
    });
});

// Increment quantity button
document.querySelectorAll('.increment-qty').forEach((button) => {
    button.addEventListener('click', (event) => {
        event.preventDefault();
        let closestInput = button.closest('.input-group').querySelector('.qty-input');
        let currentValue = parseInt(closestInput.value);
        if (currentValue < closestInput.getAttribute('max')) {
            closestInput.value = currentValue + 1;
        }
        let form = document.getElementById('update-qty-form');
        // form.submit();
    });
});