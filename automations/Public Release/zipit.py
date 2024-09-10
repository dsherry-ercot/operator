from zipfile import ZipFile
import constants
from pathlib import Path
import glob

# specifying zip file name
zip_file_name = Path(
    rf"C:\Users\dsherry\Desktop\{constants.YEAR}_CRR_Auction_PublicRelease.zip"
)


def zip_files():
    file_paths = glob.glob(f"{constants.parent}/*.xlsx")
    with ZipFile(zip_file_name, "w") as zip:
        for file in file_paths:
            zip.write(file, arcname=file.split("\\")[-1])
    print("All files zipped successfully!")


if __name__ == "__main__":
    zip_files()
