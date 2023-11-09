
# https://github.com/timesler/facenet-pytorch

from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image, ImageDraw

# If required, create a face detection pipeline using MTCNN:
mtcnn = MTCNN(image_size=160, margin=0)

# Create an inception resnet (in eval mode):
resnet = InceptionResnetV1(pretrained='vggface2').eval()


img = Image.open('./images/test.jpg')

# Convert the image to RGB if it's not already in that mode
if img.mode != 'RGB':
    img = img.convert('RGB')

# Get cropped and prewhitened image tensor
boxes, _ = mtcnn.detect(img) #, save_path='./images/test_result.jpg'

# Create a copy of the original image to draw the boxes on
draw_img = img.copy()
draw = ImageDraw.Draw(draw_img)

# Define box color and thickness
box_color = 'green'
thickness = 1

# Draw the boxes
if boxes is not None:
    for box in boxes:
        draw.rectangle(box.tolist(), outline=box_color, width=thickness)

# Save or display the image
draw_img.save('./images/test_with_boxes.jpg')
draw_img.show()