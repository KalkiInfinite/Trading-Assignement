import streamlit as st
import pandas as pd
from datetime import datetime
from bot import BasicBot 

st.set_page_config(
    page_title="Binance Futures Trading Bot",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(90deg, #f39c12, #e74c3c);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .error-box {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

if 'order_history' not in st.session_state:
    st.session_state.order_history = []

st.markdown('<h1 class="main-header">🚀 Binance Futures Trading Bot</h1>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.header("Place Order")
    
    with st.form("order_form"):
        col_symbol, col_quantity = st.columns(2)
        
        with col_symbol:
            symbol = st.text_input("Trading Pair (e.g., BTCUSDT)", "BTCUSDT").upper()
        
        with col_quantity:
            quantity = st.number_input("Quantity", min_value=0.0001, format="%.4f")
        
        col_type, col_side = st.columns(2)
        
        with col_type:
            order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
        
        with col_side:
            side = st.radio("Side", ["BUY", "SELL"], horizontal=True)
        
        price = None
        if order_type == "LIMIT":
            price = st.number_input("Price (for LIMIT orders)", min_value=0.01, format="%.2f")
        
        submitted = st.form_submit_button("Place Order", type="primary", use_container_width=True)

    if submitted:
        with st.spinner("Placing order..."):
            try:
                bot = BasicBot()
                result = bot.place_order(
                    symbol=symbol, 
                    side=side, 
                    order_type=order_type, 
                    quantity=quantity, 
                    price=price
                )

                if "error" in result:
                    st.markdown(f"""
                    <div class="error-box">
                        <strong>Order Failed</strong><br>
                        {result['error']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="success-box">
                        <strong>{side} order placed successfully!</strong>
                    </div>
                    """, unsafe_allow_html=True)

                    st.session_state.order_history.append({
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'symbol': symbol,
                        'side': side,
                        'type': order_type,
                        'quantity': quantity,
                        'price': price,
                        'status': 'SUCCESS'
                    })
                    
                    with st.expander("Order Response"):
                        st.json(result)
                        
            except Exception as e:
                st.error(f"Error: {str(e)}")

with col2:
    st.header("Quick Stats")
    st.metric("Current Symbol", symbol if 'symbol' in locals() else "BTCUSDT")
    st.metric("Orders Today", len(st.session_state.order_history))

st.header("Order History")
if st.session_state.order_history:
    df = pd.DataFrame(st.session_state.order_history)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    if st.button("Clear History"):
        st.session_state.order_history = []
        st.rerun()
else:
    st.info("No orders placed yet.")