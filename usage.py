import im_dash_extension_pack
import dash
import dash_html_components as html

app = dash.Dash('')

app.scripts.config.serve_locally = True

app.layout = html.Div([
    im_dash_extension_pack.ExampleComponent(
        id='input',
        href='https://www.google.ca/',
        # label='my-label'
    ),
    # html.Div(id='output'),
    # im_dash_extension_pack.A(
    #     id ='hello456'
    # ),

])


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=9000)
