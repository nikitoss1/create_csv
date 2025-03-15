import csv

class CreateCsvModel:

    def __init__(self, name_file: str, columns_count: int, headers: list, sep: str=','):
        
        if len(headers) != columns_count:
            raise ValueError(f'Количество заголовков ({columns_count}) не совпадает с количеством столбцов ({columns_count})')

        self.name_file = name_file + '.csv'
        self.columns_count = columns_count
        self.headers = headers
        self.sep = sep

        self.file = open('datasets/'+ self.name_file, mode='w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file, delimiter=self.sep)

        self.writer.writerow(self.headers)

    def write_line(self, line_list: list):
        length_list = len(line_list)
        if length_list != self.columns_count:
            raise ValueError(f'Количество элементов списка ({length_list}) не совпадает с количеством столбцов ({self.columns_count})')
        
        self.writer.writerow(line_list)

    def close(self):
        self.file.close()

if __name__ == '__main__':
    headers = ['Name', 'Age', 'City']
    line1 = ['Vadim', 22, 'Moscow']
    line2 = ['Kirill', 34, 'Novgorod']

    o = CreateCsvModel('persons', 3, headers=headers)
    o.write_line(line1)
    o.write_line(line2)

    o.close()