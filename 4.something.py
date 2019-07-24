# Calculate the velocity required to escape a circular orbit of Earth,
# depending on a user-entered orbital distance.
import math
escape_velocity_meters_per_sec = 0  # Required velocity to escape orbit
earth_grav_constant = 6.67384e-11   # Earth's gravitational constant
earth_mass_kilograms = 5.972e24      # Mass of the Earth
radius_meters = float(input('Enter distance from center of Earth:\n'))

if radius_meters < 160000:  # 160 km is minimal low-earth orbit
    escape_velocity_meters_per_sec = 0  # No escape possible!
    print('Houston, we have a problem')
else:
    standard_grav_param = earth_grav_constant * earth_mass_kilograms
    escape_velocity_meters_per_sec = math.sqrt(2*standard_grav_param / radius_meters)
    print('Thrust to %d m/s to escape these Earthly shackles.' % escape_velocity_meters_per_sec)
temperatures = {
    'Seattle': 56.5,
    'New York': 105,
    'Kansas City': 81.9,
    'Los Angeles': 76.5
}
if 'New York' in temperatures:
    if temperatures['New York'] > 90:
        print("The city is melting!")
    else:
        print("The temperature in New York is", temperatures['New York'])
else:
    print("The temperature in New York is unknown.")



