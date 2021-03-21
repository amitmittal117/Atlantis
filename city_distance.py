from math import sin, cos, sqrt, atan2, radians


class CityDistance:
    def __init__(self, city1_cod, city2_cod):
        self.city1 = city1_cod
        self.city2 = city2_cod
        self.R = 6373.0
        self.lat1 = 0
        self.lon1 = 0
        self.lat2 = 0
        self.lon2 = 0

    def calculate_lat_lon(self, city_lat_lon, number):
        lat_long_array = city_lat_lon.split(',')
        latitude = lat_long_array[0].split(' ')
        longitude = ''
        if lat_long_array[1][0] == ' ':
            longitude = lat_long_array[1].split(' ')[1:]
        else:
            longitude = lat_long_array[1].split(' ')

        lat1 = latitude[0]
        lon1 = longitude[0]
        if latitude[1] is 'S' or latitude[1] is 'W':
            lat1 = float(latitude[0]) - (2 * float(latitude[0]))
        if longitude[1] is 'S' or longitude[1] is 'W':
            lon1 = float(longitude[0]) - (2 * float(longitude[0]))
        if number == 1:
            self.lat1 = radians(float(lat1))
            self.lon1 = radians(float(lon1))
        else:
            self.lat2 = radians(float(lat1))
            self.lon2 = radians(float(lon1))

    def calculate_distance(self):
        dlon = self.lon2 - self.lon1
        dlat = self.lat2 - self.lat1
        a = sin(dlat / 2) ** 2 + cos(self.lat1) * cos(self.lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = self.R * c
        return round(distance, 2)

    def main(self):
        self.calculate_lat_lon(self.city1, 1)
        self.calculate_lat_lon(self.city2, 2)
        distance = self.calculate_distance()
        print('City 1 and City 2 are ' + str(distance) + ' km apart')

if __name__ == '__main__':
    city1 = raw_input("City 1: ")
    city2 = raw_input("City 2: ")
    CityDistanceObj = CityDistance(city1,city2)
    CityDistanceObj.main()
