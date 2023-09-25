import datetime

# Function to calculate tire volume
def calculate_tire_volume(width, aspect_ratio, diameter):
    volume = 3.14159 * width * aspect_ratio * diameter
    return volume

# Get input from the user for tire dimensions
width = float(input("Enter the width of the tire (in mm): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel (in inches): "))

# Calculate the tire volume
volume = calculate_tire_volume(width, aspect_ratio, diameter)

# Get the current date and time
current_date = datetime.datetime.now().strftime("%Y-%m-%d")

# Display the calculated tire volume with two decimal places
print(f"The volume of space inside the tire is {volume:.2f} cubic mm.")

# Append data to the 'volumes.txt' file
with open('volumes.txt', 'a') as file:
    line = f"{current_date}, {width:.2f}, {aspect_ratio:.2f}, {diameter:.2f}, {volume:.2f}\n"
    file.write(line)

# Print a message indicating data has been saved to the file
print("Data has been saved to 'volumes.txt'.")

