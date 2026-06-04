# # class A:
# #     def __init__(self,name):
# #         self.name = name
        
# #     def skill(self):
# #         print("Skill 1")

# # class B:
# #     def __init__(self,name):
# #         self.name = name
        
# #     def skill(self):
# #         print("Skill 2")

# # class C(A, B):
# #     def skills(self):
# #         print("Skill 3")

# # c = C("John")
# # c.skills()
# # c.skill()
# # print(c.name)





# # class Chemical_treatment:
# #     def preservative_articraft(self):
# #         print("Preservative artificer using chemical treatment")

# # class Climate_control:
# #     def preservative_articraft(self):
# #         print("Preservative artificer using climate control")

# # class MuseumPreservation(Chemical_treatment, Climate_control):
# #     def preservation(self):
# #         Chemical_treatment.preservative_articraft(self)
# #         Climate_control.preservative_articraft(self)

# # m = MuseumPreservation()
# # m.preservation()


# # # cooperative super call

# # class A:
# #     def method(self):
# #         print("A")

# # class B:
# #     def method(self):
# #         print("B")

# # class C(A, B):
# #     def method(self):
# #         print("C")
# #         super().method() #i want to print both a and b

# # c = C()
# # c.method()



# # 1.	Dr. Meera is preserving a 2,000-year-old artifact. She uses ChemicalTreatment and ClimateControl methods. Both classes define preserve_artifact(). She creates a MuseumPreservation class that inherits from both.
# # Question: How can she ensure both treatments are applied when she calls preserve_artifact()?
# # Hint: Think about cooperative super() calls so each parent’s method contributes to the final preservation score.
# class ChemicalTreatment:
#     def preserve_artifact(self):
#         print("Preserving artifact using chemical treatment")

# class ClimateControl:
#     def preserve_artifact(self):
#         print("Preserving artifact using climate control")

# class MuseumPreservation(ChemicalTreatment, ClimateControl):
#     def preserve_artifact(self):
#         ChemicalTreatment.preserve_artifact(self)
#         ClimateControl.preserve_artifact(self)

# m = MuseumPreservation()
# m.preserve_artifact()

# print('=============================================================================================')

# # 2.	A new telescope needs calibration. The Optics class adjusts lenses, while the Sensor class adjusts sensitivity. Both have calibrate(). The SpaceTelescope class inherits from both.
# # Question: How can the telescope combine both adjustments when calibrate() is called?
# # Hint: Use super() in each parent so the final calibration factor is the sum of both.
# class Optics:
#     def calibrate(self):
#         print("Calibrating lenses")

# class Sensor:
#     def calibrate(self):
#         print("Calibrating sensitivity")

# class SpaceTelescope(Optics, Sensor):
#     def calibrate(self):
#         Optics.calibrate(self)
#         Sensor.calibrate(self)

# s = SpaceTelescope()
# s.calibrate()

# print('=============================================================================================')
# # 3.	Ravi wants to check his farm’s soil. He has a NutrientCheck class and a MoistureCheck class, both with analyze_soil(). He builds a SoilReport class that inherits from both.
# # Question: How can he make sure both checks contribute to the soil quality score?
# # Hint: Cooperative inheritance with super() ensures no check is skipped.
# class NutrientCheck:
#     def analyze_soil(self):
#         print("Analyzing soil nutrients")

# class MoistureCheck:
#     def analyze_soil(self):
#         print("Analyzing soil moisture")

# class SoilReport(NutrientCheck, MoistureCheck):
#     def analyze_soil(self):
#         NutrientCheck.analyze_soil(self)
#         MoistureCheck.analyze_soil(self)

# s = SoilReport()
# s.analyze_soil()

# print('=============================================================================================')
# # 4.	An AI weather system uses two models: TemperatureModel and WindModel. Both define predict_weather(). The ForecastSystem class inherits from both.
# # Question: How can the system combine predictions into one final forecast?
# # Hint: Use super() so the final prediction is the average of both models.
# class TemperatureModel:
#     def predict_weather(self):
#         return 76

# class WindModel:
#     def predict_weather(self):
#         return 27

# class ForecastSystem(TemperatureModel, WindModel):
#     def predict_weather(self):
#         temp = TemperatureModel.predict_weather(self)
#         wind = WindModel.predict_weather(self)
#         print(f"Final forecast: {(temp + wind)/2} %")

# f = ForecastSystem()
# f.predict_weather()

