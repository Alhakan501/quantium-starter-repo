#this file contains all the pytest fixtures
from  dash.testing.application_runners import import_app
from selenium.webdriver.firefox.options import Options
from dash.testing.composite import DashComposite
import pytest








@pytest.fixture()
def app_():
    return import_app('app_code.app_main') #use import_app from dash.testing.application_runners passing the app.main file path
   


@pytest.fixture()
def dash_duo(request,dash_thread_server, tmpdir):
    # Configure Firefox
    firefox_options = Options()
    firefox_options.add_argument("--headless") # make the test headless
    firefox_options.add_argument("--disable-gpu")
    firefox_options.add_argument("--window-size=1920,1080")
    
    with DashComposite(dash_thread_server,
                        browser="firefox",
                        options=firefox_options,  # Critical: Pass configured options
                        headless=True,  # Extra assurance to ensure that it's headless .ie without ui
    ) as dc:
        yield dc


