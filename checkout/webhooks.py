import json
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWebhookHandler


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listen for Stripe webhooks, taken from Stripe docs.
    Inspired by Boutiqu Ado Walkthrough project.
    """
    # Get stripe keys
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # get payload data
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(content=e, status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Set up webhook handler
    handler = StripeWebhookHandler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_failed,
    }

    # Get the webhook type from Stripe
    event_type = event['type']

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response
