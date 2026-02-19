# MH second main word counter page
# import from other files

# menu function:
def main():
    # automatically sets last updated and word count to 0
    last_updated = "None"
    Word_count = "None"
    # asks user if they want to update file, view file, view doccument info, or exit
    while True:
        action = input("What do you want to do?\n1. Update doccument\n2. View doccument\n3. View doccument info\n4. Exit\nChoice (1-4): ")
        # if they want to update run the update function and save the last updated and word count
        if action == "1":
            pass
        # if they want to view the file run the view file function
        elif action == "2":
            pass
        # if they want to view the doccument info print whatever is saved as last updated and word count
        elif action == "3":
            pass
        elif action == "4":
            pass
        else:
            print("that is not an option.")
            continue