import requests


class DictionarySearch:
    def __init__(self, search_word):
        self.word = search_word
        self.ans = word + '. '
        self.flag = False

    def dictionary_api(self):
        dictionary_api_url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'
        response = requests.get(dictionary_api_url + self.word)
        return response.json()

    def main(self):
        try:
            resp = self.dictionary_api()[0]['meanings']
            for every in resp:
                if every['partOfSpeech'] == 'noun':
                    self.ans += every['partOfSpeech'] + '. '
                    self.ans += every['definitions'][0]['definition']
                    print(self.ans)
                    self.flag = True
                    break

            if not self.flag:
                self.ans += resp[0]['partOfSpeech'] + '. '
                self.ans += resp[0]['definitions'][0]['definition']
                print(self.ans)

        except Exception as e:
            print("Word not found in the Dictionary.")


if __name__ == '__main__':
    word = raw_input("Word? ")
    Dict = DictionarySearch(word)
    Dict.main()
