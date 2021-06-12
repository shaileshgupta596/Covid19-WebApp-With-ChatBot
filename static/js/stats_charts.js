function chartContainer(TotalCases,ActiveCases,RecoverdCases,DeathCases,MigrateCases){

var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	title:{
		text: "Covid-19 PieChart",
		fontColor:'white'
	},
	subtitles:[{
			text:'Percentage Of Cases',fontSize:18
	}],
	theme:'dark2',
	legend:{
		cursor: "pointer",
		itemclick: explodePie,
		fontColor:"white",
		fontSize:12
	},
	data: [{
		type: "pie",
		showInLegend: true,
		toolTipContent: "{name}: <strong>{y}%</strong>",
		indexLabelFontSize:18,indexLabelFontColor:'white',
		indexLabel: "{name} - {y}%",
		dataPoints: [
			{ y: (ActiveCases/TotalCases)*100, name: "Active", exploded: true },
			{ y: (DeathCases/TotalCases)*100, name: "Death" },
			{ y: (RecoverdCases/TotalCases)*100, name: "Recoverd" },	
			{ y: (MigrateCases/TotalCases)*100, name: "Migrated" }
		]
	}]
});
chart.render();




function explodePie (e) {
	if(typeof (e.dataSeries.dataPoints[e.dataPointIndex].exploded) === "undefined" || !e.dataSeries.dataPoints[e.dataPointIndex].exploded) {
		e.dataSeries.dataPoints[e.dataPointIndex].exploded = true;
	} else {
		e.dataSeries.dataPoints[e.dataPointIndex].exploded = false;
	}
	e.chart.render();


}
}



function chartContainer1(TotalCases,ActiveCases,RecoverdCases,DeathCases,MigrateCases){

var chart1 = new CanvasJS.Chart("chartContainer1", {
	animationEnabled: true,
	theme: "dark2", // "light1", "light2", "dark1", "dark2"
	title:{
		text: "Covid-19 BarGraph"
	},
	subtitles:[{
			text:'Count',fontSize:18
	}],
	axisY: {
		title: " Overall count"
	},
	data: [{        
		type: "column",  
		showInLegend: true, 
		legendMarkerColor: "grey",
		indexLabelFontSize:18,
		legendText: "Cases in India ",
		dataPoints: [      
			{ y: Number(TotalCases), label: "Total Cases" },
			{ y: Number(ActiveCases),  label: "Actice Cases" },
			{ y: Number(RecoverdCases),  label: "Recoverd Cases" },
			{ y: Number(DeathCases),  label: "Death Cases" },
			{ y: Number(MigrateCases),  label: "Migrated " },
		]
	}]
});
chart1.render();

}


function chartContainer2(ntc,nrc,ndc){

var chart2 = new CanvasJS.Chart("chartContainer2", {
	animationEnabled: true,
	theme: "dark2", // "light1", "light2", "dark1", "dark2"
	title:{
		text: "Covid-19 BarGraph"
	},
	subtitles:[{
			text:'Today New Cases Count',fontSize:18
	}],
	axisY: {
		title: "count"
	},
	data: [{        
		type: "column",  
		showInLegend: true, 
		legendMarkerColor: "grey",
		indexLabelFontSize:18,
		legendText: "Today Cases in India ",
		dataPoints: [      
			{ y: ntc, label: "New Cases" },
			{ y: nrc,  label: "Recoverd Cases" },
			{ y: ndc,  label: "Death Cases" }
		]
	}]
});
chart2.render();
}




function chartContainer3(Confirmed,Recoverd,Death,name,fromdate){

var chart3 = new CanvasJS.Chart("chartContainer3", {
	animationEnabled: true,
	theme: "dark2",
	title:{
		text: "Growth of Covid in "+name
	},
	subtitles:[{
			text:'From '+fromdate,
			fontSize:18
	}],
	axisX:{
		valueFormatString: "DD MMM",
		crosshair: {
			enabled: true,
			snapToDataPoint: true
		}
	},
	axisY: {
		title: "Number of Cases",
		crosshair: {
			enabled: true
		}
	},
	toolTip:{
		shared:true,
		text:'hello'
	},  
	legend:{
		cursor:"pointer",
		verticalAlign: "bottom",
		horizontalAlign: "left",
		dockInsidePlotArea: true,
		itemclick: toogleDataSeries
	},
	data: [{
		type: "line",
		showInLegend: true,
		name: " Total Cases Found",
		markerType: "square",
		xValueFormatString: "DD MMM, YYYY",
		dataPoints: Confirmed
	},
	{
		type: "line",
		showInLegend: true,
		name: " Total Recoverd",
		dataPoints: Recoverd
	},{
		type: "line",
		showInLegend: true,
		name: " Total Death",
		color: "#F08080",
		dataPoints: Death
	}
	]
});
chart3.render();

function toogleDataSeries(e){
	if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
		e.dataSeries.visible = false;
	} else{
		e.dataSeries.visible = true;
	}
	chart3.render();
}

}


function chartContainer4(Confirmed,Recoverd,Death,name,fromdate){

var chart4 = new CanvasJS.Chart("chartContainer4", {
	animationEnabled: true,
	theme: "dark2",
	title:{
		text: "Daily Result Covid in "+name
	},
	subtitles:[{
			text:'From '+fromdate,fontSize:18
	}],
	axisX:{
		valueFormatString: "DD MMM",
		crosshair: {
			enabled: true,
			snapToDataPoint: true
		}
	},
	axisY: {
		title: "Number of Cases",
		crosshair: {
			enabled: true
		}
	},
	toolTip:{
		shared:true,
		text:'hello'
	},  
	legend:{
		cursor:"pointer",
		verticalAlign: "bottom",
		horizontalAlign: "left",
		dockInsidePlotArea: true,
		itemclick: toogleDataSeries
	},
	data: [{
		type: "line",
		showInLegend: true,
		name: "Found",
		markerType: "square",
		xValueFormatString: "DD MMM, YYYY",
		dataPoints: Confirmed
	},
	{
		type: "line",
		showInLegend: true,
		name: "Recoverd",
		dataPoints: Recoverd
	},{
		type: "line",
		showInLegend: true,
		name: "Death",
		color: "#F08080",
		dataPoints: Death
	}
	]
});
chart4.render();

function toogleDataSeries(e){
	if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
		e.dataSeries.visible = false;
	} else{
		e.dataSeries.visible = true;
	}
	chart4.render();
}

}




