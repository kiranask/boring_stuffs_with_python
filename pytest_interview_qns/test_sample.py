"""
kpi proxy automation suite validate the correctness of the
api response body and status codes. This suite covers functional and regression
testing of kpi proxy apis.
"""

from requests import request
import json
import jsonpath
import warnings
import openpyxl
import pytest
import logging
from configparser import ConfigParser

import logging

warnings.filterwarnings('ignore', message='Unverified HTTPS request')
LOGGER = logging.getLogger(__name__)


@pytest.fixture
def setup():
    """
    Setup function sets up pre-requisites required for the test scripts

    """
    file = open("test_data/post_request_body.json", 'r')
    json_req = json.loads(file.read())
    input_header = open("test_data/header.json")
    headers = json.loads(input_header.read())
    config = ConfigParser()
    config.read('test_data/config.ini')
    headers['X-AUTH-SECRET'] = config['QA']['SECRET']
    return config, headers, json_req


@pytest.mark.run(order=1)
def test01_get_proxy_status(setup):
    """
    Check whether kpi proxy is up or down,
    If this test fails,(if kpi-proxy is down)
    all following test will get skipped
    """
    config, headers, json_req = setup
    LOGGER.info("Checking kpi proxy service..")
    try:
        response = request("GET", url=config['QA']['GET_SERVICE_URL'], headers=headers, verify=False)
    except Exception as error:
        LOGGER.error("HTTPS connection lost :", error)

    assert response.status_code == 200, LOGGER.critical("KPI proxy is down, skipping all other test cases")
    assert response.text == "Service is up", LOGGER.error("KPI Proxy service is down")


@pytest.mark.run(order=2)
@pytest.mark.depends(on=['test01_get_proxy_status'])
def test02_get_kpi_threshold_config(setup):
    """
    This test script validate the GET kpi threshold config.
    """
    config, headers, json_req = setup
    LOGGER.info("Validating the GET kpi threshold config..")
    try:
        response = request("GET", url=config["QA"]["GET_TH_URL"], headers=headers, verify=False)
    except Exception as error:
        LOGGER.error("HTTPS connection lost :", error)
    print("till here 1")

    assert response.status_code == 200, LOGGER.error("kpi threshold config get api is down")
    print("Assert passing..")
    obj2 = verifier.DataV1()
    print("-----mistake------")
    print(obj2)
    obj2.kpi_name_list()

    res = json.loads(response.text)
    start_date = res['config'][0]['startDate']
    assert start_date
    settings = res['config'][0]['settings']
    kpi_names_set = set()
    for name_list in settings:
        kpi_names_set.add(name_list['kpi'])
    kpi_names = list(kpi_names_set)
    assert kpi_names, LOGGER.error("V1 Cluster is down, GET calls are failing..")
    if len(kpi_names) > 0 and len(obj2.kpi_name_list()) > 0:
        assert kpi_names.sort() == obj2.kpi_name_list().sort(), LOGGER.error("'kpi names are not matching"
                                                                             "with database")


# @pytest.mark.skip
@pytest.mark.run(order=3)
@pytest.mark.depends(on=['test02_get_kpi_threshold_config'])
def test03_get_threshold_config_kpi_name(setup):
    """
    This test script validate the get kpi threshold api by name.
    """
    config, headers, json_req = setup
    obj2 = verifier.DataV1()

    for kpi_name in obj2.kpi_name_list():
        try:
            response = request("GET", url=config['QA']['GET_TH_URL'] + kpi_name,
                               headers=headers, verify=False)
        except Exception as error:
            LOGGER.error("HTTPS connection lost: ", error)

        assert response.status_code == 200
        res = json.loads(response.text)
        start_date = res['config'][0]['startDate']
        assert start_date


