from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

# User model with roles
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # Admin, Teacher, Parent, Finance
    child_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=True)  # Only for Parent role

# Student model with automatic admission number generation
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admission_number = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    class_name = db.Column(db.String(50), nullable=False)  # Add this line for class input
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'))  # Link to Parent model
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    parent = db.relationship('Parent', back_populates='students')  # Update to allow for multiple students

    fees = db.relationship('Fee', back_populates='student')

    # Generate admission numbers incrementally
    @staticmethod
    def generate_admission_number():
        last_student = Student.query.order_by(Student.id.desc()).first()
        new_admission_number = f"{int(last_student.admission_number) + 1:03}" if last_student else "001"
        return new_admission_number

# Parent model
class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationship to view child's assignments, attendance, and fees
    students = db.relationship('Student', back_populates='parent', lazy=True)  # Allow multiple students

# Teacher model
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)

    # Relationship with assignments, attendance, and remarks
    assignments = db.relationship('Assignment', backref='teacher', lazy=True)
    remarks = db.relationship('Remark', backref='teacher', lazy=True)

# Finance model to manage fees and payments
class Finance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Fee structure for each student
# Fee structure for each student
class Fee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    amount_due = db.Column(db.Float, nullable=False)
    amount_paid = db.Column(db.Float, default=0.0)
    due_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default="Pending")  # Status options: Pending, Paid, Overdue

    # Define the relationship to the Student model
    student = db.relationship('Student', back_populates='fees')


# Attendance model
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)
    status = db.Column(db.String(10))  # Present, Absent

# Remark model for teachers to provide feedback for students
class Remark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Assignment model for teachers to post assignments for students
class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=True)  # For individual or all students

    # Relationships
    student = db.relationship('Student', backref='assignments', lazy=True)

# Mark model to store student marks
class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)  # Subject for the marks
    score = db.Column(db.Float, nullable=False)  # The marks scored by the student
    test_type = db.Column(db.String(20), nullable=False)  # Assignment, CAT, or End Term
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    student = db.relationship('Student', backref='marks')
    teacher = db.relationship('Teacher', backref='marks')

class PasswordResetRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Assuming you have a User model
    reason = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='password_reset_requests')

    def __init__(self, user_id, reason):
        self.user_id = user_id
        self.reason = reason
