from django.urls import path, include
import app5.views


# http://localhost:5555/app5
# path('/insert') #http://localhost:5555/app5/insert
urlpatterns = [
    path('', app5.views.start5),
    path('/test', app5.views.test, name='test'),
    path('/test/<id>', app5.views.person, name='person'),
    path('/test/del/<id>', app5.views.delete, name='delete'),
    path('/test/up/<id>', app5.views.update, name='update'),
    path('/test/up2/go', app5.views.update2, name='update2'),
    path('/js01', app5.views.js01, name='js01'),
    path('/js02', app5.views.js02, name='js02'),
    path('/js03', app5.views.js03, name='js03'),
    path('/js04', app5.views.js04, name='js04'),
    path('/js05', app5.views.js05, name='js05'),
    path('/js06', app5.views.js06, name='js06'),
    path('/js07', app5.views.js07, name='js07'),
    path('/js08', app5.views.js08, name='js08'),
    path('/js09', app5.views.js09, name='js09'),
    path('/js10', app5.views.js10, name='js10'),
    path('/js100', app5.views.js100, name='js100'),
    path('/map1', app5.views.map1, name='map1'),
    path('/map2', app5.views.map2, name='map2'),
    path('/ajax1', app5.views.ajax1, name='ajax1'),
    path('/ajax0', app5.views.ajax0, name='ajax0'),
    path('/target', app5.views.target, name='target'),
    path('/target0', app5.views.target0, name='target0'),
    path('/target00', app5.views.target00, name='target00'),
    path('/ajax2', app5.views.ajax2, name='ajax2'),
    path('/target2', app5.views.target2, name='target2'),
    path('/target3', app5.views.target3, name='target3'),
]
