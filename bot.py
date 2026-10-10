import yfinance as yf, requests, time
from datetime import datetime
my_bot = "8605284482:AAEok5mLGggy7QnnZ0Wb1rf73-GI4qMcTbs"
my_chat = "8090932723"
def send_gamma():
    try:
        spy_price = float(yf.Ticker("SPY").history(period="1d")['Close'].iloc[-1])
        price = spy_price * 10
        tk = yf.Ticker("SPY")
        exp = tk.options[0]
        chain = tk.option_chain(exp)
        cw = int(chain.calls.loc[chain.calls['openInterest'].idxmax(), 'strike']*10)
        pw = int(chain.puts.loc[chain.puts['openInterest'].idxmax(), 'strike']*10)
        zg = int((cw+pw)/2)
        msg = f"🔥 SPX GAMMA {datetime.now().strftime('%H:%M')} Price {price:.1f} Call {cw} Put {pw} Zero {zg}"
        requests.post(f"https://api.telegram.org/bot{my_bot}/sendMessage", data={"chat_id": my_chat, "text": msg})
        print(msg)
    except Exception as e:
        print(e)

send_gamma()
while True:
    time.sleep(900)
    send_gamma()
