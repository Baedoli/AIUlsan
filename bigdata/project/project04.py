
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
folium.Marker([latitude2,longitude2],tooltip='태화강역',icon=folium.Icon(color='blue',icon='glyphicon-road'),popup='태화강역').add_to(may_y)
folium.Marker([latitude3,longitude3],tooltip='디비밸리',icon=folium.Icon(color='lightgray',icon='glyphicon-user'),popup='디비밸리').add_to(may_y)
may_y.save("mymap.html")
