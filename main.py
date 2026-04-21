import requests
import json
import os
import sys

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    logo = """
▄▄ ▄▄▄▄    ▄▄▄▄▄▄ ▄▄▄   ▄▄▄▄ ▄▄ ▄▄ 
██ ██▄█▀     ██  ██▀██ ██▀▀▀ ██▄█▀ 
██ ██        ██  ██▀██ ▀████ ██ ██ 
    """
    credit = "Author: Alien\nGithub: AK-ALiEN\nTelegram: ak_xlien\nCommunity: t.me/AlienDevLab\n\n"
    
    print(logo)
    print(credit)

def look(ip):
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://ip8.com',
        'referer': 'https://ip8.com/',
        'sec-ch-ua': '"Microsoft Edge";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0',
    }

    json_data = {
        'ip': [
            ip,
        ],
    }

    try:
        resp = requests.post('https://api2.ip8.com/ip/info', headers=headers, json=json_data, timeout=10)
        resp.raise_for_status()
        
        data = resp.json()

        ip_address = data["ip"][0]
        ip_info = data["data"][ip_address]

        city = ip_info["geoip"]["city"]
        region = ip_info["geoip"]["region"]
        country = ip_info["geoip"]["country"]
        latitude = ip_info["geoip"]["latitude"]
        longitude = ip_info["geoip"]["longitude"]
        timezone = ip_info["geoip"]["timezone"]
        postal_code = ip_info["geoip"]["postalcode"]
        isp = ip_info["isp"]["isp"]
        asn = ip_info["isp"]["autonomousSystemNumber"]
        country_code = ip_info["geoip"]["isocode"]

        google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"

        print("\n" + "="*50)
        print(f"IP Address   : {ip}")
        print(f"City         : {city}")
        print(f"Region       : {region}")
        print(f"Country      : {country}")
        print(f"Latitude     : {latitude}")
        print(f"Longitude    : {longitude}")
        print(f"Time Zone    : {timezone}")
        print(f"Postal Code  : {postal_code}")
        print(f"ISP          : {isp}")
        print(f"ASN          : {asn}")
        print(f"Country Code : {country_code}")
        print(f"Google Maps  : {google_maps_url}")
        print("="*50)

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please check your connection and try again.")
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to the API. Please check your internet connection.")
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error occurred - {e}")
    except json.JSONDecodeError:
        print("Error: Failed to parse API response. The API might be down or returned invalid data.")
    except KeyError as e:
        print(f"Error: Missing expected data field - {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")

def validate_ip(ip):
    """Simple IP validation"""
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False

def main():
    while True:
        clear_screen()
        banner()
        
        ip = input("Enter Target IP (or 'q' to quit): ").strip()
        
        if ip.lower() == 'q':
            print("\nGoodbye!")
            sys.exit(0)
        
        if not ip:
            print("Please enter an IP address!")
            input("\nPress Enter to continue...")
            continue
        
        if not validate_ip(ip):
            print("Invalid IP address format! Please enter a valid IP (e.g., 8.8.8.8)")
            input("\nPress Enter to continue...")
            continue
        
        look(ip)
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExited by user. Goodbye!")
        sys.exit(0)