import pytest
import yaml


def test_created(init_dir):
    assert init_dir.isdir()


def test_app_name_in_yaml(init_dir, app_name):
    with init_dir.join('weber.yml').open() as f:
        yml = yaml.load(f)
    assert yml['app']['name'] == app_name


