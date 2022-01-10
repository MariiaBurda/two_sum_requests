from django.urls import path

from .views import TwoSumRequestList, TwoSumRequestDetail


app_name = "two_sum"

urlpatterns = [
    path('two-sum/', TwoSumRequestList.as_view()),
    path('two-sum/<int:pk>', TwoSumRequestDetail.as_view())
]
