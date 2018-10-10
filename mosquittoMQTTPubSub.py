import paho.mqtt.client as mqtt
import json
# from cloud.process.RBI import DM_CAL

# This is the Publisher
# d = DM_CAL.DM_CAL(HighlyEffectDeadleg=True, ContainsDeadlegs=False, OnlineMonitoring="Sulfuric acid (H2S/H2) corrosion high velocity - Key process parameters")
# print(d.DF_THIN(5.08))
def set_data(Op7, BrittleFacture, MaterialHTHA, H2SInWater, DesignPressure, ReleasePercentToxic, PresenceofSulphides, 
    PreviousFailures, EnvCaustic, maxOP, CylicLoad, minOP, tempRef, ExternalCoatingQuality, NumberPipeFittings, 
    MaterialPTA, PTAMaterialCode, CostFactor, AdminControlUpset, ExternalInsulationType, HydrogenFluoric, Downtime, NorminalDiameter, 
    InternalCladding, APIFluid, DeltaFATT, maxOT, PWHT, ToxicConstituents, MaxDesignTemp, MinDesignTemp, SteamedOut, 
    PresenceCracks, PersonDensity, heatTreatment, PressurisationControlled, ExposureAmine, SulphurContent, 
    InternalLinerType, CylicOper, DetectionType, EquipmentVolumn, Chromium, PHWater, CurrentCorrosionRate, minOT, 
    CarbonAlloySteel, EnvironmentCost, InterfaceSoilWater, Highly, BranchDiameter, ExternalCoatingDate, Op2, 
    ChemicalInjection, NaOHConcentration, Op1, ExternalInsulation, CurrentThickness, Op9, NorminalThickness, 
    ReleaseDuration, System, HTHAMaterialGrade, Material, ExternalCoating, CriticalTemp, MassInventory, CO3, 
    materialExposedFluid, Op6, ThermalHistory, InsulationType, CorrectiveAction, Op4, OnlineMonitoring, exposureAcid, 
    AusteniticSteel, supportMaterial, EquipmentCost, ProductionCost, LOM, ToxicPercent, EnvCH2S, 
    OpHydrogenPressure, minTemp, hydrogen, ContainsDeadlegs, PresenceCyanides, HFICI, ExposedSulfur, TrampElements, 
    CladdingCorrosionRate, Op10, CorrosionAllowance, SusceptibleTemper, InternalCoating, InternalLinerCondition, 
    RiskAnalystPeriod, ShakingAmount, ChlorideIon, Op8, AqueOp, InsulationCondition, AqueShutdown, 
    PresenceofSulphidesShutdown, DFDI, BranchJointType, HeatTraced, NickelAlloy, AminSolution, InternalLining, 
    allowStress, MitigationSystem, VASD, ExternalEnvironment, Op3, MaxBrinell, timeShakingPipe, SigmaPhase, 
    InsulationCholride, MassComponent, EquOper, MFTF, InjureCost, PipeCondition, complex, MinReqThickness, Op5, SulfurContent):
    data = {}
    data["AminSolution"] = AminSolution
    data["HTHAMaterialGrade"] = HTHAMaterialGrade
    data["Op8"] = Op8
    data["CurrentCorrosionRate"] = CurrentCorrosionRate
    data["PWHT"] = PWHT
    data["Highly"] = Highly
    data["ToxicConstituents"] = ToxicConstituents
    data["ExternalInsulation"] = ExternalInsulation
    data["HydrogenFluoric"] = HydrogenFluoric
    data["TrampElements"] = TrampElements
    data["Downtime"] = Downtime
    data["InterfaceSoilWater"] = InterfaceSoilWater
    data["maxOP"] = maxOP
    data["supportMaterial"] = supportMaterial
    data["CriticalTemp"] = CriticalTemp
    data["exposureAcid"] = exposureAcid
    data["MitigationSystem"] = MitigationSystem
    data["BranchDiameter"] = BranchDiameter
    data["CorrectiveAction"] = CorrectiveAction
    data["PersonDensity"] = PersonDensity
    data["EquipmentVolumn"] = EquipmentVolumn
    data["Chromium"] = Chromium
    data["ExternalEnvironment"] = ExternalEnvironment
    data["NumberPipeFittings"] = NumberPipeFittings
    data["ExposureAmine"] = ExposureAmine
    data["allowStress"] = allowStress
    data["CarbonAlloySteel"] = CarbonAlloySteel
    data["CurrentThickness"] = CurrentThickness
    data["MaxDesignTemp"] = MaxDesignTemp
    data["CO3"] = CO3
    data["ChlorideIon"] = ChlorideIon
    data["heatTreatment"] = heatTreatment
    data["InsulationCholride"] = InsulationCholride
    data["MassComponent"] = MassComponent
    data["CorrosionAllowance"] = CorrosionAllowance
    data["InsulationCondition"] = InsulationCondition
    data["AusteniticSteel"] = AusteniticSteel
    data["minOP"] = minOP
    data["InternalCoating"] = InternalCoating
    data["InternalLinerType"] = InternalLinerType
    data["AqueOp"] = AqueOp
    data["Material"] = Material
    data["BranchJointType"] = BranchJointType
    data["RiskAnalystPeriod"] = RiskAnalystPeriod
    data["PHWater"] = PHWater
    data["EnvCaustic"] = EnvCaustic
    data["PreviousFailures"] = PreviousFailures
    data["EquOper"] = EquOper
    data["InternalCladding"] = InternalCladding
    data["HFICI"] = HFICI
    data["ReleasePercentToxic"] = ReleasePercentToxic
    data["System"] = System
    data["Op10"] = Op10
    data["Op6"] = Op6
    data["APIFluid"] = APIFluid
    data["materialExposedFluid"] = materialExposedFluid
    data["SulphurContent"] = SulphurContent
    data["CladdingCorrosionRate"] = CladdingCorrosionRate
    data["ExternalCoating"] = ExternalCoating
    data["Op3"] = Op3
    data["CylicLoad"] = CylicLoad
    data["EquipmentCost"] = EquipmentCost
    data["NorminalThickness"] = NorminalThickness
    data["InternalLinerCondition"] = InternalLinerCondition
    data["InternalLining"] = InternalLining
    data["ExternalCoatingQuality"] = ExternalCoatingQuality
    data["maxOT"] = maxOT
    data["OpHydrogenPressure"] = OpHydrogenPressure
    data["MinDesignTemp"] = MinDesignTemp
    data["ReleaseDuration"] = ReleaseDuration
    data["EnvironmentCost"] = EnvironmentCost
    data["PresenceofSulphidesShutdown"] = PresenceofSulphidesShutdown
    data["NaOHConcentration"] = NaOHConcentration
    data["MinReqThickness"] = MinReqThickness
    data["DesignPressure"] = DesignPressure
    data["ExternalInsulationType"] = ExternalInsulationType
    data["HeatTraced"] = HeatTraced
    data["NickelAlloy"] = NickelAlloy
    data["PipeCondition"] = PipeCondition
    data["SigmaPhase"] = SigmaPhase
    data["Op2"] = Op2
    data["DetectionType"] = DetectionType
    data["PressurisationControlled"] = PressurisationControlled
    data["MFTF"] = MFTF
    data["MassInventory"] = MassInventory
    data["ExternalCoatingDate"] = ExternalCoatingDate
    data["AdminControlUpset"] = AdminControlUpset
    data["MaterialHTHA"] = MaterialHTHA
    data["NorminalDiameter"] = NorminalDiameter
    data["complex"] = complex
    data["MaterialPTA"] = MaterialPTA
    data['PTAMaterialGrade'] = PTAMaterialCode
    data["MaterialCostFactor"] = CostFactor
    data["OnlineMonitoring"] = OnlineMonitoring
    data["ProductionCost"] = ProductionCost
    data["PresenceCracks"] = PresenceCracks
    data["Op7"] = Op7
    data["EnvCH2S"] = EnvCH2S
    data["hydrogen"] = hydrogen
    data["timeShakingPipe"] = timeShakingPipe
    data["Op5"] = Op5
    data["SteamedOut"] = SteamedOut
    data["AqueShutdown"] = AqueShutdown
    data["InjureCost"] = InjureCost
    data["PresenceofSulphides"] = PresenceofSulphides
    data["Op9"] = Op9
    data["DeltaFATT"] = DeltaFATT
    data["minTemp"] = minTemp
    data["InsulationType"] = InsulationType
    data["ExposedSulfur"] = ExposedSulfur
    data["Op1"] = Op1
    data["PresenceCyanides"] = PresenceCyanides
    data["tempRef"] = tempRef
    data["Op4"] = Op4
    data["H2SInWater"] = H2SInWater
    data["ThermalHistory"] = ThermalHistory
    data["ToxicPercent"] = ToxicPercent
    data["SusceptibleTemper"] = SusceptibleTemper
    data["LOM"] = LOM
    data["ChemicalInjection"] = ChemicalInjection
    data["ContainsDeadlegs"] = ContainsDeadlegs
    data["ShakingAmount"] = ShakingAmount
    data["DFDI"] = DFDI
    data["VASD"] = VASD
    data["BrittleFacture"] = BrittleFacture
    data["CylicOper"] = CylicOper
    data["MaxBrinell"] = MaxBrinell
    data["minOT"] = minOT
    data["SulfurContent"] = SulfurContent
    return data
