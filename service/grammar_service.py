import language_tool_python


class GrammarService:

    def __init__(self):
        self.tool = language_tool_python.LanguageTool("en-US")

    def check_text(self, text):

        matches = self.tool.check(text)

        corrections = []

        for match in matches:

            corrections.append({"message": match.message,"error": text[match.offset:match.offset + match.error_length],"suggestions": match.replacements[:3]})

        corrected_text = self.tool.correct(text)

        return corrections, corrected_text