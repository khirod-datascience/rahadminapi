from flask import Flask, jsonify, make_response, request, jsonify
from flask_mongoengine import MongoEngine
from flask_cors import CORS, cross_origin

app= Flask(__name__)
# FLASK_APP=app
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
# cors = CORS(app)

@app.route("/")
def home():
    return "Hello, Flask!"



# database_name = "News_data.hospital_data"
DB_URI = "mongodb+srv://Rah_admin:Rah123@cluster0.psrao.mongodb.net/myFirstDatabase?authSource=admin&replicaSet=atlas-mq7cjd-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
app.config["MONGODB_HOST"]= DB_URI


db= MongoEngine()
db.init_app(app)

class hospitals(db.Document):
    _id=db.ObjectIdField()
    address=db.StringField()
    contact_number=db.StringField()
    department=db.StringField()
    facilities=db.StringField()
    hospital_email=db.StringField()
    hospital_name=db.StringField()
    hospital_type=db.StringField()
    images=db.StringField()
    location=db.StringField()
    logo=db.StringField()
    total_icus=db.StringField()
    total_seats=db.StringField()
    about=db.StringField()

    def to_json(self):
        return{
            "_id": self._id,
            "address": self.address,
            "contact_number": self.contact_number,
            "department": self.department,
            "facilities": self.facilities,
            "hospital_email": self.hospital_email,
            "hospital_name": self.hospital_name,
            "hospital_type": self.hospital_type,
            "images": self.images,
            "location": self.location,
            "logo": self.logo,
            "total_icus": self.total_icus,
            "total_seats": self.total_seats,
            "about": self.about,

        }

@app.route('/api/hospital/<id>', methods =["PUT", "GET"])
@cross_origin()
def api_hospitals(id):
    if request.method == "GET":
        # hospitals=[]
        # hospital_name="APOLLO HOSPITAL"
        h=hospitals.objects(_id=id).first()
        response=jsonify(h)
        response.headers.add("Access-Control-Allow-Origin", "*")
    elif request.method == "PUT":
        body = request.get_json()
        hosp_obj = hospitals.objects(_id=id)
        hosp_obj.update(**body)
        response=jsonify({'saved':'data updated'})
        response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# @app.route('/api/image/<id>', methods=['POST'])
# def add_hospital_image(id):
#     image = request.files['file']
#     # 2
#     print(type(image))
#     print(image.filename)
#     hospital_image = hospital_data(_id=id)
#     # 3
#     hospital_image.images.put(image, filename=image.filename)
#     # 4
#     hospital_image.save()
#     # 5
#     return jsonify(hospital_image), 201








if __name__ == '__main__':
    app.run()