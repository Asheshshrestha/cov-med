var totalcases;
var activecases;
var recoveredcases;
var deaths;


var mapboxAccessToken ='pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw';
var map = L.map('map',{ scrollWheelZoom: false}).setView([28.396676634126855, 84.5303718265432], 7.45);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=' + mapboxAccessToken, {
    id: 'mapbox.light',
    tileSize: 512,
    zoomOffset: -1
}).addTo(map);


function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
    info.update(layer.feature.properties);
}
var geojson;
geojson = L.geoJson(nepalData.features,{onEachFeature: onEachFeature,style:style}).addTo(map);
map.attributionControl.addAttribution('COVID-19 Statistics &copy; <a href="http://edcd.gov.np">EDCD/MoHP</a>');
function resetHighlight(e) {
    geojson.resetStyle(e.target);
    info.update();

}
function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight
    });
}

var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    this.update();
    return this._div;
};

// method that we will use to update the control based on feature properties passed
info.update = function (props) {
    this._div.innerHTML = '<h4>Corona virus Case</h4>' +  (props ?
        '<b>' + props.TARGET+' ('+ props.DISTRICT+ ')'+ '</b><br />' +
        'Total Cases:'+getCases(props.districtid)+ '<br/>'+
        'Active Cases:'+getActiveCases(props.districtid)+ '<br/>'+
        'Recovered Cases:'+getRecoveredCases(props.districtid)+ '<br/>'+
        'Total Deaths:'+getDeathsCases(props.districtid)+ '<br/>'
        
        : 'Hover over a district');
};
function getColor(d) {
    return d > 1000 ? '#800026' :
           d > 500  ? '#BD0026' :
           d > 200  ? '#E31A1C' :
           d > 100  ? '#FC4E2A' :
           d > 50   ? '#FD8D3C' :
           d > 20   ? '#FEB24C' :
           d > 10   ? '#FED976' :
                      '#FFEDA0';
}
function style(feature) {
    return {
        fillColor: getColor(getCases(feature.properties.districtid)),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}
function getCases(district_id){
    var cases = 0;
    $.each(coronadata.district.cases, function(index, item) {
        if (item.district == district_id) {
           cases = item.count;
        }
    });
    return cases;
}
function getActiveCases(district_id){
    var cases = 0;
    $.each(coronadata.district.active, function(index, item) {
        if (item.district == district_id) {
           cases = item.count;
        }
    });
    return cases;
}
function getRecoveredCases(district_id){
    var cases = 0;
    $.each(coronadata.district.recovered, function(index, item) {
        if (item.district == district_id) {
           cases = item.count;
        }
    });
    return cases;
}
function getDeathsCases(district_id){
    var cases = 0;
    $.each(coronadata.district.deaths, function(index, item) {
        if (item.district == district_id) {
           cases = item.count;
        }
    });
    return cases;
}
info.addTo(map);
var legend = L.control({position: 'bottomleft'});

legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = [0, 10, 20, 50, 100, 200, 500, 1000],
        labels = ['Hello'];
    
    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
    }

    return div;
};

legend.addTo(map);



