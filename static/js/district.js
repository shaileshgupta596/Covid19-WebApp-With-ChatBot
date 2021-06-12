function district_wise_data_of_states(button){
  var url=localStorage.getItem("url");
  button.getAttribute('district')
  var state_name =  button.getAttribute('district');
  //console.log(state_name);
  var Info=""
  document.getElementById('yourorderstable').innerHTML = '<p style="color:white;font-size:20px;" align="center"><b>Loading.....</b></p>'
  
  $.post(url+"district_wise_data_of_states",{state_name:state_name},
                
          function(response){ 
            
           //console.log(response)
          if (response['Info'] !=0){
           for(var i=0;i<response['Info'].length;i++){
            Info=Info+'<tr align="center">\
                <th scope="col" class="counterCell"></th>\
                <th style="font-weight: bolder;font-size:15px;text-transform:capitalize;color:white">'+response['Info'][i][0]+'</th>\
                <th style="color: #00b3b3"><b>'+response['Info'][i][1]+' <br> + '+response['Info'][i][5]+'</b></th>\
                <th style="color: #ffff80">'+response['Info'][i][2]+'</th>\
                <th style="color:#1aff8c "> '+response['Info'][i][3]+' <br> + '+response['Info'][i][7]+'</th>\
                <th style="color: #ff5c33"> '+response['Info'][i][4]+' <br> + '+response['Info'][i][8]+'</th>\
              </tr>'
           }
         }
           document.getElementById("yourorderstable").innerHTML=Info;


          

},"json");
}

function district_page_response(li){
  var url=localStorage.getItem("url");
  var state_name =  li.value;
  //console.log(state_name);
  var Info=""
  document.getElementById('yourorderstable').innerHTML = '<p style="color:white;font-size:20px;" align="center"><b>Loading.....</b></p>'
  
  $.post(url+"district_page",{state_name:state_name},
                
          function(response){ 
            
           //console.log(response)
          if (response['DistrictInfo'] !=0){
           for(var i=0;i<response['DistrictInfo'].length;i++){
            Info=Info+'<tr align="center">\
                <th scope="col" class="counterCell"></th>\
                <th style="font-weight: bolder;font-size:15px;text-transform:capitalize;color:white">'+response['DistrictInfo'][i][0]+'</th>\
                <th style="color: #00b3b3"><b>'+response['DistrictInfo'][i][1]+' <br> + '+response['DistrictInfo'][i][5]+'</b></th>\
                <th style="color: #ffff80">'+response['DistrictInfo'][i][2]+'</th>\
                <th style="color:#1aff8c "> '+response['DistrictInfo'][i][3]+' <br> + '+response['DistrictInfo'][i][7]+'</th>\
                <th style="color: #ff5c33"> '+response['DistrictInfo'][i][4]+' <br> + '+response['DistrictInfo'][i][8]+'</th>\
              </tr>'
           }
         }
           document.getElementById("yourorderstable").innerHTML=Info;
           document.getElementById("counterContainer").style.display="block";
           document.getElementById('TotalCases').innerHTML=response['StateInfo'][1]
           document.getElementById('ActiveCases').innerHTML=response['StateInfo'][4]
           document.getElementById('RecoverdCases').innerHTML=response['StateInfo'][2]
           document.getElementById('DeathCases').innerHTML=response['StateInfo'][3]
           document.getElementById('MigratedCases').innerHTML=response['StateInfo'][9]
           document.getElementById('tc').innerHTML=response['StateInfo'][5]
      document.getElementById('ac').innerHTML='-'
      document.getElementById('rc').innerHTML=response['StateInfo'][6]
      document.getElementById('dc').innerHTML=response['StateInfo'][7]
                


          

},"json");
}
