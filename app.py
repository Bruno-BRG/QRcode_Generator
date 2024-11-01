from flask import Flask, request, render_template, url_for
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
    img.save(os.path.join('static', filename))

@app.route('/', methods=['GET', 'POST'])
def index():
    filename = None
    if request.method == 'POST':
        data = request.form['data']
        filename = 'qrcode.png'
        generate_qr_code(data, filename)
    return render_template('index.html', filename=filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

