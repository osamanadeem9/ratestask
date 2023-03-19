import pytest
from web.app import create_app
from web.urls import RATES_URL


class TestRoutes:
    app = create_app()

    def test_xeneta_example_region(self):
        with self.app.test_client() as client:
            response = client.get(RATES_URL,
                                  query_string={
                                      'date_from': '2016-01-01',
                                      'date_to': '2016-01-03',
                                      'origin': 'CNSGH',
                                      'destination': 'north_europe_main'
                                  })
            assert response.status_code == 200
            assert response.json == [{'average': '1112', 'day': '2016-01-01'},
                                     {'average': '1112', 'day': '2016-01-02'},
                                     {'average': None, 'day': '2016-01-03'}]

    def test_get_rate_from_region_codes(self):
        with self.app.test_client() as client:
            response = client.get(RATES_URL,
                                  query_string={
                                      'date_from': '2016-01-01',
                                      'date_to': '2016-01-01',
                                      'origin': 'CNGGZ',
                                      'destination': 'EETLL'
                                  })
            assert response.status_code == 200
            assert response.json == [{'average': '1155', 'day': '2016-01-01'}]

    def test_get_rate_from_region_names(self):
        with self.app.test_client() as client:
            response = client.get(RATES_URL,
                                  query_string={
                                      'date_from': '2016-01-01',
                                      'date_to': '2016-01-01',
                                      'origin': 'china_north_main',
                                      'destination': 'kattegat'
                                  })
            assert response.status_code == 200
            assert response.json == [{'average': '1274', 'day': '2016-01-01'}]

    def test_get_rates_with_no_routes(self):
        with self.app.test_client() as client:
            response = client.get(RATES_URL,
                                  query_string={
                                      'date_from': '2016-01-01',
                                      'date_to': '2016-01-01',
                                      'origin': 'russia_north_west',
                                      'destination': 'north_europe_main'
                                  })
            assert response.status_code == 200
            assert response.json == [{'average': None, 'day': '2016-01-01'}]
