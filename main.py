from spin_sdk import http
from spin_sdk.http import Request, Response

class IncomingHandler(http.IncomingHandler):
    def handle_request(self, request: Request) -> Response:
        # Giả sử đây là nơi bạn thực hiện logic Prime Finder
        # Bạn có thể gọi hàm xử lý của bạn tại đây
        
        return Response(
            200,
            {"content-type": "text/plain"},
            bytes("Kết quả tìm số nguyên tố từ Spin Cloud!", "utf-8")
        )
