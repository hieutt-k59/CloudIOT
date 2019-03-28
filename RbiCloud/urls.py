"""RbiCloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cloud import views
from django.conf.urls import handler404
from django.conf.urls import handler500
import django.views.static
from RbiCloud import settings
from django.conf import settings as set_
from django.conf.urls.static import static
urlpatterns = [
    # path('static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),
    path('admin/', admin.site.urls),
    path('', views.signin, name='home'),
    path('citizen/', views.citizen_home, name= 'citizenHome'),
    path('basecitizen/',views.Base_citizen,name='basecitizen'),
    path('basemanagement/', views.base_manager, name= 'basemanager'),
    path('basebusiness/',views.base_business,name='basebusiness'),
    path('business/', views.business_home, name='business'),
    path('equipment/', views.base_equipment, name='equipment'),
    path('component/', views.base_component, name='component'),
    path('proposal/', views.base_proposal, name='prosal'),
    path('risksummary/', views.base_risksummary, name='risk'),
    path('designcode/', views.base_designcode, name='designcode'),
    path('manufacture/', views.base_manufacture, name= 'manufacture'),
    ########################## Facility UI################################
    path('facilities/display/<int:siteID>/', views.ListFacilities, name='facilitiesDisplay'),
    path('facilities/<int:siteID>/new/', views.NewFacilities, name='facilitiesNew'),
    path('facilities/<int:facilityID>/edit/', views.EditFacilities, name= 'facilitiesEdit'),
    path('designcode/display/<int:siteID>/', views.ListDesignCode, name='designcodeDisplay'),
    path('designcode/<int:siteID>/new/', views.NewDesignCode, name='designcodeNew'),
    path('designcode/<int:designcodeID>/edit/', views.EditDesignCode, name='designcodeEdit'),
    path('manufacture/display/<int:siteID>/', views.ListManufacture, name='manufactureDisplay'),
    path('manufacture/<int:siteID>/new/', views.NewManufacture , name='manufactureNew'),
    path('manufacture/<int:manufactureID>/edit/', views.EditManufacture, name='manufactureEdit'),
    path('equipment/display/<int:facilityID>/', views.ListEquipment, name='equipmentDisplay'),
    path('equipment/<int:facilityID>/new/', views.NewEquipment, name='equipmentNew'),
    path('equipment/<int:equipmentID>/edit/', views.EditEquipment, name='equipmentEdit'),
    path('component/display/<int:equipmentID>/', views.ListComponent, name='componentDisplay'),
    path('component/<int:equipmentID>/new/', views.NewComponent , name='componentNew'),
    path('component/<int:componentID>/edit/', views.EditComponent, name='componentEdit'),
    path('proposal/display/<int:componentID>/', views.ListProposal, name='proposalDisplay'),
    path('proposal/<int:componentID>/new/', views.NewProposal, name='proposalNew'),
    path('tank/<int:componentID>/new/', views.NewTank , name='tankNew'),
    path('proposal/<int:proposalID>/edit/', views.EditProposal, name='prosalEdit'),
    path('tank/<int:proposalID>/edit/', views.EditTank, name='tankEdit'),
    path('proposal/<int:proposalID>/risk-matrix/', views.RiskMatrix, name='riskMatrix'),
    path('proposal/<int:proposalID>/damage-factor/', views.FullyDamageFactor, name='damgeFactor'),
    path('proposal/<int:proposalID>/chart/', views.RiskChart, name='riskChart'),
    path('proposal/<int:proposalID>/fully-consequence/',views.FullyConsequence, name='fullyConsequence'),
    path('export/<int:index>/<str:type>/', views.ExportExcel, name='exportData'),
    path('site/<int:siteID>/upload/InspectionHistory/', views.uploadInspPlan, name='upload'),
    path('site/<int:siteID>/upload/Plan/', views.upload, name='uploadPlan'),
    path('forum/',views.base_forum,name='forum'),
    path('forum/post/<int:postID>',views.posts_forum,name='posts'),
    path('logout',views.logout,name='logout'),
    path('massages/',views.MassagesHome,name='massages'),
    path('Massagessent/',views.Email_Massage_sent,name='massagessent'),
    # path('proposal/<int:proposalID>/dataa/', views.dataa, name='dataa'),
    path('help/',views.Help, name='help'),
    path('AccountCitizen/', views.AccountCitizen, name='accountcitizen'),
    path('AccountBusiness/',views.AccountBusiness, name='accountbusiness'),
    path('AccountManagement',views.AccountManagement,name='accountmanagement'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    #### manager ####
    path('management/<int:siteID>/', views.ManagerHome, name= 'manager'),
    path('facilitiesMana/display/<int:siteID>/', views.ListFacilitiesMana, name='facilitiesDisplayMana'),
    path('equipmentMana/display/<int:facilityID>/', views.ListEquipmentMana, name='equipmentDisplayMana'),
    path('componentMana/display/<int:equipmentID>/', views.ListComponentMana, name='componentDisplayMana'),
    path('proposalMana/display/<int:componentID>/', views.ListProposalMana, name='proposalDisplayMana'),
    path('proposalMana/<int:proposalID>/data/', views.Inputdata, name='inputdata'),
    path('proposalMana/<int:proposalID>/damage-factor/', views.FullyDamageFactorMana, name='damgeFactorMana'),
    path('proposalMana/<int:proposalID>/chart/', views.RiskChartMana, name='riskChartMana'),
    path('proposalMana/<int:proposalID>/risk-matrix/', views.RiskMatrixMana, name='riskMatrixMana'),
    path('proposalMana/<int:proposalID>/fully-consequence/',views.FullyConsequenceMana, name='fullyConsequenceMana'),
    path('data_sensor/<int:mac_sensor>/', views.data_sensor_chart, name='sensor_chart'),
    path('pub/', views.mosquitto_mqtt_pub, name='mosPub'),
    path('json/temperature1/', views.get_json_tem, name='viewTemData'),
    path('json/temperature/', views.get_tem, name='viewTem'),
    path('chart/<int:sensorID>', views.show_chart_sensor, name='showChart'),
    path('gateway/<int:facilityID>/new', views.new_gateway, name='gwNew'),
    path('gateway/display/<int:facilityID>/', views.ListGateway, name='gatewayDisplay'),
    path('sensor/display/<int:gatewayID>/', views.ListSensor, name='sensorDisplay'),
]

urlpatterns += static(set_.STATIC_URL, document_root=set_.STATIC_ROOT)

handler404 = 'cloud.views.handler404'
handler500 = 'cloud.views.handler404'