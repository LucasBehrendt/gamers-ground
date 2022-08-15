// Get keys from template
const stripe_public_key = document.getElementById('id_stripe_public_key').innerText.slice(1, -1);
const client_secret = document.getElementById('id_client_secret').innerText.slice(1, -1);

// set up stripe elements & mount to template
const stripe = Stripe(stripe_public_key);
const elements = stripe.elements();
const style = {
    base: {
      color: '#212529',
      fontSize: '1.3rem',
      '::placeholder': {
            color: 'grey'
        }
    }
  };
const card = elements.create('card', {style: style});
card.mount('#card-element');