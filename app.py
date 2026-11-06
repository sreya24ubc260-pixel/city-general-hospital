from flask import Flask, render_template, request, redirect, url_for

from forms import (
    AppointmentForm,
    ContactForm,
    FeedbackForm
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clinical-trust-secret-key'


# -------------------- Home --------------------

@app.route('/')
def index():
    return render_template('index.html')


# -------------------- Appointment --------------------

@app.route('/book', methods=['GET', 'POST'])
def book():

    form = AppointmentForm()

    if form.validate_on_submit():

        return redirect(url_for(
            'confirmation',
            name=form.patient_name.data,
            email=form.email.data,
            age=form.age.data,
            gender=form.gender.data,
            department=form.department.data,
            date=form.appointment_date.data.strftime("%d-%m-%Y"),
            symptoms=form.symptoms.data
        ))

    return render_template('book.html', form=form)


# -------------------- Contact --------------------

@app.route('/contact', methods=['GET', 'POST'])
def contact():

    form = ContactForm()

    if form.validate_on_submit():

        return redirect(url_for(
            'confirmation',
            name=form.name.data,
            email=form.email.data,
            age="N/A",
            gender="N/A",
            department=form.subject.data,
            date="N/A",
            symptoms=form.message.data
        ))

    return render_template('contact.html', form=form)


# -------------------- Feedback --------------------

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():

    form = FeedbackForm()

    if form.validate_on_submit():

        return redirect(url_for(
            'confirmation',
            name=form.name.data,
            email=form.email.data,
            age="N/A",
            gender="N/A",
            department="Patient Feedback",
            date="N/A",
            symptoms=form.suggestions.data
        ))

    return render_template('feedback.html', form=form)


# -------------------- Confirmation --------------------

@app.route('/confirmation')
def confirmation():

    data = {
        "name": request.args.get("name"),
        "email": request.args.get("email"),
        "age": request.args.get("age"),
        "gender": request.args.get("gender"),
        "department": request.args.get("department"),
        "date": request.args.get("date"),
        "symptoms": request.args.get("symptoms")
    }

    return render_template("confirmation.html", data=data)


# -------------------- Main --------------------

if __name__ == '__main__':
    app.run(debug=True)