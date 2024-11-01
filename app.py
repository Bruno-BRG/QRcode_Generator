from flask import Flask, request, send_file, render_template_string
import qrcode
import os

app = Flask(__name__)

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['data']
        filename = 'qrcode.png'
        generate_qr_code(data, filename)
        return send_file(filename, as_attachment=True)
    return render_template_string('''
        <!doctype html>
        <title>QR Code Generator</title>
        <h1>Generate QR Code</h1>
        <form method=post enctype=multipart/form-data>
          <input type=text name=data placeholder="Enter link or text">
          <input type=submit value=Generate>
        </form>
    ''')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

