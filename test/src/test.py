import requests
import os
import json


target_ip = os.getenv('TARGET_IP')
target_port = int(os.getenv('TARGET_PORT'))

url = f"http://{target_ip}:{target_port}"


def test_echo_api_simple_case():
    echo_api = url + '/api/echo'
    payload = {'hello': 'world'}

    response = requests.post(echo_api, json=payload)
    echoed_payload = json.loads(response.text)

    assert response.status_code == 200
    assert echoed_payload == payload

def test_failed():
    assert False, "You shall not pass this test"
