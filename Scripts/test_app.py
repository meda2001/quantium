import dash
from dash import dcc, html
from dash.testing.application_runners import import_app
from dash.testing.application_runners import wait_for
import pytest

# Import your app layout and create a Dash test app
app = import_app('my_dash_app.app')

# Define tests
def test_header_present():
    """
    Test if the header is present.
    """
    # Start the app in a test mode
    with app() as test_app:
        # Find the header element by its CSS selector
        header = test_app.find_element("h1")
        assert header.text == "Soul Foods Sales Visualization"

def test_visualization_present():
    """
    Test if the visualization is present.
    """
    # Start the app in a test mode
    with app() as test_app:
        # Find the visualization element by its ID
        visualization = test_app.find_element("sales-chart")
        assert visualization is not None

def test_region_picker_present():
    """
    Test if the region picker is present.
    """
    # Start the app in a test mode
    with app() as test_app:
        # Find the region picker element by its ID
        region_picker = test_app.find_element("region-radio")
        assert region_picker is not None

if __name__ == '__main__':
    pytest.main([__file__])
