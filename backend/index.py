import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import stripe
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

STRIPE_API_KEY=os.getenv("STRIPE_API_KEY")
FRONTEND_URL=os.getenv("FRONTEND_URL")
if not STRIPE_API_KEY:
  raise RuntimeError("Api key not loaded")

stripe.api_key = STRIPE_API_KEY

app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=FRONTEND_URL,
  allow_methods=["*"]
)

@app.post('/create-checkout-session')
def create_checkout_session():
  session = stripe.checkout.Session.create(
    line_items=[{
      'price_data':{
        'currency':'usd',
        'product_data':{
          'name':'T-shirt'
        },
        'unit_amount':'2099'
      },
      'quantity':1
    }],
    mode='payment',
    success_url=FRONTEND_URL+'/success'
  )
  
  return {"url":session.url}

if __name__== '__main__':
    app.run(port=4242)