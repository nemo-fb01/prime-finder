from flask import Flask, request, render_template_string

app = Flask(__name__)

# Giao diện HTML đơn giản tích hợp trực tiếp
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Prime Finder</title>
    <style>
        body { font-family: sans-serif; text-align: center; margin-top: 50px; }
        input { padding: 10px; width: 200px; }
        button { padding: 10px 20px; cursor: pointer; background: #007bff; color: white; border: none; }
        .result { margin-top: 20px; font-weight: bold; color: #28a745; word-wrap: break-word; padding: 0 20px; }
    </style>
</head>
<body>
    <h1>Tìm số nguyên tố</h1>
    <form method="POST">
        <input type="number" name="number" placeholder="Nhập một số..." required>
        <button type="submit">Tìm ngay</button>
    </form>
    {% if result %}
        <div class="result">
            <p>Các số nguyên tố nhỏ hơn {{ n }}:</p>
            <p>{{ result }}</p>
        </div>
    {% endif %}
</body>
</html>
"""

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    n = None
    if request.method == "POST":
        try:
            n = int(request.form.get("number"))
            primes = [str(x) for x in range(2, n) if is_prime(x)]
            result = ", ".join(primes) if primes else "Không có số nào."
        except:
            result = "Vui lòng nhập số hợp lệ."
    return render_template_string(HTML_TEMPLATE, result=result, n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
