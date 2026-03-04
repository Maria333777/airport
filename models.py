class TravelPlan:

    client_name = ""
    countries = []
    dates = ""
    notes = ""

    def set_client_name(self, name):
        self.client_name = name
        self.countries = [] 

    def add_country(self, country, days, start_date, notes):
        self.countries.append({
            "country": country,
            "days": days,
            "start_date": start_date,
            "notes": notes
        })
    

    def set_dates(self, dates):
        self.dates = dates

    def set_notes(self, notes):
        self.notes = notes

    def to_dict(self):
        return {
            "client_name": self.client_name,
            "countries": self.countries,
            "dates": self.dates,
            "notes": self.notes
        }