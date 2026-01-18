import data
import configuration
import requests
import pytest
import sender_stand_request
import data
# Федотов Дмитрий, 39-я когорта — Финальный проект. Инженер по тестированию плюс
#
def test_one_symbol_in_name():
    track=sender_stand_request.get_track(data.order_body).json()["track"]
    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200

