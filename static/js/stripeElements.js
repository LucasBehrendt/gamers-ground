// Get keys from template
// const stripe_publishable_key = document.getElementById('id_stripe_publishable_key').innerText.slice(1, -1);
// const client_secret = document.getElementById('id_client_secret').innerText.slice(1, -1);


// set up stripe elements & mount to template
document.addEventListener('DOMContentLoaded', async function() {
    const stripeData = await FetchData()
    const stripe = Stripe(stripeData.stripe_publishable_key);
    const options = {
        clientSecret: stripeData.client_secret,
    };
    const elements = stripe.elements(options);
    const style = {
        base: {
          color: '#212529',
          fontSize: '20px',
          '::placeholder': {
                color: 'grey'
            }
        }
    };
    const card = elements.create('card', {style: style});
    card.mount('#card-element');

    // Display validation error on the card element to user
    card.addEventListener('change', (event) => {
        let errorDiv = document.getElementById('card-errors');
        if (event.error) {
            let errorMessage = `${event.error.message}`;
            errorDiv.innerHTML = errorMessage;
        } else {
            errorDiv.innerText = "";
        }
    });

    // Handle payment form submit
    const form = document.getElementById('payment-form');
    form.addEventListener('submit', async (event) => {
        handleFormSubmit(event, form, stripeData)
    });
    async function handleFormSubmit(event, form, stripeData) {
        event.preventDefault();

        // Disable card input & submit button. Enable loading overlay
        card.update({'disabled': true});
        document.getElementById('checkout-submit').disabled = true;
        toggleLoadingOverlay(true);

        // Retrieve metadata & add to new form, post to cache_checkout_data
        // view & modify payment intent to hold metadata.
        // If response is OK, confirm card payment & submit form with data from customer.
        // If an error occurs, disable loading overlay, enable card 
        // input & buttons, and display error message to customer.
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        const saveInfo = document.getElementById('save-info').checked;
        const url = '/checkout/cache_checkout_data/';

        const cachedData = new FormData();
        cachedData.set('csrfmiddlewaretoken', csrfToken);
        cachedData.set('save_info', saveInfo);
        cachedData.set('client_secret', stripeData.client_secret);

        await fetch(url, {
            method: 'POST',
            body: cachedData,
        }).then(function(response) {
            if (response.status == 200) {
                stripe.confirmCardPayment(stripeData.client_secret, {
                    payment_method: {
                        card: card,
                        billing_details: {
                            name: `${form.first_name.value.trim()} ${form.last_name.value.trim()}`,
                            email: form.email_address.value.trim(),
                            phone: form.phone_number.value.trim(),
                            address: {
                                line1: form.street_address_1.value.trim(),
                                line2: form.street_address_2.value.trim(),
                                city: form.city.value.trim(),
                                country: form.country.value.trim(),
                            }
                        },
                    },
                    shipping: {
                        name: `${form.first_name.value.trim()} ${form.last_name.value.trim()}`,
                        phone: form.phone_number.value.trim(),
                        address: {
                            line1: form.street_address_1.value.trim(),
                            line2: form.street_address_2.value.trim(),
                            postal_code: form.postcode.value.trim(),
                            city: form.city.value.trim(),
                            country: form.country.value.trim(),
                        }
                    }
                }).then(function(result) {
                    if (result.error) {
                        const errorDiv = document.getElementById('card-errors');
                        let errorMessage = `${result.error.message}`;
                        errorDiv.innerHTML = errorMessage;
                        card.update({'disabled': false});
                        document.getElementById('checkout-submit').disabled = false;
                        toggleLoadingOverlay(false);
                    } else {
                        if (result.paymentIntent.status === 'succeeded') {
                            form.submit();
                        }
                    }
                });
            } else {
                location.reload();
            }
        })
    }
});

// Toggle overlay when processing payment
function toggleLoadingOverlay(value) {
    const overlay = document.getElementById('loading-overlay')

    if (value) {
        overlay.style.display = 'block'
    } else {
        overlay.style.display = 'none'
    }
}

// Fetch client secret & publishable key
async function FetchData() {
    const response = await fetch('/checkout/secret');
    const stripeData = await response.json();

    // document.getElementById('client-secret').innerText = client_secret['client_secret']

    return stripeData
}
