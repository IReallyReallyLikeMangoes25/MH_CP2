# MH second main word counter page

# import from other files
from word_counter_mangement import *
from word_counter_time import *

last_updated = "Not yet updated."
word_count = 0

# menu function:
def main(updated, words):
    print("Welcome to Mirai's word counter program. In this program you have a file you may edit, view, or check the information of.")
    # automatically sets last updated and word count to 0
    # asks user if they want to update file, view file, view doccument info, or exit
    while True:
            action = input("\nWhat do you want to do?\n1. Update doccument\n2. View doccument\n3. View doccument info\n4. Exit\nChoice (1-4): ")
            # if they want to update run the update function and save the last updated and word count
            if action == "1":
                updated, words = update_file(words)
            # if they want to view the file run the view file function
            elif action == "2":
                view_file(word_count)
            # if they want to view the doccument info print whatever is saved as last updated and word count
            elif action == "3":
                print(f"\nLast updated : {updated}\nWord Count : {words}")
            elif action == "4":
                break
            else:
                print("\nthat is not an option.\n")
                continue

main(last_updated, word_count)