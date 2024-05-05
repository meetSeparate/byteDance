from django.urls import path, re_path
from api.views import login, product, category, city, job, job_detail, test, resume, delivery, parse

urlpatterns = [
    path('login/', login.LoginView.as_view()),  # 登录接口
    path('sign/', login.SignView.as_view()),  # 注册接口
    path('product/', product.ProductView.as_view()),  # 产品信息接口
    path('category/', category.CategoryView.as_view()),  # 岗位种类接口
    path('city/', city.CityView.as_view()),  # 岗位城市接口
    path('job/', job.JobView.as_view()),  # 获取岗位列表接口
    re_path(r'job_detail/(?P<nid>\d+)/', job_detail.JobDetailView.as_view()),  # 获取岗位详情接口
    path('test/', test.TestView.as_view()),
    path('resume/', resume.ResumeView.as_view()),
    path('delivery/', delivery.DeliveryView.as_view()),
    path('parse/', parse.ParseView.as_view()),
]
