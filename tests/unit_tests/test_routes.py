from web.app import create_app
from web.urls import HEALTH_URL, RATES_URL


class TestRoutes:
    app = create_app()

    def test_is_rates_route_working(self):
        with self.app.test_client() as client:
            response = client.get(RATES_URL,
                                  query_string={
                                      'date_from': '2016-01-01',
                                      'date_to': '2016-01-10',
                                      'origin': 'CNSGH',
                                      'destination': 'north_europe_main'
                                  })
            assert response.status_code == 200

    def test_no_rates_record_found(self):
        with self.app.test_client() as client:
            response = client.get(RATES_URL,
                                  query_string={
                                      'date_from': '2016-01-01',
                                      'date_to': '2016-01-10',
                                      'origin': 'ABCD',
                                      'destination': 'EFGH'
                                  })
            assert response.status_code == 200

    def test_is_health_route_working(self):
        with self.app.test_client() as client:
            response = client.get(HEALTH_URL)
            assert response.status_code == 200
