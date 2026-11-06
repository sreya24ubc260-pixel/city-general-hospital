from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import (
    StringField, EmailField, PasswordField, IntegerField,
    RadioField, SelectField, SelectMultipleField,
    BooleanField, TextAreaField, DateField, SubmitField
)

from wtforms.validators import (
    DataRequired, Length, Email,
    EqualTo, NumberRange, Optional
)


# -------------------- Appointment Form --------------------

class AppointmentForm(FlaskForm):
    patient_name = StringField(
        'Patient Full Name',
        validators=[DataRequired(), Length(min=3, max=30)]
    )

    email = EmailField(
        'Email Address',
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        'Create Password',
        validators=[DataRequired(), Length(min=8)]
    )

    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password', message="Passwords must match")
        ]
    )

    age = IntegerField(
        'Age',
        validators=[DataRequired(), NumberRange(min=1, max=120)]
    )

    gender = RadioField(
        'Gender',
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        ],
        validators=[DataRequired()]
    )

    department = SelectField(
        'Department',
        choices=[
            ('', 'Choose Department'),
            ('Cardiology', 'Cardiology'),
            ('Neurology', 'Neurology'),
            ('Orthopedics', 'Orthopedics'),
            ('Pediatrics', 'Pediatrics')
        ],
        validators=[DataRequired()]
    )

    symptoms = TextAreaField(
        'Symptoms',
        validators=[Optional()]
    )

    appointment_date = DateField(
        'Appointment Date',
        validators=[DataRequired()]
    )

    medical_reports = FileField(
        'Medical Report',
        validators=[Optional()]
    )

    agree_terms = BooleanField(
        'I agree to the Terms & Conditions',
        validators=[DataRequired()]
    )

    submit = SubmitField('Book Appointment')


# -------------------- Contact Form --------------------

class ContactForm(FlaskForm):

    name = StringField(
        'Full Name',
        validators=[DataRequired(), Length(min=3, max=30)]
    )

    email = EmailField(
        'Email Address',
        validators=[DataRequired(), Email()]
    )

    subject = SelectField(
        'Subject',
        choices=[
            ('General Inquiry', 'General Inquiry'),
            ('Billing', 'Billing'),
            ('Emergency', 'Emergency')
        ],
        validators=[DataRequired()]
    )

    message = TextAreaField(
        'Message',
        validators=[
            DataRequired(),
            Length(min=10, max=300)
        ]
    )

    submit = SubmitField('Send Message')


# -------------------- Feedback Form --------------------

class FeedbackForm(FlaskForm):

    name = StringField(
        'Full Name',
        validators=[DataRequired()]
    )

    email = EmailField(
        'Email Address',
        validators=[DataRequired(), Email()]
    )

    services_used = SelectMultipleField(
        'Services Used',
        choices=[
            ('OPD', 'OPD'),
            ('Pharmacy', 'Pharmacy'),
            ('Diagnostics', 'Diagnostics')
        ],
        validators=[DataRequired()]
    )

    rating = RadioField(
        'Overall Rating',
        choices=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')
        ],
        validators=[DataRequired()]
    )

    recommend = BooleanField(
        'Would you recommend our hospital?',
        validators=[Optional()]
    )

    suggestions = TextAreaField(
        'Suggestions',
        validators=[Optional()]
    )

    submit = SubmitField('Submit Feedback')