# print('=============================================================================================')
# # 5.	In a therapy session, a healer uses an Instrument and a FrequencyGenerator. Both define play_sound(). The HealingSession class inherits from both.
# # Question: How can the healer ensure both natural and generated sounds are played together?
# # Hint: Cooperative super() calls can merge sound outputs.
# class Instrument:
#     def play_sound(self):
#         print("Playing natural sound")

# class FrequencyGenerator:
#     def play_sound(self):
#         print("Playing generated sound")

# class HealingSession(Instrument, FrequencyGenerator):
#     def play_sound(self):
#         Instrument.play_sound(self)
#         FrequencyGenerator.play_sound(self)

# h = HealingSession()
# h.play_sound()

# print('=============================================================================================')
# # 6.	A conservationist uses a GPSDevice and a DroneCamera to track animals. Both define track_animal(). The SmartTracker class inherits from both.
# # Question: How can she ensure both GPS and camera data are collected?
# # Hint: Use super() so both tracking methods run sequentially.
# class GPSDevice:
#     def track_animal(self):
#         print("Tracking animal using GPS")

# class DroneCamera:
#     def track_animal(self):
#         print("Tracking animal using drone camera")

# class SmartTracker(GPSDevice, DroneCamera):
#     def track_animal(self):
#         GPSDevice.track_animal(self)
#         DroneCamera.track_animal(self)

# s = SmartTracker()
# s.track_animal()

# print('=============================================================================================')
# # 7.	A marine biologist measures coral health using a ChemicalSensor and a LightSensor. Both define measure_coral_health(). The CoralLab class inherits from both.
# # Question: How can she combine both sensor readings into one coral health index?
# # Hint: Cooperative super() calls can add both scores.

# class ChemicalSensor:
#     def measure_coral_health(self):
#         print("Measuring coral health using chemical sensor")

# class LightSensor:
#     def measure_coral_health(self):
#         print("Measuring coral health using light sensor")

# class CoralLab(ChemicalSensor, LightSensor):
#     def measure_coral_health(self):
#         ChemicalSensor.measure_coral_health(self)
#         LightSensor.measure_coral_health(self)

# c = CoralLab()
# c.measure_coral_health()

# print('=============================================================================================')
# # 8.	A coach evaluates players using SpeedAnalysis and StaminaAnalysis, both with evaluate_player(). The PerformanceReport class inherits from both.
# # Question: How can the coach generate a weighted performance score?
# # Hint: Use super() so both metrics contribute to the final evaluation.

# class SpeedAnalysis:
#     def evaluate_player(self):
#         print("Evaluating player using speed analysis")

# class StaminaAnalysis:
#     def evaluate_player(self):
#         print("Evaluating player using stamina analysis")

# class PerformanceReport(SpeedAnalysis, StaminaAnalysis):
#     def evaluate_player(self):
#         SpeedAnalysis.evaluate_player(self)
#         StaminaAnalysis.evaluate_player(self)

# p = PerformanceReport()
# p.evaluate_player()

# print('=============================================================================================')
# # 9.	A food scientist evaluates recipes using TasteTest and NutritionCheck, both with evaluate_recipe(). The FinalRecipe class inherits from both.
# # Question: How can she combine taste and nutrition scores?
# # Hint: Cooperative inheritance ensures both evaluations are included.

# class TasteTest:
#     def evaluate_recipe(self):
#         print("Evaluating recipe using taste test")

# class NutritionCheck:
#     def evaluate_recipe(self):
#         print("Evaluating recipe using nutrition check")

# class FinalRecipe(TasteTest, NutritionCheck):
#     def evaluate_recipe(self):
#         TasteTest.evaluate_recipe(self)
#         NutritionCheck.evaluate_recipe(self)

# f = FinalRecipe()
# f.evaluate_recipe()

# print('=============================================================================================')
# # 10.	A robot must plan its path using ObstacleDetection and EnergyOptimizer, both with plan_path(). The SmartRobot class inherits from both.
# # Question: How can the robot ensure both constraints are applied to its path length?
# # Hint: Use super() so the final path considers obstacles and energy efficiency.

# class ObstacleDetection:
#     def plan_path(self):
#         print("Planning path considering obstacles")

# class EnergyOptimizer:
#     def plan_path(self):
#         print("Planning path considering energy efficiency")

# class SmartRobot(ObstacleDetection, EnergyOptimizer):
#     def plan_path(self):
#         ObstacleDetection.plan_path(self)
#         EnergyOptimizer.plan_path(self)

# s = SmartRobot()
# s.plan_path()


