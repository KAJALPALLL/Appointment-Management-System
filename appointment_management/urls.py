from . import views
from django.urls import path

urlpatterns = [
    path('create-business-history',views.create_business_history,name='create_business_history'),
    path('book-appointment/<str:id>',views.book_appointment,name='book_appointment'),
    path('clients-appointment-list',views.clients_appointment_list,name='clients_appointment_list'),
    path('business-appointment-list',views.business_appointment_list,name='business_appointment_list'),
    path('appointment-list',views.appointment_list,name='appointment_list'),
    path('terms',views.terms,name='terms'),
    path('business-man-terms',views.business_man_terms,name='business_man_terms'),

]