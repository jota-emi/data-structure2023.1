from csv import reader

class Dataset:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []
        self.header = None
        self.read_data()

    def read_data(self):
        with open(self.file_path) as file:
            read_file = reader(file)
            self.data = list(read_file)
            self.header = self.data[0]
            self.data = self.data[1:]

    def explore_data(self, start, end, rows_and_columns=False):
        dataset_slice = self.data[start:end]    
        for row in dataset_slice:
            print(row)
            print('\n') # adds a new (empty) line between rows
        
        if rows_and_columns:
            print('Number of rows:', len(self.data))
            print('Number of columns:', len(self.header))

    def get_reviews_max(self):
        reviews_max = {}
        for app in self.data:
            name = app[0]
            n_reviews = float(app[3])

            if name in reviews_max and reviews_max[name] < n_reviews:
                reviews_max[name] = n_reviews

            elif name not in reviews_max:
                reviews_max[name] = n_reviews

        return reviews_max

    def clean_data(self):
        reviews_max = self.get_reviews_max()
        android_clean = []
        already_added = []

        for app in self.data:
            name = app[0]
            n_reviews = float(app[3])

            if (reviews_max[name] == n_reviews) and (name not in already_added):
                android_clean.append(app)
                already_added.append(name)

        self.data = android_clean

    def is_english(self, string):
        non_ascii = 0

        for character in string:
            if ord(character) > 127:
                non_ascii += 1

        if non_ascii > 3:
            return False
        else:
            return True

    def filter_english_apps(self):
        android_english = []
        for app in self.data:
            name = app[0]
            if self.is_english(name):
                android_english.append(app)
        self.data = android_english

    def filter_free_apps(self):
        android_final = []
        for app in self.data:
            price = app[7]
            if price == '0':
                android_final.append(app)
        self.data = android_final

    def get_categories_frequency(self):
        categories_frequency = {}
        for app in self.data:
            category = app[1]
            if category in categories_frequency:
                categories_frequency[category] += 1
            else:
                categories_frequency[category] = 1

        return categories_frequency
    
    def main():
        ios_dataset = Dataset('AppleStore.csv')
        print(ios_dataset.header)
        ios_dataset.explore_data(0, 3, True)

        android_dataset = Dataset('googleplaystore.csv')
        print(android_dataset.header)
        android_dataset.explore_data(0, 3, True)

        android_dataset.clean_data()
        android_dataset.filter_english_apps()
        android_dataset.filter_free_apps()

        categories_frequency = android_dataset.get_categories_frequency()
        for category in categories_frequency:
            total = 0
            len_category = 0
            for app in android_dataset.data:
                category_app = app[1]
                if category_app == category:
                    total += float(app[5])
                    len_category += 1
            avg_rating = total / len_category
            print(category, avg_rating)

    main()