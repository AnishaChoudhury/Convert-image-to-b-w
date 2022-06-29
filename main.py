from flask import Flask,request,render_template,redirect
import os
app = Flask(__name__, template_folder='template')
from PIL import Image, ImageOps
import io
import base64


app.config["IMAGE_UPLOADS"] = "C:/Users/91932/Downloads/Flask_assign/test_app/test_app/static"


@app.route('/convert',methods = ["GET","POST"])
def upload_convert_image():
	if request.method == "POST":
		image = request.files['file']

		if image.filename == '':
			print("Image must have a file name")
			return redirect(request.url)


		file_name = image.filename

		basedir = os.path.abspath(os.path.dirname(__file__))

		image.save(os.path.join(basedir,"static", file_name))
		

		img = Image.open(app.config["IMAGE_UPLOADS"] + "/" + file_name)
		gray_image = img.convert('1')
		data = io.BytesIO()
		gray_image.save(data, "JPEG")
		encode_img_data = base64.b64encode(data.getvalue())

		return render_template("main.html",filename = encode_img_data.decode("UTF-8"))



	return render_template('main.html')

app.run(debug=True,port=2000)