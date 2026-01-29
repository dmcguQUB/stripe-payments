"use client"

export default function Checkout() {

  async function handleCheckout(){
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/create-checkout-session`,{
      method:"POST"
    });
    const data =await res.json();
    window.location.href=data.url
  }
  return (
    <div>
      <button onClick={handleCheckout}>Checkout</button>
    </div>
  );
}
