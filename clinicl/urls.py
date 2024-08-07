from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from clinicApp import views
from .views import HomeView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('doctor-profile/', views.doctor_profile_link, name='doctor-profile-link'),
    path('doctor-home/', views.doctor_home, name='doctor-home'),
    path('login-signup/', views.login_signup_view, name='login-signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('save_user_info/', views.save_user_info, name='save_user_info'),
    path('send_reset_code/', views.send_reset_code, name='send_reset_code'),
    path('reset_password/', views.reset_password, name='reset_password/'),
    path('send_reset_code_login/', views.send_reset_code_login, name='send_reset_code_login'),
    path('reset_password_login/', views.reset_password_login, name='reset_password_login/'),
    path('attach-page/', views.attach_page, name='attach-page'),
    path('save_organization/', views.save_organization, name='save_organization'),
    path('profile_link/', views.profile_link, name='profile_link'),
    path('handle_image_upload/', views.handle_image_upload, name='handle_image_upload'),
    path('get-doctors/<str:clinic_ext_id>/', views.get_doctors_by_clinic, name='get-doctors-by-clinic'),
    path('appoint_doctor/', views.appoint_doctor, name='appoint_doctor'),
    path('update_doctor/', views.update_doctor, name='update_doctor'),
    path('find_user_view/', views.find_user_view, name='find_user_view'),
    path('create_appointment/', views.create_appointment, name='create_appointment'),
    path('medical_history/', views.medical_history, name='medical_history'),
    path('cancel-appointment/<int:appointment_id>', views.cancel_appointment, name='cancel-appointment'),
    path('save_comment/', views.save_comment, name='save_comment'),
    path('detach_patient/<str:iin>/', views.detach_patient, name='detach_patient'),
    path('create_prescription/', views.create_prescription, name='create_prescription'),
    path('get_prescriptions/', views.get_prescriptions, name='get_prescriptions'),
    path('download_prescription/<int:prescription_id>/', views.download_prescription_pdf, name='download_prescription'),
    path('create_appointment_first/', views.create_appointment_first, name='create_appointment_first'),
    path('create_referral/', views.create_referral, name='create_referral'),
    path('get_referrals/', views.get_referrals, name='get_referrals'),
    path('referrals/', views.referrals, name='referrals'),
    path('prescriptions/', views.prescriptions_view, name='prescriptions'),
    path('create_test_result/', views.create_test_result, name='create_test_result'),
    path('get_test_results/', views.get_test_results, name='get_test_results'),
    path('patient/test-results/', views.patient_test_results, name='patient_test_results'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)