
from Soul_foods.components_ids import test_bar_graph,test_header,test_sub_header,test_radio_items,test_pie_graph,test_line_graph




def test_check_for_elements(app_,dash_duo):
    #start the dash headless server
    dash_duo.start_server(app_)
    
    #find the first element wich is the header
    assert dash_duo.find_element(test_header) is not None , 'Header not found'

    #find the second element wich is the sub-header
    assert dash_duo.find_element(test_radio_items) is not None , 'the sub-header is not found'

    #find the third element wich is the radio button
    assert dash_duo.find_element(test_radio_items) is not None , 'the selectors/radio-buttons are not found'

    #find the fourth element wich is the line graph
    assert dash_duo.find_element(test_line_graph) is not None , 'the line visualizer is not found'

    #find the fifth element wich is the bar chart
    assert dash_duo.find_element(test_bar_graph) is not None , 'the bar visualize is missing'

    #find the final element wich is the pie chart
    assert dash_duo.find_element(test_pie_graph) is not None , 'the pie visualize is not found'

