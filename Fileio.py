import os


class FileIO:
    @staticmethod
    def read_as_string(file_name):
        try:
            """read info from file, if file exists. return a string"""
            with open(str(file_name)) as f:
                data = f.read()
                f.close()
                return data
        except FileNotFoundError:
            # we want a string either way, but this way we can let the calling class decide business logic
            return ""

    @staticmethod
    def read_as_pos_int(file_name: str)->int:
        """

        :param file_name:
        :return:
        """
        try:
            """read info from file. If file exists, return a positive int, negative for errors"""
            with open(str(file_name)) as file:
                data = file.read()
                file.close()
                if data.isnumeric():
                    return int(data)
                else:
                    return 0
        except Exception as error:
            # if there's no file, or the file has invalid data, return -1 for value
            return -1

    @staticmethod
    def mkdir(new_dir):  # returns an int to indicate status, 1 created, 0 already exists, -1 error
        try:
            os.mkdir(str(new_dir))
            return 1
        except FileExistsError:
            return 0
        except Exception as error:
            return -1

    @staticmethod
    def path_join(directory, file):
        # wrapper for path join to eliminate importing os elsewhere
        return os.path.join(str(directory), str(file))

    @staticmethod
    def overwrite(file_name, data):
        with open(file_name, 'w') as file:
            file.write(str(data))

    @staticmethod  # not needed in this project, but good to have if we use this class elsewhere
    def append(file_name, data):
        with open(str(file_name)) as current:
            data = current.read() + data
            current.close()
        with open(str(file_name), 'w') as f:
            f.write(data)
            f.close()

    @staticmethod
    def list_file_names(directory: str = ".")->list:
        return os.listdir(directory)
