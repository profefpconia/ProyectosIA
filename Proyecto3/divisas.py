import requests

def obtener_tasa_cambio(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "conversion_rates" in data:
            tasa_cambio = data["conversion_rates"].get(target_currency)
            if tasa_cambio:
                return tasa_cambio
            else:
                print(f"Moneda objetivo '{target_currency}' no encontrada.")
        else:
            print("Error en la respuesta de la API.")
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
    return None

def main():
    api_key = "94f33702cfb1d380f4bb7427"  # Reemplaza con tu clave de API de ExchangeRate-API
    base_currency = "USD"  # Moneda base
    target_currency = "EUR"  # Moneda objetivo

    print(f"Obteniendo tasa de cambio de {base_currency} a {target_currency}...")
    tasa_cambio = obtener_tasa_cambio(api_key, base_currency, target_currency)

    if tasa_cambio:
        print(f"1 {base_currency} = {tasa_cambio} {target_currency}")

if __name__ == "__main__":
    main()
