# Created by Leon Hunter at 9:54 AM 10/23/2020

from src.main.file_reader import FileReader
import os, fnmatch

class FileWriter(object):

    def __init__(self) -> None:
        super().__init__()
        self.file_reader = FileReader()

    def replace_all_text_in_files(self, parent_directory, text_to_replace, replacement_text, file_extensions=[".txt", ".java", ".py", ".html", ".css", ".js", ".ts", ".md"]):
        for path, dirs, files in os.walk(os.path.abspath(parent_directory)):
            for file_extension in file_extensions:
                for filename in fnmatch.filter(files, file_extension):
                    filepath = os.path.join(path, filename)
                    with open(filepath) as f:
                        text = f.read()
                    text = text.replace(text_to_replace, replacement_text)
                    with open(filepath, "w") as f:
                        f.write(text)

    def replace_all_text_in_local_files(self, text_to_replace, replacement_text):
        self.replace_all_text_in_files(self.file_reader.get_local_directory(), text_to_replace, replacement_text)
