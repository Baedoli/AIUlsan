
from turtle import color, fillcolor
import folium

# 유곡이편한세상 좌표 ..
latitude1 = 35.5600416
longitude1 = 129.3025264
latitude2 = 35.539408
longitude2 = 129.353788
latitude3 = 35.5637475
longitude3 = 129.3128051

may_y = folium.Map(location=[latitude1, longitude1],zoom_start=15)
folium.Marker([latitude1,longitude1],tooltip='유곡이편한세상',icon=folium.Icon(color='red',icon='glyphicon-home'),popup='유곡이편한세상').add_to(may_y)
folium.Marker([latitude2,longitude2],tooltip='태화강역',icon=folium.Icon(color='blue',icon='subway',prefix='fa'),popup='태화강역').add_to(may_y)
folium.Marker([latitude3,longitude3],tooltip='디비밸리',icon=folium.Icon(color='lightgray',icon='glyphicon-user'),popup='<a href="http://www.dbvalley.com" target="_blank">디비밸리</a>').add_to(may_y)
may_y.save("mymap.html")

latitude_usa, longitude_usa = 37.33485704383146, -122.0089505445861
map_usa = folium.Map([latitude_usa,longitude_usa],zoom_start=15)
folium.Marker([latitude_usa,longitude_usa],tooltip='Apple Park',icon=folium.Icon(color='blue',icon='fa-apple',prefix='fa'),popup='<a href="http://www.apple.com" target="_blank">Apple</a>').add_to(map_usa)
folium.CircleMarker([latitude_usa,longitude_usa],radius=50,popup='Apple Park Around',color='blue',fill_color='blue').add_to(map_usa)
map_usa.save("mymap_usa.html")

lat_usa2, long_usa2 = 45.5236, -122.6750
map_stamen = folium.Map([lat_usa2,long_usa2],zoom_start=13,tiles='Stamen Terrain')
map_stamen.save("mymap_stamen.html")

lat1, long1 = 37.52860, 126.9343 
lat2, long2 = 36.6684, 138.3492 
lat3, long3 = 45.5215, -122.6261 
lat4, long4 = 51.0554, 10.6265
map_y = folium.Map(location=[lat1, long1], zoom_start=1)
folium.CircleMarker([lat1, long1], radius=70, popup='KOREA', color='red', fill_color='red').add_to(map_y) 
folium.Marker([lat1, long1], icon=folium.Icon(color='red', icon='car', prefix='fa')).add_to(map_y)
folium.CircleMarker([lat2, long2], radius=30, popup='JAPAN', color='blue', fill_color='blue',).add_to(map_y) 
folium.Marker([lat2, long2], icon=folium.Icon(color='blue', icon='car', prefix='fa')).add_to(map_y)
folium.CircleMarker([lat3, long3], radius=80, popup='USA', color='black', fill_color='black').add_to(map_y) 
folium.Marker([lat3, long3], icon=folium.Icon(color='black', icon='car', prefix='fa')).add_to(map_y)
folium.CircleMarker([lat4, long4], radius=100, popup='Germany', color='orange', fill_color='orange').add_to(map_y) 
folium.Marker([lat4, long4], icon=folium.Icon(color='orange', icon='car', prefix='fa')).add_to(map_y)
map_y.save("mymap_sales.html")
