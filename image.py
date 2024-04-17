from PIL import Image, ImageDraw

height = 700
width = 800
image = Image.new(mode='L', size=(height, width), color=255)

draw = ImageDraw.Draw(image)
y_start = 0
y_end = image.height
step_size1 = int(image.width / 4)
step_size2 = int(image.height/6)

for x in range(0, image.width, step_size1):
    line = ((x, y_start), (x, y_end))
    draw.line(line, fill=128)

    x_start = 0
    x_end = image.width

for y in range(0, image.height, step_size2):
    line = ((x_start, y), (x_end, y))
    draw.line(line, fill=128)

image.show()
image.save('igrovoepole.jpg')