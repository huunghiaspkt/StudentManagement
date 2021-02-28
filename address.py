class Address:
    def __init__(self,county, city, street):
        try:
            self.country = county
            self.city = city
            self.street = street
        except BaseException as reason:
            print(f'Wrong address format {reason}')

