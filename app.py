from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # استلام البيانات من النموذج
        comprehension = request.form.get('comprehension')
        activity_time = request.form.getlist('activity-time')
        study_preference = request.form.get('study-preference')
        focus_time = request.form.get('focus-time')
        time_management = request.form.getlist('time-management')
        subjects = request.form.getlist('subjects')
        grades = {
            'cis120': request.form.get('grade1'),
            'stat101': request.form.get('grade2'),
            'cs111': request.form.get('grade3'),
            'da350': request.form.get('grade4'),
            'math101': request.form.get('grade5')
        }

        # هنا يمكنك إدراج الخوارزمية لمقارنة الإجابات
        # مثال: مقارنة البيانات وإرجاع النتيجة
        result = compare_answers(comprehension, activity_time, study_preference, focus_time, time_management, subjects, grades)

        return jsonify(result)

    return render_template('index.html')

def compare_answers(comprehension, activity_time, study_preference, focus_time, time_management, subjects, grades):
    # منطق الخوارزمية لمقارنة الإجابات
    # استبدل هذا بالمنطق الفعلي الخاص بك
    return {
        "message": "تمت مقارنة الإجابات بنجاح",
        "data": {
            "comprehension": comprehension,
            "activity_time": activity_time,
            "study_preference": study_preference,
            "focus_time": focus_time,
            "time_management": time_management,
            "subjects": subjects,
            "grades": grades
        }
    }

if __name__ == '__main__':
    app.run(debug=True)
