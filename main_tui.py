# Note for future me: Use streamlit  or flask  here
# Actually I'll do it later

import os
import shutil
from colorama import Back, Style, Fore
import api_input

# To get the width of terminal for appropriately sizing the heading
size = shutil.get_terminal_size()

size = int(size[0] - len(' J W S T  I M A G E  C O L O R I S E R '))
size = int(size / 2)
print(Fore.GREEN + '=' * size + ' J W S T  I M A G E  C O L O R I S E R ' + '=' * size)

# Blah Blah Blah
print(
    Fore.RESET + '\nNote:\n1.\tThe images are distributed into pages\n2.\tEach page has a variable number of images, '
                 'as there are thumb files\n3.\tThumb files are of low quality and hence are excluded\n4.\tThe '
                 'processed images are located under the ' + Fore.RED + 'result_images' + Fore.RESET + ' folder')

option = input(
    'For clearing the folders, type ' + Fore.RED + 'clr' + Fore.RESET + '. For generating images, type' + Fore.RED + ' gen: ' + Fore.RESET)

# To run the other python files. yes ik it is using the exec() statement, but i don't give a shit
if option == 'gen':
    print(Fore.BLUE + "\nIMPORTANT: THE FOLLOWING FIELDS MUST ALL BE INTEGER NUMBERS." + Fore.RESET + '\n')
    page = input('Which ' + Fore.RED + 'page' + Fore.RESET + ' page you need (starting from 1) ?')

    results = input('How many results do you need per page (incl. thumb files)? ')

    api_input.generate_json(page, results)
    try:
        exec(open('image_extractor.py').read())
        exec(open('downloader.py').read())
        exec(open('colorise_ai.py').read())
    except:
        print('There was some kind of error generated due to the code. This is not your fault, as the API data was '
              'successfully downloaded without error')

# Clearing directroies
elif option == 'clr':
    try:
        with os.scandir('raw_images') as entries:
            for entry in entries:
                if entry.is_file():
                    os.remove(entry.path)
        print("All files under \'raw_images\' deleted successfully.")
        with os.scandir('result_images') as entries:
            for entry in entries:
                if entry.is_file():
                    os.remove(entry.path)
        print("All files under \'result_images\' deleted successfully.")
        with os.scandir('raw') as entries:
            for entry in entries:
                if entry.is_file():
                    os.remove(entry.path)
        print("All files under \'raw\' deleted successfully.")
    except OSError:
        print("Error occurred while deleting files.")
