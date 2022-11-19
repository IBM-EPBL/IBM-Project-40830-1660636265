import numpy as np
import pickle
from flask import request, render_template,Flask,redirect,url_for
from flask_cors import CORS
import joblib
import response
 
app = Flask(__name__, static_url_path='')
CORS(app)
model = pickle.load(open('web_phishing.pkl', 'rb')) 


@app.route('/')
def sendHomePage():
    return render_template('sample.html')
 
@app.route('/predict')
def predictSpecies():
    return render_template('predict.html')

@app.route('/result',methods=['POST','GET'])
def result():
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

    
    
    
    
    
    va = [[ having_IPhaving_IP_Address,URLURL_Length, Shortining_Service,having_At_symbol, double_slash_redirecting,Prefix_Suffix,having_Sub_Domain,SSLfinal_State,Domain_registeration_length, Favicon,Port,HTTPS_token,Request_URL,URL_of_Anchor,Links_in_tags,SFH,Submitting_to_email,Abnormal_URL,Redirect,on_mouseover,RightClick, popUpWidnow,Iframe,age_of_domain,DNSRecord,web_traffic,Page_Rank,Google_Index,Links_pointing_to_page,Statistical_report]]
    
    prediction = model.predict(va)[0]  
    if prediction==1:
        return render_template('neg.html',predict=prediction)
    else:
        return render_template('pos.html',predict=prediction)                

if __name__ == '__main__':
    app.run(debug=True)