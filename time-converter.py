from datetime import datetime

def convert_to_24_hour(hour, minute, period):
    # Create a datetime object with the given time
    dt = datetime.strptime(f"{hour}:{minute} {period}", "%I:%M %p")

    # Format the result as a four-digit string
    result = dt.strftime("%H%M")

    return result

# Test cases
print(convert_to_24_hour(9, 30, "am"))  # Output: "0930"
print(convert_to_24_hour(9, 30, "pm"))  # Output: "2130"
