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

        card.update({'disabled': true});
        document.getElementById('checkout-submit').disabled = true;

        toggleLoadingOverlay(true);

        const response = await stripe.confirmCardPayment(stripeData.client_secret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: 'Jenny Rosen',
                },
            },
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
    }
});

function toggleLoadingOverlay(value) {
    const overlay = document.getElementById('loading-overlay')

    if (value) {
        overlay.style.display = 'block'
    } else {
        overlay.style.display = 'none'
    }
}


async function FetchData() {
    const response = await fetch('/checkout/secret');
    const stripeData = await response.json();

    // document.getElementById('client-secret').innerText = client_secret['client_secret']

    return stripeData
}
