/* Map JS File*/


var map_init = function(map, options){

    var osm = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap contributors'
    });

    osm.addTo(map);

    var cartoLight = L.tileLayer("https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
    });

    var mapbox = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
        maxZoom: 18,
        id: 'satellite-streets-v9',
        accessToken: 'pk.eyJ1Ijoic3lrMWsiLCJhIjoiY2plb2JqMHllNGYydjJ3cGVmMnE2aHlkYSJ9.uXv_J38Ndp0_aHJ0r9zP4A'
    });

    var baseMaps = {
        "OpenStreetMap": osm,
        "CartoDB": cartoLight,
        "MapBox": mapbox,
    };

    var prefecture = L.geoJson(prefectureTogo, {

    });

    var cantons = new L.GeoJSON.AJAX('/canton/', {

    });

    var sanitaires = new L.GeoJSON.AJAX('/structures/', {
        onEachFeature : function(feature, layer){
            layer.bindPopup(
            "<div style=''>"+
            "Nom : <strong>"+feature.properties.nom_fs+"</strong><br/>"+
            "Localite : <strong>"+feature.properties.localite+"</strong><br/>"+
            "Region : <strong>"+feature.properties.region+"</strong><br/>"+
            "</div>"
            );
        }

    });

    var markerClusterSanitaires = L.markerClusterGroup();

    sanitaires.on("data:loaded", function(){
        markerClusterSanitaires.addLayer(sanitaires);
        markerClusterSanitaires.addTo(map);
    });


    var overLayers = {
        "Sanitaires":markerClusterSanitaires,
        "Prefectures":prefecture,
        "Cantons":cantons,
    };

    var controleLalyer = L.control.layers(baseMaps, overLayers).addTo(map);

};