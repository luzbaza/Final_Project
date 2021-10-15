function iniciarMap(){
	var coord = {lat:6.2082569, lng: -75.5707931};
	var map = new google.maps.Map(document.getElementById('map'),{
	  zoom: 10,
	  center: coord
	});
	var marker = new google.maps.Marker({
	  position: coord,
	  map: map
	});
  }