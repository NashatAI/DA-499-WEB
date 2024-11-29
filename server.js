const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();
app.use(bodyParser.json());

// الاتصال بقاعدة البيانات
mongoose.connect('mongodb://localhost:27017/studyData', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

const studentSchema = new mongoose.Schema({
  comprehension: String,
  activityTime: [String],
  studyPreference: String,
  focusTime: Number,
  timeManagement: [String],
  subjects: [String],
  grades: {
    cis120: String,
    stat101: String,
    cs111: String,
    da350: String
  },
  currentGpa: Number
});

const Student = mongoose.model('Student', studentSchema);

app.post('/processData', (req, res) => {
  const studentData = new Student(req.body);

  studentData.save((err) => {
    if (err) {
      res.status(500).send(err);
    } else {
      res.status(200).send('Data saved successfully!');
    }
  });
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
