import shutil
from pathlib import Path
import automations.Rename.funcs as funcs

kml_readme = r"Q:\Posting Data\Auction Models Posted to MIS\KML_Readme.txt"

# copy Network Model files to Downloads folder
downloads_folder = Path(Path.home(), "Downloads")


def main(from_directory):
    from_directory = rf"{from_directory}"
    # assign 'auction' variable
    if "Annual" in str(from_directory):
        auction = Path(from_directory).name
    if "Monthly" in str(from_directory):
        auction = funcs.get_monthly_auction_name(Path(from_directory).name)

    # copy Model Builder folder to user's Downloads folder
    destination = Path(downloads_folder, auction)
    shutil.copytree(from_directory, destination)

    # handle LTAS auctions
    if "Annual" in str(destination):
        funcs.rename_parent_folders(destination, auction)
        funcs.rename_outage_files(destination, auction)
        funcs.rename_inside_monthly_folders(destination, auction)
        funcs.rename_mapdocs_folder(destination, auction)
        funcs.rename_oneline_diagrams_folder(destination, auction)

    # handle Monthly auctions
    if "Monthly" in str(destination):
        for file_name in destination.iterdir():
            if str(file_name.stem)[:4] != auction[:4]:
                if "contingencies" in str(file_name).lower():
                    file_name.replace(
                        file_name.with_stem(
                            f"{auction}.Contingencies")
                    )
                if "transformers" in str(file_name).lower():
                    file_name.replace(
                        file_name.with_stem(
                            f"{auction}.MonitoredLinesAndTransformers"
                        )
                    )
                if "networkmodel" in str(file_name).lower():
                    file_name.replace(
                        file_name.with_stem(f"{auction}.NetworkModel_PeakWD")
                    )

                if "thermal" in str(file_name).lower():
                    file_name.replace(
                        file_name.with_stem(
                            f"{auction}.Non-ThermalConstraints"
                        )
                    )
                if "sources" in str(file_name).lower():
                    file_name.replace(
                        file_name.with_stem(
                            f"{auction}.SourcesAndSinks")
                    )
                if "station" in str(file_name).lower():
                    file_name.replace(file_name.with_stem(
                        f"{auction}.StationOneLines"))
                if "outage" in str(file_name).lower():
                    year = auction.split(".")[0]
                    month = auction.split(".")[1]
                    worst_outage_day = str(file_name.stem).split(".")[0]
                    file_name.replace(
                        file_name.with_stem(
                            f"{auction}.Outages_{month}_{year}_{month}{str(worst_outage_day).zfill(2)}"
                        )
                    )
            if file_name.suffix.lower() == ".kml":
                file_name.replace(file_name.with_stem(
                    f"{auction}.OneLineDiagram"))

            if "mapping" in str(file_name).lower():
                file_name.replace(
                    file_name.with_stem(
                        f"{auction}.MappingDocument"
                    )
                )

        shutil.copy(kml_readme, destination)

    shutil.make_archive(destination, "zip", destination)


if __name__ == "__main__":
    main(
        r"Q:\Posting Data\Long-Term Auctions\LTAS23 (2024.2nd6 - 2027.1st6)\2025.1st6.AnnualAuction.Seq2"
    )
