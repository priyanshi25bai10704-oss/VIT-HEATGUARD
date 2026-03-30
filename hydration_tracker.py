# VIT-HEATGUARD - Daily Hydration & Heat Reminder Tracker
# BYOP Project for VITyarthi - Helps prevent dehydration and weakness in Bhopal heat

print("🌡️ VIT-HEATGUARD - Bhopal Heat & Hydration Tracker")
print("=" * 55)
print("Prevents dehydration, weakness, fatigue and heat exhaustion\n")

# Get user input safely
try:
    temp = float(input("Enter current temperature in °C (e.g. 38): "))
    age = int(input("Enter your age: "))
    activity = input("Activity level (resting / light / moderate / heavy): ").lower().strip()
    weight = float(input("Enter your approx weight in kg (or 60 if unsure): ") or 60)
except:
    print("Using default values for demo.")
    temp = 38
    age = 25
    activity = "light"
    weight = 60

# Calculate recommended water (simple real-world formula)
base_water = weight * 0.033  # 33 ml per kg body weight

# Extra water for Bhopal's extreme heat
if temp >= 40:
    base_water += 1.2
elif temp >= 35:
    base_water += 0.8
elif temp >= 30:
    base_water += 0.4

# Extra for activity level
if activity == "heavy":
    base_water += 0.8
elif activity == "moderate":
    base_water += 0.5
elif activity == "light":
    base_water += 0.2

# Extra care for children and elderly
if age > 60 or age < 12:
    base_water += 0.4

recommended = round(base_water, 1)

print(f"\n✅ Your recommended daily water intake today: {recommended} liters")

print("\n🛡️ Important Reminders:")
print("• Drink a glass of water every 1-2 hours (even if not thirsty)")
print("• Always carry a water bottle when going outside")
print("• Add lemon, ORS or buttermilk if you are sweating a lot")

print("\n⚠️ Early Warning Signs of Dehydration & Weakness:")
print("• Feeling weak or tired")
print("• Dry mouth, extreme thirst or dizziness")
print("• Headache or reduced urine")
print("→ If you notice any of these, drink water immediately and rest in shade!")

# Simple daily log
print("\n📝 Today's Water Log")
drank = float(input("How many liters of water have you drunk today so far? "))
remaining = max(0, recommended - drank)

print(f"\nYou have drunk {drank} liters today.")
print(f"You still need approximately {remaining} liters.")

if remaining > 2:
    print("🚨 You are behind — please start drinking more water now!")
elif remaining > 0.5:
    print("Good progress! Keep sipping regularly.")
else:
    print("Excellent! You are well hydrated today.")

print("\nStay safe and hydrated in Bhopal's heat! 💧🌡️")
