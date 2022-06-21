#bdjson
class BdJson:


    #
    def __init__(self, file_route):
        self.file_route=file_route
        text= self.open()
    
    #
    def open(self):
        text = None
        with open (self.file_route, mode='r') as file:
            text = file.readlines()
        return text

    #
    def delete_characters(self, line):
        avoid = ["[","]","{","}"] 
        for av in avoid:
            if line.find(av) != -1:
                return False
        return line

    #
    def create_clean_list(self):
        lineas= []
        text = self.open()
        for line in text:
            ln = self.delete_characters(line)
            if ln != False:
                lineas.append(ln)
        return lineas

#
    def separate_data_elements(self):
        palabra = ''
        information_list= []
        lineas  = self.create_clean_list()
        dict_images={}
        for line in lineas:

            num = [pos for pos, char in enumerate(line) if char == '"']

            key = line[ num[0]+1: num[1] ]
            value = line[ num[2]+1: num[3] ]
            
            information_list.append(key)
            information_list.append(value)
        
        dict_images = self.list_to_dict(information_list)
        return dict_images

    #
    def list_to_dict(self, information_list):
        lista = information_list
        list_dict = []
        dict_images={}
        for i in range(0, len(lista), 2):
            dict_images [lista[i]] = lista[i + 1]
            list_dict.append(dict_images)
            dict_images= {}

        return list_dict


