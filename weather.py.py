import requests

def get_weather():
    # Get user input and format it
    country = input("Digite o país (Ex.: Brasil): ").strip().title()
    state = input("Digite o estado (Ex.: PE): ").strip().upper()
    city = input("Digite a cidade (Ex.: Recife): ").strip().title()

    # Combine location into a single string
    full_location = f"{city}, {state}, {country}"

    # Format the location for the URL (replace spaces with '+')
    city_url = full_location.replace(" ", "+")

    # Construct the URL for wttr.in
    url = f"https://wttr.in/{city_url}?format=3"

    try:
        # Make the HTTP request
        response = requests.get(url)
        if response.status_code == 200:
            result = response.text
            # Check if the location was not found
            if "Unknown location" in result or "Sorry" in result:
                print("\nLocalização não encontrada. Verifique seu input e digite novamente.") 
            else:
                print("\nClima atual:") 
                print(result.replace("+", " "))
        else:
            print(f"\nErro ao buscar clima. HTTP status code: {response.status_code}") 
    except requests.exceptions.RequestException as e:
        # Handle any network-related errors
        print(f"\nErro de Conexão: {e}") 

# Run the function
get_weather()