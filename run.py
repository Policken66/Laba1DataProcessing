from pathlib import Path

from FreedomHouse.freedom_house_processing import select_inform_about_russia, save_in_file

if __name__ == "__main__":
    print("Hello")
    input_path = Path("FreedomHouse/Resources/freedom_house.xlsx")
    data = select_inform_about_russia(input_path)
    output_path = Path("FreedomHouse/Output/freedom_house.xlsx")
    save_in_file(path=output_path, data=data)