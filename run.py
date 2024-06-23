def format_filename(filename):
    # Remove hyphens and capitalize each word
    words = filename.split('-')
    formatted_name = ' '.join(word.capitalize() for word in words)
    return formatted_name

# Open the file containing the list of filenames
with open('filenames.txt', 'r') as file_list:
    # Loop through each line in the file
    for filename in file_list:
        # Strip any surrounding whitespace or newline characters
        filename = filename.strip()
        # Format the filename for title and h1
        formatted_name = format_filename(filename)
        # Create an HTML file for each filename
        html_filename = f"{filename}.html"
        with open(html_filename, 'w') as html_file:
            html_file.write(f"<h1>{formatted_name}</h1>\n")
        print(f"Created {html_filename}")
