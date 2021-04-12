# Created by Leon Hunter at 9:54 AM 10/23/2020
import os


class FileReader(object):
    def get_local_directory(self):
        return os.path.dirname(os.path.abspath("README.md"))

    def get_text_of_file(self, absolute_path_to_file):
        with open(absolute_path_to_file, 'r') as file:
            text = file.read()
        return text

    def get_all_files(self, parent_directory):
        file_list = []
        for root, dirs, files in os.walk(parent_directory):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list

    def get_all_local_files(self):
        return self.get_all_files(self.get_local_directory())

    def get_all_files_containing_text(self, parent_directory, text_to_search_for):
        all_files_containing_text = []
        for file_path in self.get_all_files(parent_directory):
            try:
                if text_to_search_for in self.get_text_of_file(file_path):
                    all_files_containing_text.append(file_path)
            except:
                pass
        return all_files_containing_text

    def get_all_local_files_containing_text(self, text_to_search_for):
        return self.get_all_files_containing_text(self.get_local_directory(), text_to_search_for)



print(FileReader().get_all_local_files_containing_text("all_"))
