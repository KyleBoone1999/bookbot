
class Book:
    def __init__(self, file_path, title = None):
        self.file_path = file_path
        if title is None:
            self.title = file_path[:]
        else:
            self.title = title
        with open(file_path, "r") as f:
            book = f.read()
            self.str = book
            f.close()

    def count_letters(self, counts = dict()):
        words = [w.lower() for w in self.str.split()]
        if not "word_count" in self.__dict__:
            self.word_count = len(words)
        for w in words:
            for letter in w:
                if letter not in counts:
                    counts[letter] = 0
                counts[letter] += 1
        return counts

    def letter_report(self):
        letter_counts = self.count_letters()
        report = ''
        report += f"--- Begin letter report of {self.title} ---" + "\n"
        report += f"{self.word_count} words counted in {self.file_path}" + "\n\n"
        for k, v in sorted(letter_counts.items(), key = lambda x: x[1], reverse=True):
            report += f"Character '{k}' was counted {v} times" + "\n"
        report += f"--- End letter report of {self.file_path} ---"
        return report



def main():
    this_book = Book("./books/frankenstein.txt", title="Frankenstein")
    print(this_book.letter_report())
        

main()