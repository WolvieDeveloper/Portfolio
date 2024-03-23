from stegano import lsb

# Path to the original image
image_path = "img.png"

# Message to hide in the image
message_to_hide = "This is a Secret message and you are the only one who knows this."

# Hide the message in the image
secret_image = lsb.hide(image_path, message_to_hide)

# Save the modified image
secret_image.save("secret_image.png")

# Extract the hidden message from the image
extracted_message = lsb.reveal("secret_image.png")

# Print the extracted message
print("Extracted Message:", extracted_message)
