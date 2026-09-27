import re


class FillerService:

    def find_filler_words(self, text):

        fillers = ["um","uh","umm","like","actually","basically","you know","I mean","so","well","literally","seriously","honestly","right","okay","alright"]

        found = {}

        text = text.lower()

        for filler in fillers:

            pattern = r"\b" + re.escape(filler) + r"\b"

            count = len(re.findall(pattern, text))

            if count > 0:
                found[filler] = count

        return found