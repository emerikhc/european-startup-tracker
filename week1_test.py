# week1_test.py - Prototype Data Model for European Startups

# 1. A list of dictionaries representing under-the-radar European startups
early_stage_startups = [
    {
        "name": "Kite Mobility",
        "hub": "Munich",
        "open_source_stars": 1250,
        "hiring_velocity": 4,  # Net new roles this month
        "spinoff": True
    },
    {
        "name": "Argus Bio",
        "hub": "Cambridge",
        "open_source_stars": 340,
        "hiring_velocity": 2,
        "spinoff": True
    },
    {
        "name": "LayerPulse",
        "hub": "Paris",
        "open_source_stars": 4800,
        "hiring_velocity": 8,
        "spinoff": False
    }
]

print("=== EUROPEAN STARTUP TRACKER: WEEK 1 PROTOTYPE ===\n")

# 2. Loop through the list to parse and display signals
for startup in early_stage_startups:
    name = startup["name"]
    hub = startup["hub"]
    stars = startup["open_source_stars"]
    velocity = startup["hiring_velocity"]
    is_spinoff = "Yes (University/Lab)" if startup["spinoff"] else "No"

    # Formatted string output (f-strings)
    summary = (
        f"Company: {name} | Hub: {hub}\n"
        f" -> GitHub Stars: {stars} | Hiring Velocity: +{velocity} roles/mo\n"
        f" -> Academic Spinoff: {is_spinoff}\n"
        f" --------------------------------------------------"
    )
    print(summary)