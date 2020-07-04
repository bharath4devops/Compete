from django.urls import path 
from . import views

urlpatterns = [
			path('list/', views.getlists, name = 'list'),
			path('detail/<int:Id>', views.detail, name = 'detail'),
			path('list_kn/', views.getlists_kn, name = 'list'),
			path('detail_kn/<int:Id>', views.detail_kn, name = 'detail'),
			path('list_mr/', views.getlists_mr, name = 'list'),
			path('detail_mr/<int:Id>', views.detail_mr, name = 'detail'),
			path('list_ml/', views.getlists_ml, name = 'list'),
			path('detail_ml/<int:Id>', views.detail_ml, name = 'detail'),
			path('list_pa/', views.getlists_pa, name = 'list'),
			path('detail_pa/<int:Id>', views.detail_pa, name = 'detail'),
			path('list_gu/', views.getlists_gu, name = 'list'),
			path('detail_gu/<int:Id>', views.detail_gu, name = 'detail'),
			path('list_te/', views.getlists_te, name = 'list'),
			path('detail_te/<int:Id>', views.detail_te, name = 'detail'),
			path('list_ta/', views.getlists_ta, name = 'list'),
			path('detail_ta/<int:Id>', views.detail_ta, name = 'detail'),
			path('list_or/', views.getlists_or, name = 'list'),
			path('detail_or/<int:Id>', views.detail_or, name = 'detail'),
			path('list_ur/', views.getlists_ur, name = 'list'),
			path('detail_ur/<int:Id>', views.detail_ur, name = 'detail'),
			path('list_hi/', views.getlists_hi, name = 'list'),
			path('detail_hi/<int:Id>', views.detail_hi, name = 'detail'),
			path('material/<str:dept>', views.getMaterial, name = 'material'),
			path('dept/<str:st>', views.getDept, name = 'department'),
			]