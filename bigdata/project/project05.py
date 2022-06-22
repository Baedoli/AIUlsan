
import base64
import folium
import os

path = os.getcwd()
path

lat1, long1 = 37.465323, 126.948741
lat2, long2 = 35.231701, 129.084565
img1 = path+'/Seoul_National_University.jpg'
img2 = path+'/Pusan_National_Universiry.jpg'

m = folium.Map(location=[lat1,long1],zoom_start=6)

pic1 = base64.b64encode(open(img1,'rb').read()).decode()
image_tag1 = '<img src="data:image/jpeg;base64,{}">'.format(pic1)
image_tag1 = '<a href="https://www.snu.ac.kr/" target="_blank">'+image_tag1+'</a>'
iframe1 = folium.IFrame(image_tag1,width=510,height=165)
popup1 = folium.Popup(iframe1,max_width=650)

pic2 = base64.b64encode(open(img2,'rb').read()).decode()
image_tag2 = '<img src="data:image/jpeg;base64,{}">'.format(pic2)
image_tag2 = '<a href="https://www.pusan.ac.kr/kor/Main.do" target="_blank">'+image_tag2+'</a>'
iframe2 = folium.IFrame(image_tag2,width=300,height=120)
popup2 = folium.Popup(iframe2,max_width=650)

folium.Marker([lat1,long1],popup=popup1,tooltip='서울대학교 정문').add_to(m)
folium.Marker([lat2,long2],popup=popup2,tooltip='부산대학교 정문').add_to(m)
m.save("mymap_university.html")

