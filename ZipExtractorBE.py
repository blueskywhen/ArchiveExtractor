import sys
import zipfile

def extractArchive(zipPath, destDirectory):
    with zipfile.ZipFile(zipPath, "r") as archive:
        archive.extractall(destDirectory)

if __name__ == "__main__":
    extractArchive("C:/Users/akhil/Desktop/myzip.zip",
                   "C:/Users/akhil/Desktop/Dest")
