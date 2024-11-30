from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/submit-data', methods=['POST'])
def submit_data():
    # استقبال البيانات من الطلب
    data = request.json  # Assuming the data is sent as JSON

    # تخزين البيانات في ملف (على سبيل المثال)
    with open('submitted_data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return jsonify({"message": "تم تخزين البيانات بنجاح!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
