
import openpyxl
import csv
from pathlib import Path

# ----------------------------------
# 1. Load Excel workbook
# ----------------------------------

excel_file = Path(__file__).parent / "Aerofoil+data (Turbine).xlsx"
sheet = openpyxl.load_workbook(excel_file)

workbook = openpyxl.load_workbook(excel_file, data_only=True)

sheet = workbook["Aerofoil table-With Z"]


# ----------------------------------
# 2. Define sections and Z values
# ----------------------------------

sections = {
    "I-I":     {"z": 27.5, "ycc_col": 5, "ycv_col": 2},
    "II-II":   {"z": 41.65, "ycc_col": 11, "ycv_col": 8},
    "III-III": {"z": 55.2, "ycc_col": 17, "ycv_col": 14},
    "IV-IV":   {"z": 68.15, "ycc_col": 23, "ycv_col": 20},
    "V-V":     {"z": 80.5, "ycc_col": 29, "ycv_col": 26}
}

# ----------------------------------
# 3. Create output folder
# ----------------------------------

output_folder = Path(__file__).parent / "Aerofoil_DAT_Files"
output_folder.mkdir(exist_ok=True)

# ----------------------------------
# 4. Generate the 10 DAT files
# ----------------------------------

for section, details in sections.items():

    z_value = details["z"]

    datasets = {
        "CC": details["ycc_col"],
        "CV": details["ycv_col"]
    }

    for surface, y_col in datasets.items():

        filename = f"Section_{section}_{surface}.dat"
        output_path = output_folder / filename

        valid_rows = []
        deleted_rows = 0

        for row in range(4, sheet.max_row + 1):

            x_value = sheet.cell(row=row, column=1).value

            if x_value is None:
                break

            y_value = sheet.cell(row=row, column=y_col).value

            # Remove rows containing '-' or empty Y values
            if y_value is None or str(y_value).strip() == "-":
                deleted_rows += 1
                continue

            valid_rows.append([x_value, y_value, z_value])

        # Write numerical data only (NO COLUMN HEADERS)
        with open(output_path, "w", newline="") as file:

            writer = csv.writer(
                file,
                delimiter="\t",
                lineterminator="\n"
            )

            writer.writerows(valid_rows)

        print(
            f"Created: {filename} | "
            f"Valid points: {len(valid_rows)} | "
            f"Deleted rows: {deleted_rows}"
        )

# ----------------------------------
# 5. Completion message
# ----------------------------------

print("\nAll 10 DAT files generated successfully!")
print(f"Output location: {output_folder}")
