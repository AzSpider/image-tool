from PIL import Image
import os


# Resize all images function
def bunch_resize():
    while True:
        img_folder = input('Enter Your image folder Name: ')
        if not os.path.exists(img_folder):
            print(f'There is no folder named {img_folder}. Please retry... ')
        else:
            break
    output_folder = input('Create a new folder to save your resized image. Enter new folder name: ')
    width = int(input('Enter the width= '))
    height = int(input('Enter the height = '))
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    print('Processing...')
    for file_name in os.listdir(img_folder):
        img = Image.open(f'{img_folder}/{file_name}')
        get_ext = img.format
        ext = get_ext.lower()
        resized_image = img.resize((width, height))
        clean_name = os.path.splitext(file_name)[0]
        resized_image.save(f'{output_folder}/{clean_name}.{ext}', ext)
    print(f'Thank You. All your images has been resized. find All your images inside \'{output_folder}\'')


# Generate thumbnail function
def thumbnail_generator():
    while True:
        img_folder = input('Enter Your image folder Name: ')
        if not os.path.exists(img_folder):
            print(f'There is no folder named {img_folder}. Please retry... ')
        else:
            break
    output_folder = input('Create a new folder to save your thumbnail image. Enter new folder name: ')
    width = int(input('Enter the width= '))
    height = int(input('Enter the height = '))
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    print('Processing...')
    for file_name in os.listdir(img_folder):
        img = Image.open(f'{img_folder}/{file_name}')
        get_ext = img.format
        ext = get_ext.lower()
        img.thumbnail((width, height))
        clean_name = os.path.splitext(file_name)[0]
        img.save(f'{output_folder}/{clean_name}.{ext}', ext)
    print(f'Thank You. All your thumbnail is generated. Find All your images inside \'{output_folder}\'')


# PNG converter function
def convert_to_png():
    while True:
        img_folder = input('Enter Your image folder Name: ')
        if not os.path.exists(img_folder):
            print(f'There is no folder named {img_folder}. Please retry... ')
        else:
            break
    output_folder = input('Create a new folder to save your png images. Enter new folder name: ')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    print('Processing...')
    for file_name in os.listdir(img_folder):
        img = Image.open(f'{img_folder}/{file_name}')
        clean_name = os.path.splitext(file_name)[0]
        img.save(f'{output_folder}/{clean_name}.png', 'png')
    print(f'Thank You. All your images has been converted to png. find All your images inside \'{output_folder}\'')
