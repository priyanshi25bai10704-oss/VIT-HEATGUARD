# VitHeatGuard - Daily Hydration & Heat Reminder Tracker for Bhopal
print("🌡️ VitHeatGuard - Bhopal Heat & Hydration Tracker")
print("=" * 50)
print("Helps prevent dehydration, weakness and heat exhaustion\n")

try:
    temp = float(input("Enter current temperature in °C (e.g. 38): "))
    age = int(input("Enter your age: "))
    activity = input("Activity level (resting/light/moderate/heavy): ").lower().strip()
    weight = float(input("Enter approx weight in kg (or 60): ") or 60)
except:
    temp, age, activity, weight = 38, 25, "light", 60

base_water = weight * 0.033

if temp >= 40:
    base_water += 1.2
elif temp >= 35:
    base_water += 0.8
elif temp >= 30:
    base_water += 0.4

if activity == "heavy":
    base_water += 0.8
elif activity == "moderate":
    base_water += 0.5
elif activity == "light":
    base_water += 0.2

if age > 60 or age < 12:
    base_water += 0.4

recommended = round(base_water, 1)

print(f"\n✅ Recommended daily water: {recommended} liters")

print("\n🛡️ Reminders:")
print("• Drink every 1-2 hours")
print("• Carry water bottle")
print("• Use lemon/ORS if sweating")

print("\n⚠️ Watch for dehydration/weakness:")
print("• Weakness or fatigue")
print("• Dry mouth, dizziness, less urine")

drank = float(input("\nHow many liters have you drunk today? "))
remaining = max(0, recommended - drank)
print(f"You still need \~{remaining} liters today. Stay hydrated in Bhopal heat! 💧")
