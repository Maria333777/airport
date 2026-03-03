import flet as ft
from api_services import get_country_data, get_weather
from models import TravelPlan
from cost_calculator import calculate_total_cost
from storage import save_plan

def main(page: ft.Page):
    page.title = "Gran Malo Travel Agency"
    page.scroll = "auto"

    selected_country = {"data": None}
    current_plan = {"plan": None}

    country_input = ft.TextField(label="Enter country name")
    client_input = ft.TextField(label="Client Name")
    days_input = ft.TextField(label="Days of stay")
    date_input = ft.TextField(label="Start Date (YYYY-MM-DD)")
    notes_input = ft.TextField(label="Notes")

    country_info = ft.Text()
    weather_info = ft.Text()
    cost_info = ft.Text()

    def search_country(e):
        data = get_country_data(country_input.value)

        if not data:
            country_info.value = "Country not found."
            page.update()
            return

        selected_country["data"] = data

        country_info.value = (
            f"Official Name: {data['official_name']}\n"
            f"Capital: {data['capital']}\n"
            f"Region: {data['region']} - {data['subregion']}\n"
            f"Population: {data['population']}\n"
            f"Currencies: {data['currencies']}\n"
            f"Languages: {data['languages']}\n"
            f"Timezones: {data['timezones']}"
        )

        lat, lon = data["latlng"]
        weather = get_weather(lat, lon)

        if weather:
            weather_info.value = (
                f"Temperature: {weather.get('temperature')}°C\n"
                f"Wind Speed: {weather.get('windspeed')} km/h"
            )

        page.update()

    def create_plan(e):
        current_plan["plan"] = TravelPlan(client_input.value)

    def add_country(e):
        if selected_country["data"] and current_plan["plan"]:
            current_plan["plan"].add_country(
                selected_country["data"]["official_name"],
                days_input.value,
                date_input.value,
                notes_input.value
            )

    def calculate_cost(e):
        if current_plan["plan"]:
            total = calculate_total_cost(current_plan["plan"].countries)
            current_plan["plan"].total_cost = total
            cost_info.value = f"Total Estimated Cost: ${total}"
            page.update()

    def save_current_plan(e):
        if current_plan["plan"]:
            save_plan(current_plan["plan"])
            cost_info.value += "\nPlan saved!"
            page.update()

    page.add(
        ft.Text("Gran Malo Travel Agency", size=24),
        country_input,
        ft.ElevatedButton("Search Country", on_click=search_country),
        country_info,
        weather_info,
        ft.Divider(),
        ft.Text("Create Travel Plan", size=20),
        client_input,
        ft.ElevatedButton("Create Plan", on_click=create_plan),
        days_input,
        date_input,
        notes_input,
        ft.ElevatedButton("Add Country", on_click=add_country),
        ft.ElevatedButton("Calculate Cost", on_click=calculate_cost),
        ft.ElevatedButton("Save Plan", on_click=save_current_plan),
        cost_info
    )


ft.app(target=main)