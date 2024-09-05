from PIL import Image
f=Image.open('r.png','r')
color_ranges = {
    1: ([0, 180, 220], [60, 255, 255]),  # Approximate BGR range for Index 1
    2: ([0, 150, 200], [60, 220, 255]),  # Approximate BGR range for Index 2
    3: ([0, 120, 170], [60, 190, 255]),  # Approximate BGR range for Index 3
    4: ([0, 100, 150], [60, 160, 255]),  # Approximate BGR range for Index 4
    5: ([0, 80, 130], [60, 140, 255]),   # Approximate BGR range for Index 5
}
print(color_ranges[5])