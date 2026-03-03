DAILY_COST = 120
TRANSPORT_COST = 300
AGENCY_FEE = 150

def calculate_total_cost(countries):
    total_days = 0

    for country in countries:
        total_days += country["days"]
    
    total = total_days * DAILY_COST
    
    if len(countries) > 1:
        moves = len(countries) - 1
        total += moves * TRANSPORT_COST

    total += AGENCY_FEE

    return total
