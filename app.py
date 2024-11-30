<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مشروع تطوير الأداء الدراسي</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            direction: rtl;
            background-color: #f9f9f9;
            color: #333;
        }
        header {
            background: linear-gradient(90deg, #4CAF50, #36A2EB);
            color: white;
            padding: 20px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        h1 {
            margin: 0;
            font-size: 2em;
        }
        section {
            padding: 20px;
            background-color: white;
            margin: 20px auto;
            width: 90%;
            max-width: 800px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        footer {
            background-color: #333;
            color: white;
            padding: 5px 0;
            position: fixed;
            bottom: 0;
            width: 100%;
            font-size: 0.8em;
        }
        .button {
            background-color: #36A2EB;
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px 2px;
            cursor: pointer;
            border-radius: 12px;
            transition: background-color 0.3s;
        }
        .button:hover {
            background-color: #4CAF50;
        }
        .question {
            margin: 20px 0;
            text-align: right;
            font-weight: bold;
        }
        form {
            display: block;
            text-align: right;
            margin: 20px auto;
            width: 90%;
            max-width: 800px;
        }
        input[type="checkbox"], input[type="radio"], input[type="number"], input[type="text"], select {
            margin-right: 5px;
            vertical-align: middle;
        }
        input[type="number"], input[type="text"], select {
            width: calc(100% - 10px);
            padding: 8px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            transition: border-color 0.3s;
        }
        input[type="number"]:focus, input[type="text"]:focus, select:focus {
            border-color: #36A2EB;
        }
        .option-group {
            margin: 10px 0;
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
</head>
<body>
    <header>
        <h1>مشروع تطوير الأداء الدراسي</h1>
    </header>
    <section>
        <form action="#" method="post">
            <div class="option-group">
                <label class="question" for="comprehension">1. كيف درست مواد الفهم؟</label><br>
                <input type="radio" id="video" name="comprehension" value="مشاهدة فيديو">
                <label for="video">مشاهدة فيديو</label><br>
                <input type="radio" id="reading" name="comprehension" value="القراءة">
                <label for="reading">القراءة</label><br>
                <input type="radio" id="writing" name="comprehension" value="الكتابة">
                <label for="writing">الكتابة</label><br>
                <input type="radio" id="writing-reading" name="comprehension" value="الكتابة والقراءة">
                <label for="writing-reading">الكتابة والقراءة</label><br><br>
            </div>
            
            <div class="option-group">
                <label class="question" for="activity-time">2. متى تكون أكثر نشاطًا؟</label><br>
                <input type="checkbox" id="morning1" name="activity-time-morning" value="8:00 AM - 12:00 PM">
                <label for="morning1">8:00 AM - 12:00 PM</label><br>
                <input type="checkbox" id="afternoon" name="activity-time-afternoon" value="12:00 PM - 4:00 PM">
                <label for="afternoon">12:00 PM - 4:00 PM</label><br>
                <input type="checkbox" id="evening" name="activity-time-evening" value="6:00 PM - 10:00 PM">
                <label for="evening">6:00 PM - 10:00 PM</label><br>
                <input type="checkbox" id="night" name="activity-time-night" value="10:00 PM - 12:00 AM">
                <label for="night">10:00 PM - 12:00 AM</label><br><br>
            </div>
            
            <div class="option-group">
                <label class="question" for="study-preference">3. كيف تفضل أن تدرس؟</label><br>
                <input type="radio" id="alone" name="study-preference" value="منفردًا">
                <label for="alone">منفردًا</label><br>
                <input type="radio" id="group" name="study-preference" value="في مجموعة">
                <label for="group">في مجموعة</label><br><br>
            </div>
            
            <div class="option-group">
                <label class="question" for="focus-time">4. كم دقيقة تستطيع البقاء محافظًا على تركيزك أثناء الدراسة؟</label><br>
                <input type="number" id="focus-time" name="focus-time" min="1" max="300" required><br><br>
            </div>
            
            <div class="option-group">
                <label class="question" for="time-management">5. ما هي الأدوات التي تستخدمها لإدارة وقتك؟</label><br>
                <input type="checkbox" id="digital-calendars" name="time-management" value="تقاويم رقمية">
                <label for="digital-calendars">تقاويم رقمية</label><br>
                <input type="checkbox" id="task-apps" name="time-management" value="تطبيقات إدارة المهام">
                <label for="task-apps">تطبيقات إدارة المهام</label><br>
                <input type="checkbox" id="paper-schedules" name="time-management" value="جداول زمنية ورقية">
                <label for="paper-schedules">جداول زمنية ورقية</label><br>
                <input type="checkbox" id="no-tools" name="time-management" value="لا أستخدم أي أدوات">
                <label for="no-tools">لا أستخدم أي أدوات</label><br><br>
            </div>
            
            <div class="option-group">
                <label class="question" for="subjects">6. المواد التي درستها</label><br>
                <input type="checkbox" id="cis120" name="subjects[]" value="نظم معلومات حاسوبية (CIS 120)">
                <label for="cis120">نظم معلومات حاسوبية (CIS 120)</label><br>
                <input type="checkbox" id="stat101" name="subjects[]" value="احصاء (STAT 101)">
                <label for="stat101">احصاء (STAT 101)</label><br>
                <input type="checkbox" id="cs111" name="subjects[]" value="برمجه بلغة مختارة (CS 111)">
                <label for="cs111">برمجه بلغة مختارة (CS 111)</label><br>
                <input type="checkbox" id="da350" name="subjects[]" value="تعلم آلي (DA 350)">
                <label for="da350">تعلم آلي (DA 350)</label><br>
                <input type="checkbox" id="math101" name="subjects[]" value="تفاضل وتكامل (MATH 101)">
                <label for="math101">تفاضل وتكامل (MATH 101)</label><br><br>
            </div>
            
            <div class="option-group" id="grades-section">
                <label class="question" for="grade1">7. ما هي العلامة التي حصلت عليها في مساق نظم معلومات حاسوبية (CIS 120)</label><br>
                <select id="grade1" name="grade1" required>
                    <option value="" disabled selected>اختر</option>
                    <option value="80-89">80-89</option>
                    <option value="70-79">70-79</option>
                    <option value="60-69">60-69</option>
                    <option value="50-59">50-59</option>
                </select><br>

                <label class="question" for="grade2">8. ما هي العلامة التي حصلت عليها في مساق احصاء (STAT 101)</label><br>
                <select id="grade2" name="grade2" required>
                    <option value="" disabled selected>اختر</option>
                    <option value="90-100">90-100</option>
                    <option value="80-89">80-89</option>
                    <option value="70-79">70-79</option>
                    <option value="60-69">60-69</option>
                    <option value="50-59">50-59</option>
                </select><br>

                <label class="question" for="grade3">9. ما هي العلامة التي حصلت عليها في مساق برمجه بلغة مختارة (CS 111)</label><br>
                <select id="grade3" name="grade3" required>
                    <option value="" disabled selected>اختر</option>
                    <option value="90-100">90-100</option>
                    <option value="80-89">80-89</option>
                    <option value="70-79">70-79</option>
                    <option value="60-69">60-69</option>
                    <option value="50-59">50-59</option>
                </select><br>

                <label class="question" for="grade4">10. ما هي العلامة التي حصلت عليها في مساق تعلم آلي (DA 350)</label><br>
                <select id="grade4" name="grade4" required>
                    <option value="" disabled selected>اختر</option>
                    <option value="90-100">90-100</option>
                    <option value="80-89">80-89</option>
                    <option value="70-79">70-79</option>
                    <option value="60-69">60-69</option>
                    <option value="50-59">50-59</option>
                </select><br>

                <label class="question" for="grade5">11. ما هي العلامة التي حصلت عليها في مساق تفاضل وتكامل (MATH 101)</label><br>
                <select id="grade5" name="grade5" required>
                    <option value="" disabled selected>اختر</option>
                    <option value="90-100">90-100</option>
                    <option value="80-89">80-89</option>
                    <option value="70-79">70-79</option>
                    <option value="60-69">60-69</option>
                    <option value="50-59">50-59</option>
                </select><br>
            </div>

            <div class="option-group">
                <label class="question" for="gpa">12. ما هو معدلك التراكمي؟</label><br>
                <input type="number" id="gpa" name="gpa" min="0" max="100" step="0.1" required><br><br>
            </div>

            <button type="submit" class="button">إرسال</button>
        </form>
    </section>
    <footer>
        <p>&copy; 2024 مشروع تطوير الأداء الدراسي</p>
    </footer>
</body>
</html>
