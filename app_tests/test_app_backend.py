from app_code.data_filtering import Data 
import pandas as pd








def test_line_chart_data():
    data_class=Data()

    line_chart_data=data_class.line_chart_data('all')

    assert isinstance(line_chart_data, list), (
        f"line_chart_data must be list, got {type(line_chart_data).__name__}. "
        "Expected format: [{'x': [...], 'y': [...]}, ...]"
    )




def test_bar_chart_data():
    data_class=Data()

    bar_chart_data=data_class.bar_chart_data()

    assert isinstance(bar_chart_data, pd.DataFrame), (
        f"bar_chart_data must be DataFrame, got {type(bar_chart_data).__name__}. "
        "Expected format: DataFrame"
    )






