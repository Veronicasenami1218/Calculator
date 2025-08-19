def modify_content(content):
    """
    Function to modify the content of the file.
    (Here we’ll just make the text uppercase as an example.)
    """
    return content.upper()


# Ask the user for the filename
filename = input("Enter the name of the file to read: ")

try:
    # Try opening the file for reading
    with open(filename, "r") as file:
        content = file.read()
    
    # Modify the content
    modified_content = modify_content(content)
    
    # Write the modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)
    
    print(f"Modified content has been written to '{new_filename}' ")

except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
