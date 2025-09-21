import threading, time
try:
    import webview
except Exception:
    webview = None
from app import app as flask_app

def run_flask():
    # Run Flask on a thread; set debug False for desktop run
    flask_app.run(debug=False, port=5000)

if __name__ == '__main__':
    t = threading.Thread(target=run_flask, daemon=True)
    t.start()
    time.sleep(1)  # give server a second
    if webview:
        webview.create_window('MadLibs by Tanzeel', 'http://127.0.0.1:5000')
        webview.start()
    else:
        print('pywebview not installed. Open http://127.0.0.1:5000 in your browser.')
