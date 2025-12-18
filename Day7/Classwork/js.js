let student = {
    studentId: 101,
    fullName: "Shri Patil",
    email: "shri@123.com",
    course: "Full Stack Development",
    marks: [85, 90, 78, 92, 88]
};

let studentJSON = JSON.stringify(student);
console.log(studentJSON);

let studentObj = JSON.parse(studentJSON);
console.log(studentObj);

let students = ["Alice", "Bob", "Charlie", "David"];
console.log(students);
students.push("Eve");
students.shift();
console.log(students.length);
console.log(students[students.length - 1]);

let marks = [35, 67, 82, 49, 90, 58];

let passedMarks = marks.filter(mark => mark >= 50);
console.log(passedMarks);

let percentageMarks = marks.map(mark => mark + "%");
console.log(percentageMarks);

let hasHighScorer = marks.some(mark => mark > 85);
console.log(hasHighScorer);