@pytest.mark.depends(on=['test01_get_proxy_status'])
@pytest.mark.run(order=4)
def test04_case_post_valid_input_rline(setup):
    """
    This test script validates the kpi proxy post api.
    media-kpi-proxy-service/api/v1/data
    This is data driven test cases, post request will be tested with different request body data sets
    """
    config, headers, json_req = setup
    obj1 = library.Utility('test_data/postrequests.xlsx', 'Sheet1')
    rov = obj1.fetch_row_count()
    keyList = obj1.fetch_key_names()
    for i in range(2, rov + 1):
        req = obj1.update_request_with_data(i, json_req, keyList)
        req['logtype'] = "r-lines"
        try:
            response = request("POST", url=config['QA']['POST_URL'], headers=headers, data=json.dumps(req),
                               verify=False)
        except Exception as error:
            LOGGER.error("HTTPS connection lost: ", error)

        assert response.status_code == 200, LOGGER.error("kpi proxy post api is failing")
        json_response = json.loads(response.text)
        assert json_response['columns'], LOGGER.error("V1 cluster is down, POST calls are failing")


@pytest.mark.depends(on=['test01_get_proxy_status'])
@pytest.mark.run(order=4)
def test05_case_post_valid_input_t_line(setup):
    """
    This test script validates the kpi proxy post api.
    media-kpi-proxy-service/api/v1/data
    This is data driven test cases, post request will be tested with different request body data sets
    """
    config, headers, json_req = setup
    obj1 = library.Utility('test_data/postrequests.xlsx', 'Sheet1')
    rov = obj1.fetch_row_count()
    keyList = obj1.fetch_key_names()
    for i in range(2, rov + 1):
        req = obj1.update_request_with_data(i, json_req, keyList)
        req['logtype'] = 't-lines'
        try:
            response = request("POST", url=config['QA']['POST_URL'], headers=headers, data=json.dumps(req),
                               verify=False)
        except Exception as error:
            LOGGER.error("HTTPS connection lost: ", error)

        assert response.status_code == 200, LOGGER.error("kpi proxy post api is failing")
        json_response = json.loads(response.text)
        assert json_response['columns'], LOGGER.error("V2 cluster is down, POST Calls are failing")


@pytest.mark.depends(on=['test01_get_proxy_status'])
def test06_post_invalid_inputs(setup):
    """
    This test script validates the kpi proxy post api.
    media-kpi-proxy-service/api/v1/data
    This is data driven test cases, post request will be tested with different invalid request body
    """

    config, headers, json_req = setup
    obj1 = library.Utility('test_data/postrequests.xlsx', 'Sheet2')
    rov = obj1.fetch_row_count()
    keyList = obj1.fetch_key_names()
    for i in range(2, rov + 1):
        print()
        req = obj1.update_request_with_data(i, json_req, keyList)
        try:
            response = request("POST", url=config['QA']['POST_URL'], headers=headers, data=json.dumps(req),
                               verify=False)
        except Exception as error:
            LOGGER.error("HTTPS connection lost", error)
        print(response.status_code)
        assert response.status_code == 400, LOGGER.error("Client side errors are not getting reported")


@pytest.mark.depends(on=['test01_get_proxy_status'])
def test_07_check_post_response_body(setup):
    """
    This test case validate the correctness of post api response body.
    """
    config, headers, json_req = setup
    json_req['sql'] = 'select * from ref_thresholds_bucket;'
    json_req['logtype'] = 'r-lines'
    try:
        response = request("POST", url=config['QA']['POST_URL'], headers=headers, data=json.dumps(json_req),
                           verify=False)
    except Exception as error:
        LOGGER.error("HTTPS connection lost", error)
    assert response.status_code == 200
    json_response = json.loads(response.text)
    assert json_response['columns'], LOGGER.error("V1 cluster is down, POST calls are failing")
    # assert response == request("GET", url=config['QA']['GET_TH_URL'], headers=headers)


@pytest.mark.depends(on=['test01_get_proxy_status'])
def test_08_test_auth_header(setup):
    """
    This test case validate the correctness of post api response body.
    """
    config, headers, json_req = setup
    try:
        response = request("POST", url=config['QA']['POST_URL'], data=json.dumps(json_req),
                           verify=False)
    except Exception as error:
        LOGGER.error("HTTPS connection lost", error)
    assert response.status_code == 401
