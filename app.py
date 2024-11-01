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
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
            <title>QR Code Generator</title>
        </head>
        <body>
            <div class="container">
                <h1 class="mt-5">Generate QR Code</h1>
                <form method="post" enctype="multipart/form-data" class="mt-3">
                    <div class="form-group">
                        <label for="data">Enter link or text</label>
                        <input type="text" class="form-control" id="data" name="data" placeholder="Enter link or text" required>
                    </div>
                    <button type="submit" class="btn btn-primary">Generate</button>
                </form>
            </div>
            <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
        </body>
        </html>
    ''')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

