import socket
import ssl
import threading

server_address = ('localhost', 12345)

# Hàm nhận dữ liệu từ server
def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("\nNhận:", data.decode('utf-8'))
    except:
        pass
    finally:
        ssl_socket.close()
        print("Kết nối đã đóng.")

# ✅ Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ✅ Tạo SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = False

# ✅ Tải chứng chỉ của server để xác thực
context.load_verify_locations(cafile="./certificates/server-cert.crt")

# ✅ Thiết lập SSL cho socket client
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')

# ✅ Kết nối tới server
ssl_socket.connect(server_address)

# ✅ Tạo thread nhận dữ liệu
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()

# ✅ Gửi tin nhắn
try:
    while True:
        message = input("Nhập tin nhắn: ")
        ssl_socket.send(message.encode('utf-8'))
except KeyboardInterrupt:
    print("Thoát.")
finally:
    ssl_socket.close()
