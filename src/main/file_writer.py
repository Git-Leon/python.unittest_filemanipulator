# Created by Leon Hunter at 9:54 AM 10/23/2020

from src.main.file_reader import FileReader


class FileWriter(object):
    def __init__(self) -> None:
        super().__init__()
        self.file_reader = FileReader()

    def replace_all_text_in_files(self, parent_directory, text_to_replace, replacement_text):
        files_with_text_to_be_replaced = self.file_reader.get_all_files_containing_text(parent_directory, text_to_replace)
        for file_path in files_with_text_to_be_replaced:
            file_out = open(file_path, 'w+')
            text = file_out.read()
            text = text.replace(text_to_replace, replacement_text)
            file_out.write(text)
            file_out.close()

    def replace_all_text_in_local_files(self, text_to_replace, replacement_text):
        self.replace_all_text_in_files(self.file_reader.get_local_directory(), text_to_replace, replacement_text)
