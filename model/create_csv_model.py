import csv
import os

class CreateCsvModel:
    def __init__(self, name_file: str, columns_count: int, headers: list, sep: str = ','):
        if len(headers) != columns_count:
            raise ValueError(
                f'Количество заголовков ({len(headers)}) не совпадает с количеством столбцов ({columns_count})'
            )

        self.name_file = 'datasets/' + name_file + '.csv'
        self.columns_count = columns_count
        self.headers = headers
        self.sep = sep

        file_exists = os.path.exists(self.name_file)

        self.file = open(self.name_file, mode='a', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file, delimiter=self.sep)

        if not file_exists or os.stat(self.name_file).st_size == 0:
            self.writer.writerow(self.headers)

    def write_line(self, line_list: list):
        if len(line_list) != self.columns_count:
            raise ValueError(
                f'Количество элементов списка ({len(line_list)}) не совпадает с количеством столбцов ({self.columns_count})'
            )
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
