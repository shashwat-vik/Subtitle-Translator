from translate import Translator

class Extractor:
    def __init__(self, file_path):
        self.translate = Translator()
        with open(file_path, 'rb') as f:
            self.raw_text = f.read().decode('utf-8')
        self.output = ""

    def parse_translate(self):
        splits = self.raw_text.split('\r\n')
        count = 1

        start_signal = False
        end_signal = False
        offset = 0

        for split in splits:
            if split == str(count):
                start_signal = True
                if start_signal:
                    end_signal = True
                count += 1

            if start_signal:
                if end_signal:
                    offset = 0
                    end_signal = False
                offset += 1

                if offset >=3:
                    if split:
                        magic = self.translate.text_translate(split)
                        # FOR DISPLAY WITH NO UNICODE SUPPORT
                        print (split.encode('utf-8').decode('ascii','replace').replace('\uFFFD','?'),' --> ',magic)
                        self.output +=  magic + '\r\n'
                    else:
                        self.output += split + '\r\n'
                else:
                    self.output += split + '\r\n'

    def write(self):
        with open('output/english_translation.srt','wb') as f:
            f.write(self.output.encode('utf-8'))

    def run(self):
        self.parse_translate()
        self.write()
