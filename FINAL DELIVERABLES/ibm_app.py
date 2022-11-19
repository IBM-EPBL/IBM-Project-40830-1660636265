import flask
from flask import request, render_template
from flask_cors import CORS
import joblib
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "<1jqY6DdhM2hZfDHiwtKxtS8rWhQMSF1aazImLUa2dBp4>"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = flask.Flask(__name__, static_url_path='')
CORS(app)

@app.route('/', methods=['GET'])
def sendHomePage():
    return render_template('sample.html')
@app.route('/', methods=['GET'])
def sendHomePage():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predictSpecies():
    having_IPhaving_IP_Address=int(request.form['having_IPhaving_IP_Address'])
    URLURL_Length = int(request.form['URLURL_Length'])
    Shortining_Service=int(request.form['Shortining_Service'])
    having_At_symbol = int(request.form['having_At_symbol'])
    double_slash_redirecting=int(request.form['double_slash_redirecting'])
    Prefix_Suffix=int(request.form['Prefix_Suffix'])
    having_Sub_Domain = int(request.form['having_Sub_Domain'])
    SSLfinal_State = int(request.form['SSLfinal_State'])
    Domain_registeration_length=int(request.form['Domain_registeration_length'])
    Favicon=int(request.form['Favicon'])
    Port = int(request.form['Port'])
    HTTPS_token = int(request.form['HTTPS_token'])
    Request_URL=int(request.form['Request_URL'])
    URL_of_Anchor=int(request.form['URL_of_Anchor'])
    Links_in_tags=int(request.form['Links_in_tags'])
    SFH=int(request.form['SFH'])
    Submitting_to_email=int(request.form['Submitting_to_email'])
    Abnormal_URL = int(request.form['Abnormal_URL'])
    Redirect=int(request.form['Redirect'])
    on_mouseover=int(request.form['on_mouseover'])
    RightClick=int(request.form['RightClick'])
    popUpWidnow=int(request.form['popUpWidnow'])
    Iframe=int(request.form['Iframe'])
    age_of_domain = int(request.form['age_of_domain'])
    DNSRecord = int(request.form['DNSRecord'])
    web_traffic=int(request.form['web_traffic'])
    Page_Rank = int(request.form['Page_Rank'])
    Google_Index=int(request.form['Google_Index'])
    Links_pointing_to_page=int(request.form['Links_pointing_to_page'])
    Statistical_report=int(request.form['Statistical_report'])

    
    
    
    
    
    X = [[ having_IPhaving_IP_Address,URLURL_Length, Shortining_Service,having_At_symbol, double_slash_redirecting,Prefix_Suffix,having_Sub_Domain,SSLfinal_State,Domain_registeration_length, Favicon,Port,HTTPS_token,Request_URL,URL_of_Anchor,Links_in_tags,SFH,Submitting_to_email,Abnormal_URL,Redirect,on_mouseover,RightClick, popUpWidnow,Iframe,age_of_domain,DNSRecord,web_traffic,Page_Rank,Google_Index,Links_pointing_to_page,Statistical_report]]
    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"field": [ 'having_IPhaving_IP_Address','URLURL_Length', 'Shortining_Service','having_At_symbol', 'double_slash_redirecting','Prefix_Suffix','having_Sub_Domain','SSLfinal_State','Domain_registeration_length',' Favicon','Port','HTTPS_token','Request_URL','URL_of_Anchor','Links_in_tags','SFH','Submitting_to_email','Abnormal_URL','Redirect','on_mouseover','RightClick', 'popUpWidnow','Iframe','age_of_domain','DNSRecord','web_traffic','Page_Rank','Google_Index','Links_pointing_to_page','Statistical_report'], "values":X}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/f7f79866-678a-4c37-a334-2938f21a0240/predictions?version=2022-11-18', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    predictions=response_scoring.json()
    predict=predictions['predictions'][0]['values'][0][0]
    print("Final Prediction:",predict)
    
    if predict==1:
            return render_template('neg.html',predict=predict)
    else:
        return render_template('pos.html',predict=predict)                

if __name__ == '__main__':
    app.run()