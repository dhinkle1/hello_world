from datetime import datetime
import pytz

def get_time_in_est():
    """
    Returns the current time in Eastern Standard Time (EST).
    """
    # Define the EST timezone
    est = pytz.timezone('America/New_York')

    # Get the current time in UTC and convert it to EST
    current_time_utc = datetime.utcnow()
    current_time_est = current_time_utc.astimezone(est)

    return current_time_est.strftime("%Y-%m-%d %H:%M:%S %Z")

if __name__ == "__main__":
    # If this script is executed, rather than imported as a module, run this code
    current_time = get_time_in_est()
    print("Current time in EST:", current_time)

