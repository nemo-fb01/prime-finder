import os
import time
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

class PrimeHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        n_val = query.get("n", [None])[0]
        
        result_text = ""
        execution_time = 0

        if n_val:
            try:
                num = int(n_val)
                start_time = time.time() # Bắt đầu đo
                
                primes = [str(x) for x in range(2, num) if is_prime(x)]
                
                end_time = time.time() # Kết thúc đo
                execution_time = (end_time - start_time) * 1000 # Chuyển sang ms
                result_text = f"Tìm thấy {len(primes)} số. Thời gian xử lý: {execution_time:.4f} ms"
            except:
                result_text = "Lỗi: Vui lòng nhập số nguyên!"

        html = f"""
        <!DOCTYPE html>
        <html>
        <head><meta charset="utf-8"><title>Python Prime Finder</title></head>
        <body style="text-align:center; font-family:sans-serif; padding-top:50px;">
            <h1>Python Prime Finder (Wasmer)</h1>
            <form method="GET">
                <input type="number" name="n" placeholder="Nhập N..." required>
                <button type="submit">Tính toán</button>
            </form>
            <p style="color:blue;">{result_text}</p>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

if __name__ == "__main__":
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 8080))
    server = HTTPServer((host, port), PrimeHandler)
    server.serve_forever()
