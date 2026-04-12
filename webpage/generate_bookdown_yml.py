import os
import re

def extract_numeric_prefix(s):
    match = re.match(r'^(\d+)_', s)
    if not match:
        return (999, s)
    num_str = match.group(1)
    section = int(num_str[0])
    try:
        protocol_num = int(num_str[1:])
    except:
        protocol_num = 0
    return (section, protocol_num)

webpage_dir = "."
files = [f for f in os.listdir(webpage_dir) if f.endswith(".Rmd")]

# Standard headers
headers = {
    "005_intro.Rmd": "# (PART) General Information {-}",
    "100_site-characteristics.Rmd": "# (PART) Section 1: Site Characteristics and Data Management {-}",
    "200_carbon-and-nutrient-cycling.Rmd": "# (PART) Section 2: Carbon and Nutrient Cycling {-}",
    "300_water-cycling.Rmd": "# (PART) Section 3: Water Cycling {-}",
    "400_species-and-interactions.Rmd": "# (PART) Section 4: Species and Interactions {-}",
    "500_stress-physiology.Rmd": "# (PART) Section 5: Stress Physiology {-}",
    "600_blog-posts.Rmd": "# (PART) Blog {-}"
}

for filename, content in headers.items():
    if not os.path.exists(filename):
        with open(filename, 'w') as hf:
            hf.write(content + "\n")
        if filename not in files:
            files.append(filename)

# Sorting Function
def sort_key(f):
    if f == "index.Rmd": return (-1, 0)
    if f.startswith("01_") or f == "005_intro.Rmd":
        # Group info pages under General Info
        return (0, f)
    return extract_numeric_prefix(f)

all_sorted = sorted([f for f in files if f != "00_home.Rmd"], key=sort_key)

# Remove empty landing pages to reduce noise
to_remove = []
for rmd in all_sorted:
    if rmd in ["01_about-us.Rmd", "01_blog.Rmd"]:
        with open(rmd, 'r') as f:
            if len(f.read().strip().split('\n')) < 6:
                to_remove.append(rmd)

final_list = [f for f in all_sorted if f not in to_remove]

with open("_bookdown.yml", 'w') as f:
    f.write("delete_merged_file: true\n")
    f.write("new_session: true\n")
    f.write('book_filename: "ClimEx Handbook"\n')
    f.write("rmd_files:\n")
    for rmd in final_list:
        f.write(f'  - "{rmd}"\n')

print(f"Generated final _bookdown.yml with {len(final_list)} files.")
