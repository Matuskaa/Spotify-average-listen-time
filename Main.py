# Dobry den pane uciteli
while True :
    try: 
        minuty = input("Spotify minutes: ")
        minuty = int(minuty)

        result = minuty / 525600 * 24
        hodiny = int(result)
        minutes_left = round((result - hodiny) * 60)

        print(f"{hodiny} hours and {minutes_left} minutes or {round(result * 60)} minutes ")

    except ZeroDivisionError:
        print("nununutututu")
    except ValueError:
        print("nununutututu")
