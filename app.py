# from flask import Flask, render_template, request
# from keras.models import load_model
# from keras.utils import load_img,img_to_array
# import numpy as np
# from os import path
# import os

# app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
# model = load_model('D:/food_project/foodimages/project/food_model.h5')

# labels = {'adhirasam': 0,
#  'aloo_gobi': 1,
#  'aloo_matar': 2,
#  'aloo_methi': 3,
#  'aloo_shimla_mirch': 4,
#  'aloo_tikki': 5,
#  'anarsa': 6,
#  'ariselu': 7,
#  'bandar_laddu': 8,
#  'basundi': 9,
#  'bhatura': 10,
#  'bhindi_masala': 11,
#  'biryani': 12,
#  'boondi': 13,
#  'butter_chicken': 14,
#  'chak_hao_kheer': 15,
#  'cham_cham': 16,
#  'chana_masala': 17,
#  'chapati': 18,
#  'chhena_kheeri': 19,
#  'chicken_razala': 20,
#  'chicken_tikka': 21,
#  'chicken_tikka_masala': 22,
#  'chikki': 23,
#  'daal_baati_churma': 24,
#  'daal_puri': 25,
#  'dal_makhani': 26,
#  'dal_tadka': 27,
#  'dharwad_pedha': 28,
#  'doodhpak': 29,
#  'double_ka_meetha': 30,
#  'dum_aloo': 31,
#  'gajar_ka_halwa': 32,'gavvalu': 33,
#  'ghevar': 34,
#  'gulab_jamun': 35,
#  'imarti': 36,
#  'jalebi': 37,
#  'kachori': 38,
#  'kadai_paneer': 39,
#  'kadhi_pakoda': 40,
#  'kajjikaya': 41,
#  'kakinada_khaja': 42}



# def processed_img(img_path):
#     img=load_img(img_path,target_size=(128,128,3))
#     img=img_to_array(img)
#     img=img/255
#     img=np.expand_dims(img,[0])
#     answer=model.predict(img)
#     y_class = answer.argmax(axis=-1)
#     print("y_class",y_class)
#     y = " ".join(str(x) for x in y_class)
#     y = int(y)
#     print("yyyyyyyyyy",y)
#     key = list(labels.keys())
#     val = list(labels.values())
#     position = val.index(y)
#     return key[position]

           
    
# # processed_img("D:/food_project/foodimages/food_images  ariselu8.jpg")
# # # routes
# @app.route("/", methods=['GET', 'POST'])
# def main():
# 	return render_template("index.html")

# @app.route("/about")
# def about_page():
# 	return "Please subscribe  Artificial Intelligence Hub..!!!"
# img_path = "D:/food_project/foodimages/project/static/uploads/"
# app.config["upload"]=img_path
# @app.route("/submit", methods = ['GET', 'POST'])
# def get_output():
# 	if request.method == 'POST':
# 		image = request.files['img']
# 		filename = image.filename
# 		# img_path = "D:/food_project/foodimages/project/static/uploads/" + img.filename	
# 		image.save(os.path.join(app.config['upload'], filename))
# 		img = os.path.join(app.config['upload'], filename)
# 		# img_path =os.path.basename('f D:/food_project/foodimages/project/static/uploads/{}')
# 		# img.save(img_path)
# 		# print("img_path",img_path)
# 		p = processed_img(img)
# 		print("*************************************************",p)

# 	return render_template("index.html", prediction = p, img_path =img)


# if __name__ =='__main__':
# 	#app.debug = True
# 	app.run(debug = True)


from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename
import os
from flask import Flask, render_template, request
from keras.models import load_model
from keras.utils import load_img,img_to_array
import numpy as np
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Food_Project"
mongo = PyMongo(app)
model = load_model('D:/food_project/foodimages/project/food_model.h5')
labels = {'adhirasam': 0,
 'aloo_gobi': 1,
 'aloo_matar': 2,
 'aloo_methi': 3,
 'aloo_shimla_mirch': 4,
 'aloo_tikki': 5,
 'anarsa': 6,
 'ariselu': 7,
 'bandar_laddu': 8,
 'basundi': 9,
 'bhatura': 10,
 'bhindi_masala': 11,
 'biryani': 12,
 'boondi': 13,
 'butter_chicken': 14,
 'chak_hao_kheer': 15,
 'cham_cham': 16,
 'chana_masala': 17,
 'chapati': 18,
 'chhena_kheeri': 19,
 'chicken_razala': 20,
 'chicken_tikka': 21,
 'chicken_tikka_masala': 22,
 'chikki': 23,
 'daal_baati_churma': 24,
 'daal_puri': 25,
 'dal_makhani': 26,
 'dal_tadka': 27,
 'dharwad_pedha': 28,
 'doodhpak': 29,
 'double_ka_meetha': 30,
 'dum_aloo': 31,
 'gajar_ka_halwa': 32,'gavvalu': 33,
 'ghevar': 34,
 'gulab_jamun': 35,
 'imarti': 36,
 'jalebi': 37,
 'kachori': 38,
 'kadai_paneer': 39,
 'kadhi_pakoda': 40,
 'kajjikaya': 41,
 'kakinada_khaja': 42}

def processed_img(img_path):
    img=load_img(img_path,target_size=(128,128,3))
    img=img_to_array(img)
    img=img/255
    img=np.expand_dims(img,[0])
    answer=model.predict(img)
    y_class = answer.argmax(axis=-1)
    print("y_class",y_class)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    print("yyyyyyyyyy",y)
    key = list(labels.keys())
    val = list(labels.values())
    position = val.index(y)
    return key[position]

# def get_recipe_by_name(name):
#     collection = mongo.db.Recipe  
#     recipe = collection.find_one({'name':str(name)})
#     if recipe:
#         recipe['_id'] = str(recipe['_id'])
#         # print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh",recipe)
#         return jsonify(recipe)
#     else:
#         return jsonify({'message': 'Recipe not found'})
     
upload_folder = os.path.join('static', 'uploads')
 
app.config['UPLOAD'] = upload_folder
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")
@app.route("/submit", methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        res = processed_img(img)
        print("*************************************************",res)
        collection = mongo.db.Recipe  
        recipe = collection.find_one({'name':str(res)})
        if recipe:
            recipe['_id'] = str(recipe['_id'])
        # print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh",recipe)
            
        print("*******************************************",recipe)
    # Return data as a JSON response
        return render_template('index.html',img=img,prediction = res,recipe=recipe)
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run(debug=True)