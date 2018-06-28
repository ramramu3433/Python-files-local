# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 16:33:18 2018

@author: janakiraman.r
"""


import pandas
import requests,json
import dash
import dash_core_components as dcc
import dash_html_components as html


df=pandas
data=df.read_excel("Requirements_TestCases_Defects - v5.xlsx",workbook="RequirementsVsTestCases")
#print(data)
dir(data)
t=data.to_json(orient='records',lines=True)
final_json_string= ' '
for k in t.split('\n'):
    msg=json.loads(k)
    _id=msg['Req ID']
    metadata = json.dumps({'index': {'_id': msg['Req ID']}})
    msg.pop('Req ID')
    final_json_string += metadata + '\n' + json.dumps(msg) + '\n'


headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post('http://localhost:9200/testdb/tcases/_bulk', data=final_json_string, headers=headers, timeout=60) 
#t=json.loads(t)


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), 100))]
    )

     
app = dash.Dash()

app.layout = html.Div(children=[
    html.H4(children='Test case reports'),
    generate_table(data)
])

if __name__ == '__main__':
    app.run_server(debug=True)