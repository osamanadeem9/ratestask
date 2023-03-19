import pytest
from web import utils

from web.app import create_app
from web.urls import RATES_URL


class TestParams:
    app = create_app()

    def test_is_valid_url(self):
        with self.app.test_client() as client:
            response = client.get(RATES_URL,
                                  query_string={
                                      'date_from': '2016-01-01',
                                      'date_to': '2016-01-10',
                                      'origin': 'CNSGH',
                                      'destination': 'north_europe_main'
                                  })
        assert response.status_code == 200

    def test_is_attribute_missing(self):
        with self.app.test_client() as client:
            response = client.get(RATES_URL,
                                  query_string={
                                      'date_from': '2016-01-01',
                                      'date_to': '2016-01-10',
                                      'origin': 'CNSGH',
                                      'destination': ''
                                  })
        assert response.status_code == 401

    def test_is_start_date_smaller(self):
        with self.app.test_client() as client:
            response = client.get(RATES_URL,
                                  query_string={
                                      'date_from': '2016-01-15',
                                      'date_to': '2016-01-10',
                                      'origin': 'CNSGH',
                                      'destination': 'north_europe_main'
                                  })
        assert response.status_code == 401

    def test_is_valid_date_difference(self):
        start_date = '2021-05-10'
        end_date = '2021-05-20'

        assert utils.is_valid_date_difference(start_date, end_date) is True
        assert utils.is_valid_date_difference('2021-04-25', '2021-04-02') is False

    def test_validate_empty_params(self):
        args = {'date_from': '',
                'date_to': '',
                'origin': '',
                'destination': ''}
        assert utils.validate_params(args)['result'] is False

        args['origin'] = 'ABC'
        args['destination'] = 'DEF'
        assert utils.validate_params(args)['result'] is False

    def test_validate_date_format(self):
        args = {'date_from': '20-11-2014',
                'date_to': '25-12-2014',
                'origin': 'ABC',
                'destination': 'DEF'}
        assert utils.validate_params(args)['result'] is False

        args['date_from'] = '2014-11-20'
        args['date_to'] = '2014-12-25'
        assert utils.validate_params(args)['result'] is True

    def test_valid_params(self):
        args = {'date_from': '2016-01-01',
                'date_to': '2016-01-10',
                'origin': 'CNSGH',
                'destination': 'north_europe_main'}
        assert utils.validate_params(args)['result'] is True

        args['origin'] = ''
        assert utils.validate_params(args)['result'] is False

        args['origin'] = None
        assert utils.validate_params(args)['result'] is False
