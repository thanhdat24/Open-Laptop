from flask import Flask, request
import os
import wakeonlan

app = Flask(__name__)

# 🔹 Lấy địa chỉ MAC từ biến môi trường
TARGET_MAC = os.getenv("TARGET_MAC")

@app.route('/wake', methods=['GET'])
def wake_pc():
    try:
        if not TARGET_MAC:
            return "❌ Không tìm thấy TARGET_MAC trong môi trường!", 500
        wakeonlan.send_magic_packet(TARGET_MAC)
        return f"✅ Đã gửi lệnh bật máy đến {TARGET_MAC}!", 200
    except Exception as e:
        return f"❌ Lỗi: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
