from django.urls import path
from . import views
from .views import thank_you


urlpatterns = [
    path('', views.register_student, name='register_student'),
    path('organiser/search/', views.organiser_search, name='organiser_search'),
    path('organiser/confirm/<int:registration_id>/', views.confirm_ticket, name='confirm_ticket'),
    path('organiser/dashboard/', views.organiser_dashboard, name='organiser_dashboard'),
    path('custom_admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('custom_admin/dashboard/chart-data/', views.ticket_confirmation_data, name='ticket_confirmation_data'),
    path('no-permission/', views.no_permission, name='no_permission'),
    path('organiser/registration/<int:registration_id>/', views.registration_detail, name='registration_detail'),
    path('custom_admin/dashboard/confirmed-tickets/', views.confirmed_tickets_list, name='confirmed_tickets_list'),
    path('custom_admin/dashboard/organiser-cash-summary/', views.organiser_cash_daywise, name='organiser_cash_daywise'),
    path('thank-you/', thank_you, name='thank_you'),

]


