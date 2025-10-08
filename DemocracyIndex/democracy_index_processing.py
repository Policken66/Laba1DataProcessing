from pathlib import Path

import pandas as pd
from pandas import Series


def convert_csv2exel(csv_path: Path, excel_path: Path):
    df = pd.read_csv(csv_path)
    df.to_excel(excel_path)

def select_inform_about_russia(path: Path) -> Series:
    df = pd.read_excel(path)
    result = df[df.apply(lambda row: row.astype(str).str.contains('Russia').any(), axis=1)]
    return result

def save_in_file(path: Path, data: Series):
    data.to_excel(path)