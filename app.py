from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'jsrcc-VCU-MAH-VEK-1999'

# Global variable for weight_input
weight = None
result = None

@app.route('/')
def index():
    return render_template('input_page.html')

@app.route('/input_page')
def input_page():
    return render_template('input_page.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    global weight
    global result
    user_input = request.form['user_input']
    checkbox1 = request.form.get('checkbox1')
    checkbox2 = request.form.get('checkbox2')

    weight_input = int(user_input)
    
    # Add your if-else logic based on checkbox values
    if checkbox1:
        weight = round(weight_input / 2.205, 6)
        result = f"You entered: {user_input} lb. Converted to {weight} kg."
    else: 
        weight = weight_input
        result = f"You entered: {user_input} kg."
    
    # Store weight and result in session
    session["result"] = result
    session['weight'] = weight
    
    return render_template('slider_page.html', result=result, weight=weight)

@app.route('/process_slider', methods=['POST'])
def process_slider():
    # Process slider data if needed
    return redirect(url_for('canine_sedation_opts'))

@app.route('/slider_page')
def slider_page():
    # Get weight from session
    weight = session.get('weight')
    result = session.get('result')
    return render_template('slider_page.html', weight=weight, result=result)

@app.route('/sedation_route')
def sedation_route():
    weight = session.get('weight')
    result = session.get('result')
    return render_template('sedation_route.html', weight=weight,  result=result)

@app.route('/canine_sedation_opts')
def canine_sedation_opts():
    weight = session.get('weight')
    result = session.get('result')
    print(f"Weight on new_page: {weight}")  # Add this line for debugging
    return render_template('canine_sedation_opts.html', weight=weight,  result=result)

@app.route('/feline_sedation_opts')
def feline_sedation_opts():
    weight = session.get('weight')
    result = session.get('result')
    print(f"Weight on new_page: {weight}")  # Add this line for debugging
    return render_template('feline_sedation_opts.html', weight=weight, result=result)

@app.route('/ER_drugs')
def ER_drugs():
    weight = session.get('weight')
    result = session.get('result')
    print(f"Weight on new_page: {weight}")  # Add this line for debugging
    return render_template('ER_drugs.html', weight=weight, result=result)


if __name__ == '__main__':
    app.run(debug=True)
