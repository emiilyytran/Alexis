import datetime
import requests

def get_zodiac_sign(month, day):
    # Zodiac date ranges
    zodiac_dates = [
        ((1, 20), (2, 18), 'Aquarius'),
        ((2, 19), (3, 20), 'Pisces'),
        ((3, 21), (4, 19), 'Aries'),
        ((4, 20), (5, 20), 'Taurus'),
        ((5, 21), (6, 20), 'Gemini'),
        ((6, 21), (7, 22), 'Cancer'),
        ((7, 23), (8, 22), 'Leo'),
        ((8, 23), (9, 22), 'Virgo'),
        ((9, 23), (10, 22), 'Libra'),
        ((10, 23), (11, 21), 'Scorpio'),
        ((11, 22), (12, 21), 'Sagittarius'),
        ((12, 22), (1, 19), 'Capricorn')
    ]
    
    # Check which zodiac sign the date falls into
    for start_date, end_date, sign in zodiac_dates:
        start_month, start_day = start_date
        end_month, end_day = end_date
        
        if ((month == start_month and day >= start_day) or (month == end_month and day <= end_day)):
            return sign

    return "Unknown Zodiac Sign"

def get_horoscope_from_api(zodiac_sign):
    # Horoscope API URL (for example, using Horoscope-API)
    params = (
        ('sign', zodiac_sign),
        ('day', 'today')
    )
    day = 'today'
    # url = f"https://aztro.sameerkumar.website?sign={zodiac_sign}&day=today"
    api_url = "https://aztro.sameerkumar.website/?sign="+zodiac_sign+"&day="+day
    
    # Make a POST request to the API
    response = requests.post(api_url)
    
    
    if response.status_code == 200:
        data = response.json()
        return data.get("description", "No horoscope available.")
    else:
        return "Unable to fetch horoscope from the API."

def run_horoscope():
    # Get user input for birthday
    birthday_input = input("Enter your birthday (YYYY-MM-DD): ")
    
    try:
        # Parse the input into a datetime object
        birthday = datetime.datetime.strptime(birthday_input, '%Y-%m-%d')
        
        # Get the zodiac sign based on the birthday
        zodiac_sign = get_zodiac_sign(birthday.month, birthday.day)
        
        # Fetch the horoscope from the API
        horoscope = get_horoscope_from_api(zodiac_sign)
        
        # Output the result
        print(f"Your zodiac sign is: {zodiac_sign}")
        print(f"Your horoscope: {horoscope}")
        
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

if __name__ == "__main__":
    run_horoscope()
