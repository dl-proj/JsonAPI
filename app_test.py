import datetime

from app import JsonPlaceholderAPI
from settings import TITLE, POSTS_100, STATUS_CODE, X_Content_Type_Options, X_POWERED_BY, NEW_ID

json_api = JsonPlaceholderAPI()


def test_print_posts_99():

    assert json_api.print_title_posts_99() == TITLE


def test_inject_field_posts_100():

    current_utc_time = datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")
    api_return_value = json_api.inject_time_stamp_posts_100()

    assert api_return_value["id"] == POSTS_100["id"]
    assert api_return_value["userId"] == POSTS_100["userId"]
    assert api_return_value["title"] == POSTS_100["title"]
    assert api_return_value["body"] == POSTS_100["body"]
    assert api_return_value["time"] == current_utc_time


def test_create_new_posts():

    new_posts_result = json_api.create_new_posts()

    assert new_posts_result.json()["id"] == NEW_ID
    assert new_posts_result.status_code in STATUS_CODE
    assert new_posts_result.headers["X-Powered-By"] == X_POWERED_BY


def test_delete_new_posts():

    delete_posts_result = json_api.delete_new_posts()

    assert delete_posts_result.status_code in STATUS_CODE
    assert delete_posts_result.headers["X-Content-Type-Options"] == X_Content_Type_Options
