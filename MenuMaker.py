

class menu_maker:
    @staticmethod
    def show_menu(options_list: dict, replace_underscore: bool = True):
        """

        :param options_list:
        :param replace_underscore:
        :return:
        """
        valid_selection = False
        while not valid_selection:
            # displays a list of choices and then returns user result

            menu = "Please choose from one of the available options: \n"
            for option in options_list.keys():
                option = str(option)
                item_number = str(list(options_list.keys()).index(option) + 1).rjust(5," ")
                if replace_underscore:
                    option = option.replace("_", " ")
                option = option.title()
                menu += "{}:\t{}\n".format(item_number, option)
            choice = input(menu)

            if choice.isnumeric():
                if int(choice) <= len(options_list):
                    return options_list[int(choice)-1]

            elif choice in options_list:
                return choice
            else:
                continue

    @staticmethod
    def make_menu_from_class(class_data):
        class_dict = dict(class_data.__dict__)
        return_dict = {}
        for each in class_dict.keys():
            if not str(each).startswith("_"):
                return_dict[each] = class_dict[each]

        print(return_dict)
        menu_maker.show_menu(return_dict)

