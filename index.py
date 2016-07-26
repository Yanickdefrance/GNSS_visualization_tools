__author__ = 'defrance'

#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi
import project2.create_map
import project2.position

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")



html = """<!DOCTYPE html>
<nav></nav>
<head>
	<meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />
    <link rel="stylesheet" type="text/css" href="http://localhost:63342/Web page/css/style.css" />
</head>
<body>
<header>
    <img src="http://www.tibco.com/blog/wp-content/uploads/2014/10/TIBCO-Spotfire-4-Ways-Data-Visualization-Will-Help-Your-Organization1.jpg" />
    <h1>Visualization Tool</h1>
</header>

<section id="choices">
    <article id="run">
        <h2>Run current scenario</h2>
        <a href="http://localhost:63342/Web%20page/map_1.html"><p>Visualize the chosen scenario</p></a>
    </article>
    <article id="create">
        <h2>Create scenario</h2>
        <a href="http://localhost:63342/Web%20page/map_2.html"><p>Place yourself the markers to create your own route</p></a>
    </article>
    <article id="change">
        <h2>Change scenario</h2>
        <p>Select the scenario you want to play</p>
        <form method="post" action="/index.py" enctype=multipqrt/form-data">
            <select name="select">
                <optgroup label="Scenario">
                    <option value="Circle">Circle</option>
                    <option value="Square">Square</option>
                    <option value="Line">Line</option>
                    <option value="Static">Static</option>
                </optgroup>
            </select>
            <input type="submit" name="change" value="Change scenario">
        </form>
    </article>
</section>

<fieldset>
    <legend>Visualisation of the
"""

html2="""
    scenario</legend>
    <div id="mapid"></div>
    <script src="sample-geojson.js" type="text/javascript"></script>
	<script src="https://npmcdn.com/leaflet@1.0.0-rc.2/dist/leaflet.js"></script>
	<script>

		var mymap = L.map('mapid').setView([51.505, -0.09], 13);

		L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpandmbXliNDBjZWd2M2x6bDk3c2ZtOTkifQ._QA7i5Mpkd_m30IGElHziw', {
			attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
				'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
				'Imagery <a href="http://mapbox.com">Mapbox</a>',
			id: 'mapbox.streets'
		}).addTo(mymap);
"""

print(html+str(form.getvalue("select"))+html2)


if form.getvalue("select") == 'None' :
    P = project2.position.data('project2/ublox/ublox_data_Static.txt')
    Q = project2.position.data('project2/spectracom/spectracom_data_Static.txt')
else :
    P = project2.position.data('project2/ublox/ublox_data_'+str(form.getvalue("select"))+'.txt')
    Q = project2.position.data('project2/spectracom/spectracom_data_'+str(form.getvalue("select"))+'.txt')


a = []
b = []
for i in range(len(P)):
    a.append([P[i][2],P[i][1]])

for i in range(len(Q)):
    b.append([Q[i][2],Q[i][1]])


html4="""

        var myLines = [{
            "type": "LineString",
            "color":"#FF0000",
            "coordinates":"""

html5="""
        }, {
            "type": "LineString",
            "coordinates":"""

html6="""
        }];

        var myStyle = {
            "color": "#ff7800"
        };

        var multipolygon = L.geoJson(myLines);
        multipolygon.addTo(mymap);
        mymap.fitBounds(multipolygon.getBounds());

        $(window).on("resize", function() {
            $("#map").height($(window).height()).width($(window).width());
            map.invalidateSize();
        }).trigger("resize");

        mymap.on('click', newMarker);

	</script>
</fieldset>


</body>
</html>
"""

print(html4+str(a)+html5+str(b)+html6)

project2.create_map.create_map(P,Q)

