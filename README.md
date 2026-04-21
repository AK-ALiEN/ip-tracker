# 🌐 IP Lookup Tool (CLI)

A simple Python-based command-line tool to fetch detailed information
about any IP address using an external API.

## 🚀 Features

-   🔍 Lookup any IPv4 address
-   🌍 Get location details (city, region, country)
-   📍 Latitude & Longitude with Google Maps link
-   🕒 Timezone and postal code info
-   🌐 ISP and ASN details
-   ✅ Input validation for IP addresses
-   💻 Clean CLI interface with banner

## 📂 Project Structure

    .
    ├── main.py
    ├── requirements.txt
    └── README.md

## ⚙️ Installation

``` bash
git clone https://github.com/AK-ALiEN/ip-tracker.git
cd ip-lookup-tool
pip install -r requirements.txt
```

## ▶️ Usage

``` bash
python main.py
```

Enter an IP address:

    Enter Target IP (or 'q' to quit): 8.8.8.8

## 📸 Example Output

    ==================================================
    IP Address   : 8.8.8.8
    City         : Mountain View
    Region       : California
    Country      : United States
    Latitude     : 37.386
    Longitude    : -122.0838
    Time Zone    : America/Los_Angeles
    Postal Code  : 94035
    ISP          : Google LLC
    ASN          : AS15169
    Country Code : US
    Google Maps  : https://www.google.com/maps?q=37.386,-122.0838
    ==================================================

## 🧠 How It Works

-   Sends a POST request to an IP lookup API
-   Parses JSON response
-   Displays formatted results in terminal

## 🛡️ Error Handling

Handles: - Timeout errors - Connection issues - Invalid responses -
Incorrect IP formats

## 📌 Requirements

-   Python 3.x
-   Internet connection

## ⚠️ Disclaimer

This tool is for educational and informational purposes only.

## ⭐ Contribute

Feel free to fork the repo and submit pull requests!
