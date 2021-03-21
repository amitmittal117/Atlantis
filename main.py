from flask import Flask, request
from flask_restful import Api, Resource
import requests
import csv
from generate_csv import generate_csv

app = Flask(__name__)
api = Api(app)


class Atlantis(Resource):

    def post(self):
        # print(request.form)
        data = request.form
        csv_reader = data.to_dict(flat=False)['data']

        # with open(csv_reader) as csv_file:
        #     csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        temp = []
        for row in csv_reader:
            temp.append(row)
        init_row = temp[0]
        csvs = []
        sub_csv = []
        for row in temp[1:]:
            line_count += 1
            if line_count == 1:
                sub_csv.append(init_row)
                sub_csv.append(row)
            elif line_count == 100:
                sub_csv.append(row)
                csvs.append(sub_csv)
                line_count = 0
                sub_csv = []
            else:
                sub_csv.append(row)
        print(csvs)
        line_count = 0
        for record in csvs:
            line_count +=1
            fieldnames = ['id', 'first_name', 'last_name', 'email', 'Pincode', 'timestamp']
            writer = csv.DictWriter(open("data"+str(line_count)+".csv", "w"), fieldnames=fieldnames)
            writer.writerow(dict(zip(fieldnames, fieldnames)))
            for i in range(1, len(record)):
                writer.writerow(dict([
                    ('id', record[0]),
                    ('first_name', record[1]),
                    ('last_name', record[2]),
                    ('email', record[3]),
                    ('Pincode', record[4]),
                    ('timestamp', record[5])]))
        return {"data": "Posted"}


api.add_resource(Atlantis, "/atlantis/csv/")

if __name__ == "__main__":
    generate_csv()
    app.run(debug=True)
