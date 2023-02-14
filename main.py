from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile

window = tk.Tk()

# Set up global variables
image = None
image_tk = None
label = tk.Label(window)
text_entry = None
color_entry = None
size_entry = None
angle_scale = None
x_scale = None
y_scale = None

def open_image():
    global image, image_tk, label, x_scale, y_scale

    # Open the image file using a file dialog
    file = askopenfile(mode='rb', filetypes=[('Image Files', '*.jpg *.jpeg *.png *.bmp')])

    if file is not None:
        # Open the image using Pillow
        image = Image.open(file)
        image = image.convert('RGBA')
        # Resize the image to fit the label
        image.thumbnail((400, 300))

        # Convert the image to a Tkinter-compatible format
        image_tk = ImageTk.PhotoImage(image)

        # Update the label with the new image
        label.configure(image=image_tk)
        label.image = image_tk

        # Update the x and y scales with the new image size
        x_scale.configure(to=image.width)
        y_scale.configure(to=image.height)
        x_scale.set(0)
        y_scale.set(0)

def add_text():
    global image, image_tk, label

    # Get the text, font, color, size, and x, y locations, and angle from the user
    text = text_entry.get()
    color = color_entry.get()
    size = 20
    x_location = x_scale.get()
    y_location = y_scale.get()
    angle = angle_scale.get()

    # Draw the text on the image
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", size)
    text_width, text_height = draw.textsize(text, font=font)
    text_image = Image.new('RGBA', (text_width, text_height), (255, 255, 255, 0))
    text_draw = ImageDraw.Draw(text_image)
    text_draw.text((0, 0), text, font=font, fill=color)

    rotated_text = text_image.rotate(angle, expand=True)

    text_x = x_location - rotated_text.size[0] / 2
    text_y = y_location - rotated_text.size[1] / 2

    image.alpha_composite(rotated_text, (int(text_x), int(text_y)))

    # Convert the image to a Tkinter-compatible format
    image_tk = ImageTk.PhotoImage(image)

    # Update the label with the new image
    label.configure(image=image_tk)
    label.image = image_tk
def save_image():
    # Open a file dialog to select the save location and file format
    file = asksaveasfile(mode='wb', defaultextension='.png', filetypes=[('PNG', '*.png'), ('JPEG', '*.jpg'), ('BMP', '*.bmp')])

    if file is not None:
        # Save the image to the selected file
        image.save(file)
# Create a browse button to open an image


browse_button = tk.Button(window, text="Open Image", command=open_image,bg="#AA5656")
browse_button.pack()

# Create a Scale widget for the X location of the text
x_scale_label = tk.Label(window, text="X Location:",bg="#F8EAD8")
x_scale_label.pack()
x_scale = tk.Scale(window, from_=0, to=500, orient=tk.HORIZONTAL,bg="#AA5656")
x_scale.pack()

# Create a Scale widget for the Y location of the text
y_scale_label = tk.Label(window, text="Y Location:",bg="#F8EAD8")
y_scale_label.pack()
y_scale = tk.Scale(window, from_=0, to=500, orient=tk.HORIZONTAL,bg="#AA5656")
y_scale.pack()

# Create a Scale widget for the angle of the text
angle_label = tk.Label(window, text="Angle:",bg="#F8EAD8")
angle_label.pack()
angle_scale = tk.Scale(window, from_=-90, to=90, orient=tk.HORIZONTAL,bg="#AA5656")
angle_scale.pack()

# Create a browse button to open an image
# Create an entry widget for the text to add
text_label = tk.Label(window, text="Text:",bg="#F8EAD8")
text_label.pack()
text_entry = tk.Entry(window)
text_entry.pack()

# Create an entry widget for the text color
color_label = tk.Label(window, text="Color:",bg="#F8EAD8")
color_label.pack()
color_entry = tk.Entry(window)
color_entry.pack()

# Create an entry widget for the font size
size_label = tk.Label(window, text="Size:",bg="#F8EAD8")
size_label.pack()
size_entry = tk.Entry(window)
size_entry.pack()

# Create a button to add the text to the image
add_button = tk.Button(window, text="Add Text", command=add_text,bg="#B99B6B")
add_button.pack()

# Create a button to save the image
save_button = tk.Button(window, text="Save Image", command=save_image,bg="#698269")
save_button.pack()

# Create a label to display the image
label = tk.Label(window,bg="#F8EAD8")
label.pack()

# Run the window loop
window.geometry("380x635")
window.config(bg="#F8EAD8")
window.mainloop()

