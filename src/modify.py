def send_message(username, recipient, message):
    if username:
        if recipient:
            if message:
                if len(message) <= 280:
                    return f"{username} -> {recipient}: {message}"
                else:
                    return "Message is too long."
            else:
                return "Message cannot be empty."
        else:
            return "Choose someone to message."
    else:
        return "You must be logged in."


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
