from tools import mytools
import time
print(
    ''' 
Hey Welcome to our simple tool!
  Here you can do the following things
  i)   Resize bunch of images all at a time!
  ii)  Generate thumbnails
  iii) Convert all your images to PNG
  Enter the following Options 
  Image Resizer: 1
  Thumbnail Generator: 2 
  PNG converter: 3
''')

choice = int(input('Enter you choice : '))
if choice == 1:
    user_input = input('Do you want to resize your images? Yes/No  : ')
    if user_input == 'Yes' or user_input == 'yes':
        t1 = time.time()
        mytools.bunch_resize()
        t2 = time.time()
        print('TimeTaken:', round((t2 - t1) / 60, 2), 'sec')
    else:
        print('Thank You for using our tool.')
elif choice == 2:
    user_input = input('Do you want to generate thumbnail? Yes/No  : ')
    if user_input == 'Yes' or user_input == 'yes':
        t1 = time.time()
        mytools.thumbnail_generator()
        t2 = time.time()
        print('TimeTaken:', round((t2 - t1) / 60, 2), 'sec')
    else:
        print('Thank You for using our tool.')
elif choice == 3:
    user_input = input('Do you convert all images to PNG? Yes/No  : ')
    if user_input == 'Yes' or user_input == 'yes':
        t1 = time.time()
        mytools.convert_to_png()
        t2 = time.time()
        print('TimeTaken:', round((t2 - t1) / 60, 2), 'sec')
    else:
        print('Thank You for using our tool.')

