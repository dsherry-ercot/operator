from pathlib import Path
import shutil
import time
from functools import wraps

kml_readme = r"Q:\Posting Data\Auction Models Posted to MIS\KML_Readme.txt"


def timeit(func):
    @wraps(func)
    def measure_time(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} function took {end_time - start_time:.3f} seconds.")
        return result
    return measure_time


def rename_parent_folders(destination, auction):
    """renaming parent folders for LTAS auctions. Not needed for Monthly Auctions"""
    for parent_folder in Path(destination).iterdir():
        child_folder = parent_folder.stem  # 01 JAN 2027
        if (
            auction not in child_folder
        ):  # ensures rerunning the automation doesn't mess up changed names
            if len(child_folder.split()) == 3:
                month = list(child_folder.split())[1]
                parent_folder.replace(
                    parent_folder.with_stem(f"{auction}.{month}"))

            if "outages" in child_folder.lower():
                parent_folder.replace(
                    parent_folder.with_stem(f"{auction}.{child_folder}")
                )

            if "mapping" in child_folder.lower():
                parent_folder.replace(
                    parent_folder.with_stem(f"{auction}.Mapping_Documents")
                )

            if child_folder == "KML":
                parent_folder.replace(
                    parent_folder.with_stem(f"{auction}.Oneline_Diagrams")
                )

            if "station_onelines" in child_folder.lower():
                parent_folder.replace(
                    parent_folder.with_stem(f"{auction}.Station_OneLines")
                )


def rename_outage_files(destination, auction):
    """Renames files inside of 'Outages' folder"""
    outage_folder = destination.glob("*Outages").__next__()
    seqs_outage_is_none = ["seq4", "seq5", "seq6"]
    for outage_file in Path(outage_folder).iterdir():
        if auction not in str(outage_file.stem):
            worst_outage_day = str(outage_file.stem).split(".")[0]
            month = str(outage_file.stem).split(".")[1]
            year = str(outage_file.stem).split()[0][-4:]

            if any(seq in str(outage_folder).lower() for seq in seqs_outage_is_none):
                outage_file.replace(
                    outage_file.with_stem(
                        f"{auction}.Outages_{month}_{year}_None")
                )
            else:
                outage_file.replace(
                    outage_file.with_stem(
                        f"{auction}.Outages_{month}_{year}_{str(worst_outage_day).zfill(2)}")
                )


def get_monthly_auction_name(parent_directory):
    """Calculates monthly auction name based off folder name in Posting Data -> Monthly Auctions

      e.g.  '8_August 2024 Monthly' to '2024.AUG.Monthly.Auction'"""
    month = str(parent_directory).split("_")[1][:3].upper()
    year = str(parent_directory).split()[1]
    return f"{year}.{month}.Monthly.Auction"


def rename_inside_monthly_folders(destination, auction):
    "Rename files inside 6 monthly folder of LTAS auctions"
    for parent_folder in Path(destination).iterdir():
        if len(str(parent_folder).split(".")[-1]) == 3 and "zip" not in str(
            parent_folder
        ):
            month = str(parent_folder)[-3:]
            year = str(parent_folder.stem)[:4]
            for month_file in parent_folder.iterdir():

                if str(month_file.stem)[:4] != year:
                    if "contingencies" in str(month_file).lower():
                        month_file.replace(
                            month_file.with_stem(
                                f"{auction}.Common_Contingencies_{month}_{year}"
                            )
                        )
                    if "transformers" in str(month_file).lower():
                        month_file.replace(
                            month_file.with_stem(
                                f"{auction}.Common_MonitoredLinesAndTransformers_{month}_{year}"
                            )
                        )
                    if "networkmodel" in str(month_file).lower():
                        month_file.replace(
                            month_file.with_stem(
                                f"{auction}.Common_NetworkModel_{month}_{year}"
                            )
                        )
                    if "thermal" in str(month_file).lower():
                        month_file.replace(
                            month_file.with_stem(
                                f"{auction}.Common_Non-ThermalConstraints_{month}_{year}"
                            )
                        )
                    if "sources" in str(month_file).lower():
                        month_file.replace(
                            month_file.with_stem(
                                f"{auction}.Common_SourcesAndSinks_{month}_{year}"
                            )
                        )


def rename_mapdocs_folder(destination, auction):
    """Rename files inside 'Mapping Documents' folder of LTAS auctions"""
    for parent_folder in Path(destination).iterdir():
        if "mapping" in str(parent_folder).lower():
            year = str(parent_folder.stem)[:4]
            for mapping_file in parent_folder.iterdir():
                month = str(mapping_file.stem).split(".")[1]
                if str(mapping_file.stem)[-4:] != year:
                    mapping_file.replace(
                        mapping_file.with_stem(
                            f"{auction}.MappingDocument_{month}_{year}"
                        )
                    )


def rename_oneline_diagrams_folder(destination, auction):
    """Rename files inside 'KML' folder of LTAS auctions"""
    for parent_folder in Path(destination).iterdir():
        if "diagrams" in str(parent_folder).lower():
            year = str(parent_folder.stem)[:4]
            for mapping_file in parent_folder.iterdir():
                month = str(mapping_file.stem).split("_")[1]
                if auction not in str(mapping_file.stem):
                    mapping_file.replace(
                        mapping_file.with_stem(
                            f"{auction}.OneLineDiagram_{month}_{year}"
                        )
                    )
            shutil.copy(kml_readme, parent_folder)
