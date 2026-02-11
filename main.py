import os
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

class PrimeHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse tham số từ URL (ví dụ: /?n=50)
        query_components = parse_qs(urlparse(self.path).query)
        n_val = query_components.get("n", [None])[0]
        
        result_text = ""
        if n_val:
            try:
                num = int(n_val)
                primes = [str(x) for x in range(2, num) if is_prime(x)]
                result_text = f"Số nguyên tố nhỏ hơn {num}: " + ", ".join(primes)
            except:
                result_text = "Vui lòng nhập số nguyên hợp lệ!"

        # Giao diện HTML
        html = f"""
        <!DOCTYPE html>
        <html>
        <head><title>Prime Finder</title></head>
        <body style="text-align:center; font-family:sans-serif; padding-top:50px;">
            <h1>Máy tìm số nguyên tố</h1>
            <form method="GET">
                <input type="number" name="n" placeholder="Nhập số..." required>
                <button type="submit">Tìm</button>
            </form>
            <div style="margin-top:20px; font-weight:bold; color:blue;">{result_text}</div>
        </body>
        </html>
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

if __name__ == "__main__":
    # Quan trọng: Wasmer Cloud thường yêu cầu host 0.0.0.0
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 8080))

    server = HTTPServer((host, port), PrimeHandler)
    print(f"Server started at http://{host}:{port}")
    server.serve_forever()
