import FreeSimpleGUI as sg
import ZipExtractorBE as zebe

label1 = sg.Text("Enter an archive file")
InputBox1 = sg.InputText(tooltip = "Archive file", key = "archive")
archButton = sg.FileBrowse("Select Archive")

label2 = sg.Text("Enter the destination")
InputBox2 = sg.InputText(tooltip = "Destination path", key = "OutPath")
outputButton = sg.FolderBrowse("Output Path")
completeText = sg.Text("Completed", )
startButton = sg.Button("Start")

window = sg.Window("Zip extractor", layout = [[label1, InputBox1, archButton],
                                                [label2, InputBox2, outputButton],
                                                [startButton, completeText]],
                                                    font = ("Arial", 12))
while True:
    action, value = window.read()
    print(action)
    print(value)
    zebe.extractArchive(value["archive"], value["OutPath"])
window.close()