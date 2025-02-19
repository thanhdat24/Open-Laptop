from flask import Flask, request
import os
import wakeonlan

app = Flask(__name__)

# Địa chỉ MAC của máy cần bật
TARGET_MAC = "9C-6B-00-16-31-B5"

@app.route('/wake', methods=['GET'])
def wake_pc():
    try:
        wakeonlan.send_magic_packet(TARGET_MAC)
        return "✅ Đã gửi lệnh bật máy!", 200
    except Exception as e:
        return f"❌ Lỗi: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
