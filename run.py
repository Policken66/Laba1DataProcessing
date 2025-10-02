from pathlib import Path

from DemocracyIndex import democracy_index_processing
from FreedomHouse import freedom_house_processing

if __name__ == "__main__":
    input_path = Path("FreedomHouse/Resources/freedom_house.xlsx")
    data = freedom_house_processing.select_inform_about_russia(input_path)
    output_path = Path("FreedomHouse/Output/freedom_house.xlsx")
    freedom_house_processing.save_in_file(path=output_path, data=data)

    csv_path_EIU_DI = Path("DemocracyIndex/Resources/EIU_DI.csv")
    csv_path_EIU_DI_DATADICT = Path("DemocracyIndex/Resources/EIU_DI_DATADICT.csv")
    csv_path_EIU_DI_WIDEF = Path("DemocracyIndex/Resources/EIU_DI_WIDEF.csv")

    exel_path_EIU_DI = Path("DemocracyIndex/Output/EIU_DI.xlsx")
    exel_path_EIU_DI_DATADICT = Path("DemocracyIndex/Output/EIU_DI_DATADICT.xlsx")
    exel_path_EIU_DI_WIDEF = Path("DemocracyIndex/Output/EIU_DI_WIDEF.xlsx")

    democracy_index_processing.convert_csv2exel(csv_path_EIU_DI, exel_path_EIU_DI)
    democracy_index_processing.convert_csv2exel(csv_path_EIU_DI_DATADICT, exel_path_EIU_DI_DATADICT)
    democracy_index_processing.convert_csv2exel(csv_path_EIU_DI_WIDEF, exel_path_EIU_DI_WIDEF)