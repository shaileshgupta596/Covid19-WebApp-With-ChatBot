from scrape_data import globe_data,return_data
import country_converter as coco
import random 
def globe_data_for_map():
	country_list ,worldwide=  return_data()
	countries=[]
	for country in country_list:
		countries.append(country[0].title())


	standard_names = coco.convert(names=countries, to='ISO2')
	updated_list=[]

	if len(standard_names) == len(country_list):
		for i in range(0,len(country_list)):
			if standard_names[i]!='not found':
				small=[]
				small.append(standard_names[i])
				small.append(country_list[i])
				updated_list.append(small)

	return updated_list
#globe_data_for_map()