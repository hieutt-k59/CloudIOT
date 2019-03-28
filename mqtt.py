import os
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'RbiCloud.settings'
application = get_wsgi_application()

from cloud import models
import paho.mqtt.client as mqtt
import json
from datetime import datetime
from cloud.process.RBI import fastCalulate as ReCalculate

# This is the Subscriber
TOPIC = "+/+"
def on_connect(client, userdata, flags, rc):
    client.subscribe(TOPIC, 0)
    print("Connected MosquittoMQTT with result code " + str(rc))
# def on_subcribe(client, obj, mid, granted_qos):
#     print("Subscribed: " + str(mid) + " " + str(granted_qos))
def on_log(client, obj, level, string):
    print(string)
def on_message(client, userdata, msg):
    split_arr = (str(msg.topic)).split('/')
    payload = msg.payload.decode()
    data = json.loads(payload)
    print(split_arr[0])
    #topic "comp_id/assessment_name" or "sensor/sensor_id"
    # if split_arr[0] == "sensor":
    #     sensor_id = split_arr[1]
    #     time_get = datetime(year=int(data[0]), month=int(data[1]), day=int(data[2]), hour=int(data[3]), minute=int(data[4]))
    #     humi = float(data[5])
    #     tem = float(data[6])
    #     s = models.DataSensor(mac_sensor=sensor_id, humi=humi, temp=tem, time_get=time_get)
    #     s.save()
    # else :
    comp_id = split_arr[0]
    assess = split_arr[1]
    comp = models.ComponentMaster.objects.get(componentid= int(comp_id))
    facility_id = models.EquipmentMaster.objects.get(equipmentid=comp.equipmentid_id).facilityid_id
    target = models.FacilityRiskTarget.objects.get(facilityid=facility_id)
    faci = models.Facility.objects.get(facilityid=facility_id)
    data["APIComponentTypeID"] = models.ApiComponentType.objects.get(apicomponenttypeid=comp.apicomponenttypeid).apicomponenttypename
    data['equipmentType'] = models.EquipmentType.objects.get(equipmenttypeid=models.EquipmentMaster.objects.get(equipmentid=comp.equipmentid_id).equipmenttypeid_id).equipmenttypename
    data['AssessmentDate'] = datetime.now()
    rw_assessment = models.RwAssessment(equipmentid_id=comp.equipmentid_id, componentid_id=comp.componentid, 
        assessmentdate=data['AssessmentDate'], riskanalysisperiod=data['RiskAnalystPeriod'], 
        isequipmentlinked= comp.isequipmentlinked, proposalname=assess)
    rw_assessment.save()
    rw_equipment = models.RwEquipment(id=rw_assessment, commissiondate=models.EquipmentMaster.objects.get(equipmentid= comp.equipmentid_id).commissiondate,
        adminupsetmanagement=data["AdminControlUpset"], containsdeadlegs=data["ContainsDeadlegs"],
        cyclicoperation=data["CylicOper"], highlydeadleginsp=data["Highly"],
        downtimeprotectionused=data["Downtime"], externalenvironment=data['ExternalEnvironment'],
        heattraced=data["HeatTraced"], interfacesoilwater=data["InterfaceSoilWater"],
        lineronlinemonitoring=data["LOM"], materialexposedtoclext=data["MFTF"],
        minreqtemperaturepressurisation=data["minTemp"],
        onlinemonitoring=data['OnlineMonitoring'], presencesulphideso2=data["PresenceofSulphides"],
        presencesulphideso2shutdown=data["PresenceofSulphidesShutdown"],
        pressurisationcontrolled=data["PressurisationControlled"], pwht=data["PWHT"], steamoutwaterflush=data["SteamedOut"],
        managementfactor= faci.managementfactor, thermalhistory=data['ThermalHistory'],
        yearlowestexptemp=data["EquOper"], volume=data["EquipmentVolumn"])
    rw_equipment.save()
    rwcomponent = models.RwComponent(id=rw_assessment, nominaldiameter=data["NorminalDiameter"],
        nominalthickness=data['NorminalThickness'], currentthickness=data['CurrentThickness'],
        minreqthickness=data['MinReqThickness'], currentcorrosionrate=data['CurrentCorrosionRate'],
        branchdiameter=data['BranchDiameter'], branchjointtype=data['BranchJointType'],
        brinnelhardness=data['MaxBrinell']
        , deltafatt=data['DeltaFATT'], chemicalinjection=data["ChemicalInjection"],
        highlyinjectioninsp=data["HFICI"], complexityprotrusion=data['complex'],
        correctiveaction=data['CorrectiveAction'], crackspresent=data["PresenceCracks"],
        cyclicloadingwitin15_25m=data['CylicLoad'],
        damagefoundinspection=data["DFDI"], numberpipefittings=data['NumberPipeFittings'],
        pipecondition=data['PipeCondition'],
        previousfailures=data['PreviousFailures'], shakingamount=data['ShakingAmount'],
        shakingdetected=data["VASD"], shakingtime=data['timeShakingPipe'],
        trampelements=data["TrampElements"])
    rwcomponent.save()
    rwstream = models.RwStream(id=rw_assessment, aminesolution=data['AminSolution'], aqueousoperation=data["AqueOp"],
        aqueousshutdown=data["AqueShutdown"], toxicconstituent=data["ToxicConstituents"],
        caustic=data["EnvCaustic"],
        chloride=data['ChlorideIon'], co3concentration=data['CO3'], cyanide=data["PresenceCyanides"],
        exposedtogasamine=data["exposureAcid"], exposedtosulphur=data["ExposedSulfur"],
        exposuretoamine=data['ExposureAmine'],
        h2s=data["EnvCH2S"], h2sinwater=data["H2SInWater"], hydrogen=data["hydrogen"],
        hydrofluoric=data["HydrogenFluoric"], materialexposedtoclint=data["materialExposedFluid"],
        maxoperatingpressure=data['maxOP'],
        maxoperatingtemperature=float(data['maxOT']), minoperatingpressure=float(data['minOP']),
        minoperatingtemperature=data['minOT'], criticalexposuretemperature=data['CriticalTemp'],
        naohconcentration=data['NaOHConcentration'],
        releasefluidpercenttoxic=float(data['ReleasePercentToxic']),
        waterph=float(data['PHWater']), h2spartialpressure=float(data['OpHydrogenPressure']))
    rwstream.save()
    rwexcor = models.RwExtcorTemperature(id=rw_assessment, minus12tominus8=data['Op1'], 
        minus8toplus6=data['Op2'], plus6toplus32=data['Op3'], plus32toplus71=data['Op4'],
        plus71toplus107=data['Op5'], plus107toplus121=data['Op6'], plus121toplus135=data['Op7'],
        plus135toplus162=data['Op8'], plus162toplus176=data['Op9'], morethanplus176=data['Op10'])
    rwexcor.save()
    rwcoat = models.RwCoating(id=rw_assessment, externalcoating=data["ExternalCoating"], 
        externalinsulation=data["ExternalInsulation"],
        internalcladding=data["InternalCladding"], internalcoating=data["InternalCoating"],
        internallining=data["InternalLining"], externalcoatingdate=data["ExternalCoatingDate"],
        externalcoatingquality=data['ExternalCoatingQuality'], externalinsulationtype=data["ExternalInsulationType"],
        insulationcondition=data['InsulationCondition'], insulationcontainschloride=data["InsulationCholride"],
        internallinercondition=data['InternalLinerCondition'], internallinertype=data['InternalLinerType'],
        claddingcorrosionrate=data["CladdingCorrosionRate"], supportconfignotallowcoatingmaint=data["supportMaterial"])
    rwcoat.save()
    rwmaterial = models.RwMaterial(id=rw_assessment, corrosionallowance=data["CorrosionAllowance"], materialname=data['Material'],
        designpressure=data['DesignPressure'], designtemperature=data['MaxDesignTemp'], ishtha=data["MaterialHTHA"],
        mindesigntemperature=data['MinDesignTemp'], brittlefracturethickness=data['BrittleFacture'], 
        sigmaphase=data['SigmaPhase'], sulfurcontent=data["SulfurContent"], heattreatment=data['heatTreatment'],
        referencetemperature=data["tempRef"], ptamaterialcode=data['PTAMaterialGrade'], 
        hthamaterialcode=data['HTHAMaterialGrade'], ispta=data["MaterialPTA"], austenitic=data["AusteniticSteel"], 
        temper=data["SusceptibleTemper"], carbonlowalloy=data["CarbonAlloySteel"], nickelbased=data["NickelAlloy"], 
        chromemoreequal12=data["Chromium"], allowablestress=data['allowStress'], costfactor=data['MaterialCostFactor'])
    rwmaterial.save()
    rwinputca = models.RwInputCaLevel1(id=rw_assessment, api_fluid=data['APIFluid'], system=data['System'],
        release_duration=data['ReleaseDuration'], detection_type=data['DetectionType'],
        isulation_type=data['InsulationType'],
        mitigation_system=data['MitigationSystem'],
        equipment_cost=data['EquipmentCost'], injure_cost=data['InjureCost'],
        evironment_cost=data['EnvironmentCost'], toxic_percent=data['ToxicPercent'],
        personal_density=data['PersonDensity'],
        material_cost=data['MaterialCostFactor'],
        production_cost=data['ProductionCost'], mass_inventory=data['MassInventory'],
        mass_component=data['MassComponent'],
        stored_pressure=float(data['minOP']) * 6.895, stored_temp=data['minOT'])
    rwinputca.save()
    print("Calculating...")
    ReCalculate.ReCalculate(rw_assessment.id)
    print("Finished!")
    
    # client.disconnect()

CLOUD_URL = 'localhost'

PORT = 1883
client = mqtt.Client()
client.connect(CLOUD_URL,PORT)

client.on_connect = on_connect
client.on_message = on_message