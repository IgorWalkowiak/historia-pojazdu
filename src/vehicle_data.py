import requests
import time

MAIN_URL = "https://moj.gov.pl/nforms/engine/ng/index?xFormsAppName=HistoriaPojazdu"
DATA_URL = "https://moj.gov.pl/nforms/api/HistoriaPojazdu/1.0.18/data/vehicle-data"

def build_session_value():
    app_name = "HistoriaPojazdu"
    timestamp = int(time.time() * 1000)  
    session_value = f"{app_name}:{timestamp}"
    return session_value


class VehicleDataFetcher:
    def __init__(self):
        self.session = requests.Session()
        self.nf_wid_value = build_session_value()
        
        form_data = {
            "NF_WID": self.nf_wid_value,
            "varKey": "NF_WID",
            "varApplicationName": "HistoriaPojazdu"
        }
        
        self.session.post(MAIN_URL, data=form_data)
        self.xsrf_token = self.session.cookies.get('XSRF-TOKEN')


    def get_vehicle_data(self, registration_number, vin_number, first_registration_date):
        
        payload = {
            "registrationNumber": registration_number,
            "VINNumber": vin_number, 
            "firstRegistrationDate": first_registration_date
        }
        
        data_headers = {
            "NF_WID": self.nf_wid_value
        }
        
        data_headers["X-XSRF-TOKEN"] = self.xsrf_token
        response = self.session.post(DATA_URL, json=payload, headers=data_headers)
        return response
