from flask import Flask, request
from flask_restful import Api, Resource
import requests
import csv
from CabAvailabilityModel import BasicDetails, LocationOfCar
from rest_framework.response import Response

app = Flask(__name__)
api = Api(app)


class Registration(Resource):

    def post(self, post_request):
        name = post_request.POST.get('name')
        car_number = post_request.POST.get('car_number')
        phone_number = post_request.POST.get('phone_number')
        license_number = post_request.POST.get('license_number')
        email = post_request.POST.get('email')
        basic_details_obj, created = BasicDetails.objects.get_or_create(car_number=car_number,
                                                                        phone_number=phone_number,
                                                                        license_number=license_number,
                                                                        email=email)
        if not created:
            return Response({"status": 400, "data": "Already registered once."})

        basic_details_obj.name = name
        basic_details_obj.save()
        response_body = dict()
        response_body['name'] = name
        response_body['car_number'] = car_number
        response_body['phone_number'] = phone_number
        response_body['license_number'] = license_number
        response_body['email'] = email
        return Response({"status": 200, "data": response_body})

    def put(self, driver_id, lat, lon):
        location_obj, created = LocationOfCar.objects.get_or_create(license_number=driver_id)
        location_obj.lat = lat
        location_obj.lon = lon
        location_obj.save()
        return Response({"status": 200, "data": "Location Saved"})


api.add_resource(Registration, "/CabAvailability/registration/")
api.add_resource(Registration, "/CabAvailability/<string: driver_id>/updateLocation/<string: lat>/<string: lon>")

if __name__ == "__main__":
    app.run(debug=True)
