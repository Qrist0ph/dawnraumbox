import os
#import json
#from cssbeautifier import beautify

def format_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Format the data and write back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    # Append a CRLF at the end of the file
    with open(file_path, 'ab') as f:
        f.write(b'\r\n')

def format_json_files_recursively(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                format_json_file(file_path)
            if file.endswith('.css'):
                file_path = os.path.join(root, file)
                format_css_file(file_path,file_path)





def convert_lf_to_crlf(file_path):
    with open(file_path, 'r', encoding='utf-8',newline='') as f:
        lines = f.readlines()
    
    with open(file_path, 'w', encoding='utf-8',newline='') as f:
        for line in lines:
            if not line.endswith('\r\n'):
                f.write(line.rstrip('\n') + '\r\n')
            else:
                f.write(line)

def convert_lf_to_crlf_recursively(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            #print(file_path)
            try:
                convert_lf_to_crlf(file_path)
            except:
                print("  no")


def format_css_file(input_path, output_path):
  
    print(input_path)
    with open(input_path, 'r') as input_file:
        css_code = input_file.read()

    formatted_css = beautify(css_code)
    
    with open(output_path, 'w') as output_file:
        output_file.write(formatted_css)


            

def get_line_ending(line):
    if '\r\n' in line:
        return "CRLF"
    elif '\r' in line:
        return "CR"
    elif '\n' in line:
        return "LF"
    else:
        return "Unknown"

def print_line_endings(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=1):
            line_ending = get_line_ending(line)
            print(f"Line {line_number}: {line_ending}")


def print_last_4_ascii_codes(line):
    last_4_characters = line[-4:]
    ascii_codes = [ord(char) for char in last_4_characters]
    print("Last 4 characters:", last_4_characters)
    print("ASCII codes:", ascii_codes)

def print_last_4_ascii_codes_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8',newline='') as f:
        for line_number, line in enumerate(f, start=1):
            #line = line.rstrip('\r\n')  # Remove line endings
            if len(line) >= 4:
                print(f"Line {line_number}:")
                print_last_4_ascii_codes(line)
                special_characters = [r"\r" if c == '\r' else r"\n" if c == '\n' else c for c in line[-4:]]
                print("Special Characters:", special_characters)
                print()

# Replace 'your_directory_path' with the actual directory path where your JSON files are located.
your_directory_path = '.'
#format_json_files_recursively(your_directory_path)
convert_lf_to_crlf_recursively(your_directory_path)
#convert_lf_to_crlf('./foo.py')
#print_last_4_ascii_codes_in_file('./foo.py')
