from vehicle_data import VehicleDataFetcher
from datetime import date, timedelta
import time

if __name__ == "__main__":
    fetcher = VehicleDataFetcher()
    year_to_check = 2020
    start_date = date(year_to_check, 1, 1)
    end_date = date(year_to_check + 1, 1, 1)
    current_date = start_date
    while current_date < end_date:
        first_registration_date = current_date.strftime("%Y-%m-%d")
        fetcher.get_vehicle_data(registration_number="PKS66438", vin_number="VF1RJB00265666724", first_registration_date=first_registration_date)
        current_date += timedelta(days=1)
        time.sleep(3) # 3 seconds between requests. Please don't spam the server.




    response = fetcher.get_vehicle_data(registration_number="PKS66438", vin_number="VF1RJB00265666724", first_registration_date="2020-07-07")
    print(response.text)
    response = fetcher.get_vehicle_data(registration_number="PKS66438", vin_number="VF1RJB00265666724", first_registration_date="2020-07-08")
    print(response.text)
    response = fetcher.get_vehicle_data(registration_number="PKS66438", vin_number="VF1RJB00265666724", first_registration_date="2020-07-09")
    print(response.text)
