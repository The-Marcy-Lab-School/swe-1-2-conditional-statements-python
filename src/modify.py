def wildly_biased_review(location):
    if location == "NYC":
        print("THE GREATEST CITY IN THE WORLD")
        print("THE CITY THAT NEVER SLEEPS")
        print("WOW WHAT A CITY")
    else:
        print("Yea that place is cool I guess")


def get_weather_report(temperature):
    if temperature > 90:
        weather_report = "It's hot and gross out."
        print(weather_report)
        print("And that's your report!")
    elif temperature > 70:
        weather_report = "It's really nice!"
        print(weather_report)
        print("And that's your report!")
    elif temperature < 32:
        weather_report = "Wow, it's cold out."
        print(weather_report)
        print("And that's your report!")
