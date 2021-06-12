from flask import Flask 
from flask import render_template,request,jsonify
from scrape_data import return_data
import scrape_data
#from db import dbconnect
import globedata


app=Flask(__name__)

@app.route('/')
def main_page():
	#result=return_data()
	return render_template('covid/try.html')

@app.route('/globe_data_for_map',methods=['POST','GET'])
def globe_data_for_map():
	if request.method == 'POST':
		data=globedata.globe_data_for_map()
		return jsonify({"Info":data})


@app.route('/globe_list_of_data',methods= ['GET','POST'])
def globe_list_of_data():
	result,world = return_data()
	tc=int(world[1].replace(',',''))
	dc=int(world[2].replace(',',''))
	rc=int(world[3].replace(',',''))
	ac=tc-(dc+rc)
	return render_template('covid/homepage.html',result = result,tc=tc,dc=dc,rc=rc,ac=ac)

@app.route('/india',methods=['GET','POST'])
def india():
	return render_template('covid/india.html')

@app.route('/fetch_data',methods=['GET','POST'])
def fetch_data():
    if request.method=='POST':
        data,india=scrape_data.india()
        return jsonify({"Info":data})


@app.route('/country_table',methods =['GET','POST'])
def country_table():
	result,india = scrape_data.india()
	tc=int(india[1].replace(',',''))
	ac=india[4]
	dc=int(india[3].replace(',',''))
	rc=int(india[2].replace(',',''))
	mc=india[9]
	return render_template('covid/countrytable.html',result=result,tc=tc,dc=dc,rc=rc,ac=ac,mc=mc,tc1=india[5],rc1=india[6],dc1=india[7])

@app.route('/district_wise_data_of_states',methods=['POST'])
def district_wise_data_of_states():
	if request.method == 'POST':
		state_name=request.form['state_name'].title()
		result = scrape_data.district_wise_state_data(state_name)
		return jsonify({"Info":result})
	else:
		return jsonify({'Info':0})

@app.route('/covid_news')
def covid_news():
	result=scrape_data.covid_news()
	return render_template('covid/covid_news.html',result=result)


@app.route('/district_page',methods =['POST','GET'])
def district_page():
	if request.method == 'POST':
		state_name = request.form['state_name'].title()
		state_info,district_info = scrape_data.district_page_response(state_name)
		return jsonify({'StateInfo':state_info,"DistrictInfo":district_info})
	state_names = scrape_data.state_name()
	return render_template('covid/district_page.html',result=state_names,flag=1)


@app.route('/india_statistic',methods=['POST','GET'])
def india_statistic():
	if request.method == 'POST':
		india_info,growth_result,daily_result=scrape_data.india_stats()
		lakh_dayrate=scrape_data.timepass()
		return jsonify({"IndiaInfo":india_info,'GrowthResult':growth_result,'DailyResult':daily_result,"LakhDayRate":lakh_dayrate})
	return render_template('covid/stats.html')

@app.route('/indian_state_stats',methods=['GET','POST'])
def indian_state_stats():
	state_names =  scrape_data.state_name()
	if request.method == 'POST':
		state_name = request.form['state_name']
		state_info,district_info = scrape_data.district_page_response(state_name)
		if scrape_data.statewise_statistic(state_name)!= "No Data":
			cl,rc,dc=scrape_data.statewise_statistic(state_name)
			return jsonify({"StateInfo":state_info,'ConfirmedList':cl,'RecoverdList':rc,'DeathList':dc})


	return render_template('covid/indian_state_stats.html',result = state_names)

if __name__ == "__main__":
    app.run(debug=True)
