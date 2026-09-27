from service.speech_to_text_service import SpeechToTextService
from service.filler_service import FillerService
from service.grammar_service import GrammarService


class SpeakingAnalysisService:

    def __init__(self):

        self.speech_service = SpeechToTextService()
        self.filler_service = FillerService()
        self.grammar_service = GrammarService()

    def analyze(self, audio_path):

  
        transcript = self.speech_service.convert_audio_to_text(audio_path)

        fillers = self.filler_service.find_filler_words(transcript)

        mistakes, corrected_text = self.grammar_service.check_text(transcript)

        return {
            "transcript": transcript,
            "fillers": fillers,
            "mistakes": mistakes,
            "corrected_text": corrected_text
        }