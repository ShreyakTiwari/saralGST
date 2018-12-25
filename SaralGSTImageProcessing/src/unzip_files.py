import zipfile

class unzip:

   
    '''
    this function takes a zip files and unzp it

    arguments : 
    path_to_zip_file: input zip file
    directory_to_extract_to: output directory
    '''
    @staticmethod
    def unzip(path_to_zip_file, directory_to_extract_to):
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall(directory_to_extract_to)