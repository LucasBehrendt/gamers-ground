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

    
});


async function FetchData() {
    const response = await fetch('/checkout/secret');
    const stripeData = await response.json();

    // document.getElementById('client-secret').innerText = client_secret['client_secret']

    return stripeData
}
