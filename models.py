class TravelPlan:

    def __init__(self, client_name):
        self.client_name = client_name
        self.countries = []
        self.durations = []
        self.dates = ""
        self.notes = ""

    def add_country(self, country, days):
        self.countries.append(country)
        self.durations.append(days)

    def to_dict(self):
        return {
            "client_name": self.client_name,
            "countries": self.countries,
            "durations": self.durations,
            "dates": self.dates,
            "notes": self.notes
        }