client = mqtt.Client()
client.connect("localhost",1883,60)
data = set_data(Chromium=False, materialExposedFluid=False, EnvironmentCost=0, Op3=0, RiskAnalystPeriod=36, 
    PressurisationControlled=False, MaterialHTHA=True, NorminalThickness=19.05, HTHAMaterialGrade="1Cr-0.5Mo", 
    CorrectiveAction="None", EquOper=False, CriticalTemp=80, 
    PipeCondition="Broken gussets or gussets welded directly to pipe", ThermalHistory="Solution Annealed", 
    EquipmentVolumn=100, Op4=0, tempRef=21, AminSolution="Diglycolamine DGA", ExternalCoatingDate="2018-09-26", 
    OpHydrogenPressure=10000, EnvCaustic=False, Op9=0, Op6=0, ExposureAmine="Low Lean Amine", MassInventory=12400, 
    DeltaFATT=0.5, minOT=20, CO3=0, PresenceCyanides=False, Op7=100, APIFluid="C1-C2", NumberPipeFittings="More than 10", 
    InternalCladding=True, DFDI=False, ExternalCoatingQuality="Please select coat quality..", HydrogenFluoric=False, 
    ToxicConstituents=True, H2SInWater=1000, NickelAlloy=False, Downtime=False, 
    OnlineMonitoring="Sour water low velocity corrosion - Electrical resistance probes", InsulationType='C', 
    MinReqThickness=16.68, SusceptibleTemper=False, AusteniticSteel=False, PreviousFailures="Greater than one", 
    allowStress=240, BranchDiameter="Any branch less than or equal to 2\" Nominal OD", MaxBrinell="Below 200", 
    CylicOper=True, PHWater=5, ExposedSulfur=False, AdminControlUpset=True, CladdingCorrosionRate=0.29, 
    ExternalInsulationType="Calcium Silicate", Op10=0, Op2=0, ChlorideIon=1000, PersonDensity=0.005, 
    SulphurContent="High > 0.01%", HeatTraced=False, complex="Above Average", InsulationCholride=True, 
    SteamedOut=False, EquipmentCost=2000, CurrentThickness=19.05, LOM=False, Op8=0, InternalCoating=True, 
    AqueShutdown=False, InjureCost=5000000, MFTF=False, MassComponent=24000, InternalLinerType="Acid Brick", 
    ReleasePercentToxic=1, Op1=0, BranchJointType=None, supportMaterial=True, AqueOp=False, BrittleFacture=1, 
    PWHT=False, ReleaseDuration="", ExternalEnvironment="Arid/dry", ContainsDeadlegs=False, Highly=True, maxOP=1000, 
    timeShakingPipe="13 to 52 weeks", ChemicalInjection=False, MitigationSystem="Fire water deluge system and monitors", 
    DetectionType='C', ShakingAmount="Moderate", heatTreatment="Normalised Temper", SigmaPhase=1, 
    InternalLinerCondition="Poor", MinDesignTemp=17, System="Vapor", minOP=200, NaOHConcentration=12, hydrogen=False, 
    CorrosionAllowance=3.17, PresenceCracks=False, VASD=True, PresenceofSulphides=False, MaterialPTA=True, PTAMaterialCode="321 Stainless Stee", maxOT=100, 
    CostFactor=1.2, exposureAcid=False, HFICI=False, InternalLining=True, Op5=0, ExternalCoating=False, 
    CylicLoad="Valve with high pressure drop", ProductionCost=50000, PresenceofSulphidesShutdown=False, EnvCH2S=False, 
    Material="plastic", MaxDesignTemp=1000, NorminalDiameter=97.62, ExternalInsulation=1, minTemp=45, 
    CurrentCorrosionRate=0.29, InsulationCondition="Above average", CarbonAlloySteel=False, InterfaceSoilWater=False, 
    ToxicPercent=0, TrampElements=False, DesignPressure=12000, SulfurContent=0)
send_data = json.dumps(data)
client.publish("7/propsaltest", send_data);
client.disconnect();
