import tkinter as tk
from tkinter import messagebox
from datetime import date


from service.timebox_service import TimeboxService
from service.reading_service import ReadingService
from service.vocabulary_service import VocabularyService
from service.speaking_service import SpeakingService
from service.speaking_analysis_service import SpeakingAnalysisService
from service.writing_service import WritingService
from service.grammar_service import GrammarService
from service.performance_service import PerformanceService

from model.performance import Performance


class Dashboard:

    def __init__(self):

        # ==========================================
        # MAIN WINDOW
        # ==========================================

        self.root = tk.Tk()

        self.root.title(
            "English Timebox - AI English Practice"
        )

        self.root.geometry(
            "950x750"
        )

        self.root.minsize(
            850,
            650
        )

        self.root.configure(
            bg="#F5F7FB"
        )

        # ==========================================
        # USER
        # ==========================================

        self.user_id = 1

        # ==========================================
        # SERVICES
        # ==========================================

        self.timebox_service = TimeboxService()

        self.reading_service = ReadingService()

        self.vocabulary_service = VocabularyService()

        self.speaking_service = SpeakingService()

        self.speaking_analysis_service = (
            SpeakingAnalysisService()
        )

        self.writing_service = WritingService()

        self.grammar_service = GrammarService()

        self.performance_service = PerformanceService()

        # ==========================================
        # VARIABLES
        # ==========================================

        self.current_content_id = None

        self.speaking_result = None

        self.writing_response = None

        self.writing_mistakes = []

        self.writing_corrected = ""

        self.performance_saved = False

        # ==========================================
        # COLORS
        # ==========================================

        self.bg_color = "#F5F7FB"

        self.card_color = "#FFFFFF"

        self.text_color = "#1F2937"

        self.secondary_color = "#6B7280"

        self.primary_color = "#2563EB"

        self.success_color = "#16A34A"

        self.warning_color = "#F59E0B"

        self.danger_color = "#DC2626"

        # ==========================================
        # START
        # ==========================================

        self.show_timebox()

        self.root.mainloop()

    # ==========================================
    # CLEAR SCREEN
    # ==========================================

    def clear_screen(self):

        for widget in self.root.winfo_children():

            widget.destroy()

    # ==========================================
    # HEADER
    # ==========================================

    def create_header(
        self,
        title,
        subtitle=None
    ):

        header = tk.Frame(
            self.root,
            bg=self.primary_color,
            height=105
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(
            False
        )

        title_label = tk.Label(
            header,
            text=title,
            font=(
                "Arial",
                24,
                "bold"
            ),
            bg=self.primary_color,
            fg="white"
        )

        title_label.pack(
            pady=(18, 2)
        )

        if subtitle:

            subtitle_label = tk.Label(
                header,
                text=subtitle,
                font=(
                    "Arial",
                    11
                ),
                bg=self.primary_color,
                fg="#E5E7EB"
            )

            subtitle_label.pack()

    # ==========================================
    # BUTTON
    # ==========================================

    def create_button(
        self,
        parent,
        text,
        command,
        width=25
    ):

        return tk.Button(
            parent,
            text=text,
            command=command,
            width=width,
            height=2,
            font=(
                "Arial",
                11,
                "bold"
            ),
            bg=self.primary_color,
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            relief="flat",
            cursor="hand2"
        )

    # ==========================================
    # CARD
    # ==========================================

    def create_card(
        self,
        parent
    ):

        return tk.Frame(
            parent,
            bg=self.card_color,
            bd=1,
            relief="solid"
        )

    # ==========================================
    # TIMEBOX
    # ==========================================

    def show_timebox(self):

        self.clear_screen()

        self.create_header(
            "⏱️ English Timebox",
            "Your personalized English practice session"
        )

        container = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        container.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=30
        )

        title = tk.Label(
            container,
            text="Today's Practice Plan",
            font=(
                "Arial",
                20,
                "bold"
            ),
            bg=self.bg_color,
            fg=self.text_color
        )

        title.pack(
            pady=(5, 20)
        )

        timebox = (
            self.timebox_service
            .get_today_timebox(
                self.user_id
            )
        )

        if not timebox:

            label = tk.Label(
                container,
                text="No practice plan found for today.",
                font=(
                    "Arial",
                    15
                ),
                bg=self.bg_color,
                fg=self.secondary_color
            )

            label.pack(
                pady=50
            )

            return

        total_minutes = 0

        for item in timebox:

            activity_name = item[2]

            minutes = item[3]

            total_minutes += minutes

            card = self.create_card(
                container
            )

            card.pack(
                fill="x",
                pady=5
            )

            activity_label = tk.Label(
                card,
                text=activity_name.capitalize(),
                font=(
                    "Arial",
                    14,
                    "bold"
                ),
                bg=self.card_color,
                fg=self.text_color
            )

            activity_label.pack(
                side="left",
                padx=20,
                pady=14
            )

            minute_label = tk.Label(
                card,
                text=f"{minutes} min",
                font=(
                    "Arial",
                    12,
                    "bold"
                ),
                bg=self.card_color,
                fg=self.primary_color
            )

            minute_label.pack(
                side="right",
                padx=20
            )

        total = tk.Label(
            container,
            text=f"Total Practice Time: {total_minutes} minutes",
            font=(
                "Arial",
                14,
                "bold"
            ),
            bg=self.bg_color,
            fg=self.text_color
        )

        total.pack(
            pady=20
        )

        start_button = self.create_button(
            container,
            "▶ Start Practice",
            self.show_story
        )

        start_button.pack()

    # ==========================================
    # READING
    # ==========================================

    def show_story(self):

        self.clear_screen()

        self.create_header(
            "📖 Reading Practice",
            "Read carefully and understand the story"
        )

        container = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        container.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=25
        )

        # IMPORTANT:
        # Grid gives the story area flexible space
        # while keeping the Next button visible.

        container.grid_rowconfigure(
            1,
            weight=1
        )

        container.grid_columnconfigure(
            0,
            weight=1
        )

        content = (
            self.reading_service
            .get_all_content()
        )

        if not content:

            self.show_error(
                "No reading content found."
            )

            return

        story = content[0]

        self.current_content_id = story[0]

        # ==========================================
        # TITLE
        # ==========================================

        title = tk.Label(
            container,
            text=story[1],
            font=(
                "Arial",
                20,
                "bold"
            ),
            bg=self.bg_color,
            fg=self.text_color
        )

        title.grid(
            row=0,
            column=0,
            pady=(5, 15)
        )

        # ==========================================
        # READING AREA
        # ==========================================

        reading_frame = tk.Frame(
            container,
            bg=self.card_color,
            bd=1,
            relief="solid"
        )

        reading_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            pady=(0, 15)
        )

        scrollbar = tk.Scrollbar(
            reading_frame
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        story_box = tk.Text(
            reading_frame,
            wrap="word",
            font=(
                "Arial",
                14
            ),
            bg=self.card_color,
            fg=self.text_color,
            padx=20,
            pady=20,
            yscrollcommand=scrollbar.set,
            relief="flat"
        )

        story_box.insert(
            "1.0",
            story[2]
        )

        story_box.config(
            state="disabled"
        )

        story_box.pack(
            fill="both",
            expand=True
        )

        scrollbar.config(
            command=story_box.yview
        )

        # ==========================================
        # NEXT BUTTON
        # ==========================================

        next_button = self.create_button(
            container,
            "➡ Next: Vocabulary",
            self.reading_completed
        )

        next_button.grid(
            row=2,
            column=0,
            pady=(0, 5)
        )

    # ==========================================
    # VOCABULARY
    # ==========================================

    def reading_completed(self):

        self.clear_screen()

        self.create_header(
            "📚 Vocabulary",
            "Learn useful words from today's reading"
        )

        container = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        container.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=25
        )

        vocabulary = (
            self.vocabulary_service
            .get_vocabulary_by_content(
                self.current_content_id
            )
        )

        if vocabulary:

            for item in vocabulary:

                word = item[1]

                meaning = item[2]

                example = item[3]

                card = self.create_card(
                    container
                )

                card.pack(
                    fill="x",
                    pady=5
                )

                word_label = tk.Label(
                    card,
                    text=word,
                    font=(
                        "Arial",
                        15,
                        "bold"
                    ),
                    bg=self.card_color,
                    fg=self.primary_color
                )

                word_label.pack(
                    anchor="w",
                    padx=20,
                    pady=(12, 2)
                )

                meaning_label = tk.Label(
                    card,
                    text=f"Meaning: {meaning}",
                    font=(
                        "Arial",
                        12
                    ),
                    bg=self.card_color,
                    fg=self.text_color
                )

                meaning_label.pack(
                    anchor="w",
                    padx=20
                )

                example_label = tk.Label(
                    card,
                    text=f"Example: {example}",
                    font=(
                        "Arial",
                        11,
                        "italic"
                    ),
                    bg=self.card_color,
                    fg=self.secondary_color,
                    wraplength=750,
                    justify="left"
                )

                example_label.pack(
                    anchor="w",
                    padx=20,
                    pady=(2, 12)
                )

        else:

            label = tk.Label(
                container,
                text="No vocabulary found.",
                font=(
                    "Arial",
                    15
                ),
                bg=self.bg_color,
                fg=self.secondary_color
            )

            label.pack(
                pady=50
            )

        next_button = self.create_button(
            container,
            "➡ Next: Speaking",
            self.show_speaking
        )

        next_button.pack(
            pady=15
        )

    # ==========================================
    # SPEAKING
    # ==========================================

    def show_speaking(self):

        self.clear_screen()

        self.create_header(
            "🎤 Speaking Practice",
            "Speak naturally and stop whenever you finish"
        )

        container = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        container.pack(
            fill="both",
            expand=True,
            padx=60,
            pady=40
        )

        # ==========================================
        # TOPIC
        # ==========================================

        topic_card = self.create_card(
            container
        )

        topic_card.pack(
            fill="x",
            pady=20
        )

        topic_title = tk.Label(
            topic_card,
            text="Today's Topic",
            font=(
                "Arial",
                16,
                "bold"
            ),
            bg=self.card_color,
            fg=self.primary_color
        )

        topic_title.pack(
            pady=(20, 10)
        )

        topic = tk.Label(
            topic_card,
            text=(
                "What would you do if you found "
                "a wallet containing ₹50,000?"
            ),
            font=(
                "Arial",
                16
            ),
            bg=self.card_color,
            fg=self.text_color,
            wraplength=700
        )

        topic.pack(
            padx=30,
            pady=(0, 25)
        )

        instruction = tk.Label(
            container,
            text="Speak for as long as you want.",
            font=(
                "Arial",
                13
            ),
            bg=self.bg_color,
            fg=self.secondary_color
        )

        instruction.pack(
            pady=10
        )

        # ==========================================
        # START
        # ==========================================

        self.start_button = self.create_button(
            container,
            "🎙 Start Recording",
            self.start_recording
        )

        self.start_button.pack(
            pady=7
        )

        # ==========================================
        # STOP
        # ==========================================

        self.stop_button = self.create_button(
            container,
            "🛑 Stop Recording",
            self.stop_recording
        )

        self.stop_button.pack(
            pady=7
        )

        self.stop_button.config(
            state="disabled"
        )

        # ==========================================
        # STATUS
        # ==========================================

        self.record_status = tk.Label(
            container,
            text="Ready to record",
            font=(
                "Arial",
                13,
                "bold"
            ),
            bg=self.bg_color,
            fg=self.success_color
        )

        self.record_status.pack(
            pady=15
        )

    # ==========================================
    # START RECORDING
    # ==========================================

    def start_recording(self):

        try:

            self.speaking_service.start_recording()

            self.start_button.config(
                state="disabled"
            )

            self.stop_button.config(
                state="normal"
            )

            self.record_status.config(
                text="🔴 Recording... Speak now",
                fg=self.danger_color
            )

        except Exception as e:

            messagebox.showerror(
                "Recording Error",
                str(e)
            )

    # ==========================================
    # STOP RECORDING
    # ==========================================

    def stop_recording(self):

        filename = (
            "audio/recordings/speaking.wav"
        )

        try:

            self.record_status.config(
                text="⏳ Saving recording...",
                fg=self.warning_color
            )

            self.stop_button.config(
                state="disabled"
            )

            self.root.update()

            self.speaking_service.stop_recording(
                filename
            )

            self.record_status.config(
                text="🔎 Analyzing speech...",
                fg=self.warning_color
            )

            self.root.update()

            result = (
                self.speaking_analysis_service
                .analyze(filename)
            )

            self.speaking_result = result

            self.show_speaking_analysis(
                result
            )

        except Exception as e:

            messagebox.showerror(
                "Speaking Error",
                str(e)
            )

            self.start_button.config(
                state="normal"
            )

            self.stop_button.config(
                state="disabled"
            )

    # ==========================================
    # SPEAKING ANALYSIS
    # ==========================================

    def show_speaking_analysis(
        self,
        result
    ):

        self.clear_screen()

        self.create_header(
            "🔎 Speaking Analysis",
            "Review your speech performance"
        )

        container = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        container.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=20
        )

        # ==========================================
        # TRANSCRIPT
        # ==========================================

        title = tk.Label(
            container,
            text="📝 Your Speech",
            font=(
                "Arial",
                16,
                "bold"
            ),
            bg=self.bg_color,
            fg=self.text_color
        )

        title.pack(
            anchor="w"
        )

        transcript_box = tk.Text(
            container,
            height=5,
            wrap="word",
            font=(
                "Arial",
                12
            )
        )

        transcript_box.insert(
            "1.0",
            result["transcript"]
        )

        transcript_box.config(
            state="disabled"
        )

        transcript_box.pack(
            fill="x",
            pady=(5, 15)
        )

        # ==========================================
        # FILLERS
        # ==========================================

        filler_title = tk.Label(
            container,
            text="🔎 Filler Words",
            font=(
                "Arial",
                16,
                "bold"
            ),
            bg=self.bg_color,
            fg=self.text_color
        )

        filler_title.pack(
            anchor="w"
        )

        fillers = result["fillers"]

        if fillers:

            filler_text = ", ".join(
                f"{word}: {count}"
                for word, count
                in fillers.items()
            )

        else:

            filler_text = (
                "No filler words detected 🎉"
            )

        filler_label = tk.Label(
            container,
            text=filler_text,
            font=(
                "Arial",
                12
            ),
            bg=self.bg_color,
            fg=self.secondary_color,
            wraplength=750
        )

        filler_label.pack(
            anchor="w",
            pady=(3, 12)
        )

        # ==========================================
        # GRAMMAR
        # ==========================================

        grammar_title = tk.Label(
            container,
            text="✍️ Grammar Mistakes",
            font=(
                "Arial",
                16,
                "bold"
            ),
            bg=self.bg_color,
            fg=self.text_color
        )

        grammar_title.pack(
            anchor="w"
        )

        mistakes = result["mistakes"]

        if mistakes:

            for mistake in mistakes:

                suggestions = ", ".join(
                    mistake["suggestions"]
                )

                text = (
                    f"❌ {mistake['error']}\n"
                    f"Reason: {mistake['message']}\n"
                    f"Suggestion: {suggestions}"
                )

                label = tk.Label(
                    container,
                    text=text,
                    font=(
                        "Arial",
                        11
                    ),
                    bg=self.card_color,
                    fg=self.text_color,
                    justify="left",
                    anchor="w",
                    padx=12,
                    pady=8,
                    wraplength=750
                )

                label.pack(
                    fill="x",
                    pady=3
                )

        else:

            label = tk.Label(
                container,
                text="✅ No grammar mistakes detected!",
                font=(
                    "Arial",
                    12,
                    "bold"
                ),
                bg=self.bg_color,
                fg=self.success_color
            )

            label.pack(
                anchor="w",
                pady=5
            )

        # ==========================================
        # CORRECT VERSION
        # ==========================================

        correct_title = tk.Label(
            container,
            text="✅ Correct Version",
            font=(
                "Arial",
                16,
                "bold"
            ),
            bg=self.bg_color,
            fg=self.text_color
        )

        correct_title.pack(
            anchor="w",
            pady=(10, 3)
        )

        correct_box = tk.Text(
            container,
            height=4,
            wrap="word",
            font=(
                "Arial",
                12
            )
        )

        correct_box.insert(
            "1.0",
            result["corrected_text"]
        )

        correct_box.config(
            state="disabled"
        )

        correct_box.pack(
            fill="x"
        )

        next_button = self.create_button(
            container,
            "➡ Next: Writing",
            self.show_writing
        )

        next_button.pack(
            pady=15
        )

    # ==========================================
    # WRITING
    # ==========================================

    def show_writing(self):

        self.clear_screen()

        self.create_header(
            "✍️ Writing Practice",
            "Write your thoughts clearly and confidently"
        )

        container = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        container.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=30
        )

        topic = tk.Label(
            container,
            text=(
                "Write about what you learned from "
                "the story and what you would do "
                "in a similar situation."
            ),
            font=(
                "Arial",
                15
            ),
            bg=self.bg_color,
            fg=self.text_color,
            wraplength=700
        )

        topic.pack(
            pady=10
        )

        self.writing_box = tk.Text(
            container,
            height=14,
            wrap="word",
            font=(
                "Arial",
                13
            ),
            padx=10,
            pady=10
        )

        self.writing_box.pack(
            fill="both",
            expand=True,
            pady=15
        )

        submit_button = self.create_button(
            container,
            "✓ Submit Writing",
            self.submit_writing
        )

        submit_button.pack(
            pady=10
        )

    # ==========================================
    # SUBMIT WRITING
    # ==========================================

    def submit_writing(self):

        response = (
            self.writing_box
            .get(
                "1.0",
                "end"
            )
            .strip()
        )

        if not response:

            messagebox.showwarning(
                "Writing",
                "Please write something first."
            )

            return

        try:

            self.writing_service.add_writing(
                self.user_id,
                self.current_content_id,
                response
            )

            mistakes, corrected_text = (
                self.grammar_service
                .check_text(
                    response
                )
            )

            self.writing_response = response

            self.writing_mistakes = mistakes

            self.writing_corrected = (
                corrected_text
            )

            self.show_writing_result(
                response,
                mistakes,
                corrected_text
            )

        except Exception as e:

            messagebox.showerror(
                "Writing Error",
                str(e)
            )

    # ==========================================
    # WRITING RESULT
    # ==========================================

    def show_writing_result(
        self,
        response,
        mistakes,
        corrected_text
    ):

        self.clear_screen()

        self.create_header(
            "📝 Writing Analysis",
            "Review and improve your writing"
        )

        container = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        container.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=20
        )

        title = tk.Label(
            container,
            text="Your Writing",
            font=(
                "Arial",
                16,
                "bold"
            ),
            bg=self.bg_color,
            fg=self.text_color
        )

        title.pack(
            anchor="w"
        )

        original_box = tk.Text(
            container,
            height=6,
            wrap="word",
            font=(
                "Arial",
                12
            )
        )

        original_box.insert(
            "1.0",
            response
        )

        original_box.config(
            state="disabled"
        )

        original_box.pack(
            fill="x",
            pady=(5, 15)
        )

        grammar_title = tk.Label(
            container,
            text="✍️ Grammar Analysis",
            font=(
                "Arial",
                16,
                "bold"
            ),
            bg=self.bg_color,
            fg=self.text_color
        )

        grammar_title.pack(
            anchor="w"
        )

        if mistakes:

            for mistake in mistakes:

                suggestions = ", ".join(
                    mistake["suggestions"]
                )

                text = (
                    f"❌ {mistake['error']}\n"
                    f"Reason: {mistake['message']}\n"
                    f"Suggestion: {suggestions}"
                )

                label = tk.Label(
                    container,
                    text=text,
                    font=(
                        "Arial",
                        11
                    ),
                    bg=self.card_color,
                    fg=self.text_color,
                    justify="left",
                    anchor="w",
                    padx=12,
                    pady=8,
                    wraplength=750
                )

                label.pack(
                    fill="x",
                    pady=3
                )

        else:

            label = tk.Label(
                container,
                text="✅ No grammar mistakes detected!",
                font=(
                    "Arial",
                    12,
                    "bold"
                ),
                bg=self.bg_color,
                fg=self.success_color
            )

            label.pack(
                anchor="w",
                pady=8
            )

        correct_title = tk.Label(
            container,
            text="✅ Correct Version",
            font=(
                "Arial",
                16,
                "bold"
            ),
            bg=self.bg_color,
            fg=self.text_color
        )

        correct_title.pack(
            anchor="w",
            pady=(10, 3)
        )

        correct_box = tk.Text(
            container,
            height=5,
            wrap="word",
            font=(
                "Arial",
                12
            )
        )

        correct_box.insert(
            "1.0",
            corrected_text
        )

        correct_box.config(
            state="disabled"
        )

        correct_box.pack(
            fill="x"
        )

        performance_button = self.create_button(
            container,
            "📊 View Performance",
            self.show_performance
        )

        performance_button.pack(
            pady=15
        )

    # ==========================================
    # PERFORMANCE
    # ==========================================

    def show_performance(self):

        self.clear_screen()

        self.create_header(
            "📊 Today's Performance",
            "Your English practice results"
        )

        container = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        container.pack(
            fill="both",
            expand=True,
            padx=60,
            pady=30
        )

        # ==========================================
        # SPEAKING SCORE
        # ==========================================

        speaking_score = 0

        speaking_mistakes = 0

        if self.speaking_result:

            speaking_mistakes = len(
                self.speaking_result[
                    "mistakes"
                ]
            )

            filler_count = sum(
                self.speaking_result[
                    "fillers"
                ].values()
            )

            speaking_score = max(
                0,
                100
                - (
                    speaking_mistakes * 5
                )
                - (
                    filler_count * 2
                )
            )

        # ==========================================
        # WRITING SCORE
        # ==========================================

        writing_score = 0

        writing_mistakes = 0

        if self.writing_response:

            writing_mistakes = len(
                self.writing_mistakes
            )

            writing_score = max(
                0,
                100
                - (
                    writing_mistakes * 5
                )
            )

            word_count = len(
                self.writing_response.split()
            )

            if word_count < 30:

                writing_score = max(
                    0,
                    writing_score - 10
                )

        # ==========================================
        # SAVE ONLY ONCE
        # ==========================================

        if not self.performance_saved:

            speaking_performance = Performance(
                user_id=self.user_id,
                activity_id=3,
                score=speaking_score,
                mistake_count=speaking_mistakes,
                performance_date=date.today()
            )

            self.performance_service.add_performance(
                speaking_performance
            )

            writing_performance = Performance(
                user_id=self.user_id,
                activity_id=4,
                score=writing_score,
                mistake_count=writing_mistakes,
                performance_date=date.today()
            )

            self.performance_service.add_performance(
                writing_performance
            )

            self.performance_saved = True

        # ==========================================
        # OVERALL
        # ==========================================

        overall_score = int(
            (
                speaking_score
                + writing_score
            ) / 2
        )

        # ==========================================
        # SCORE CARDS
        # ==========================================

        score_frame = tk.Frame(
            container,
            bg=self.bg_color
        )

        score_frame.pack(
            fill="x",
            pady=10
        )

        # SPEAKING

        speaking_card = self.create_card(
            score_frame
        )

        speaking_card.pack(
            side="left",
            expand=True,
            fill="both",
            padx=5
        )

        tk.Label(
            speaking_card,
            text="🎤 Speaking",
            font=(
                "Arial",
                15,
                "bold"
            ),
            bg=self.card_color,
            fg=self.text_color
        ).pack(
            pady=(20, 5)
        )

        tk.Label(
            speaking_card,
            text=f"{speaking_score}/100",
            font=(
                "Arial",
                28,
                "bold"
            ),
            bg=self.card_color,
            fg=self.primary_color
        ).pack(
            pady=(0, 20)
        )

        # WRITING

        writing_card = self.create_card(
            score_frame
        )

        writing_card.pack(
            side="left",
            expand=True,
            fill="both",
            padx=5
        )

        tk.Label(
            writing_card,
            text="✍️ Writing",
            font=(
                "Arial",
                15,
                "bold"
            ),
            bg=self.card_color,
            fg=self.text_color
        ).pack(
            pady=(20, 5)
        )

        tk.Label(
            writing_card,
            text=f"{writing_score}/100",
            font=(
                "Arial",
                28,
                "bold"
            ),
            bg=self.card_color,
            fg=self.primary_color
        ).pack(
            pady=(0, 20)
        )

        # OVERALL

        overall_card = self.create_card(
            score_frame
        )

        overall_card.pack(
            side="left",
            expand=True,
            fill="both",
            padx=5
        )

        tk.Label(
            overall_card,
            text="🏆 Overall",
            font=(
                "Arial",
                15,
                "bold"
            ),
            bg=self.card_color,
            fg=self.text_color
        ).pack(
            pady=(20, 5)
        )

        tk.Label(
            overall_card,
            text=f"{overall_score}/100",
            font=(
                "Arial",
                28,
                "bold"
            ),
            bg=self.card_color,
            fg=self.success_color
        ).pack(
            pady=(0, 20)
        )

        # ==========================================
        # SUMMARY
        # ==========================================

        summary = tk.Label(
            container,
            text=(
                "📖 Reading       ✓ Completed\n"
                "📚 Vocabulary    ✓ Completed\n"
                f"🎤 Speaking      {speaking_score}/100\n"
                f"✍️ Writing       {writing_score}/100"
            ),
            font=(
                "Arial",
                13
            ),
            bg=self.bg_color,
            fg=self.text_color,
            justify="left"
        )

        summary.pack(
            pady=20
        )

        # ==========================================
        # PROGRESS
        # ==========================================

        progress_button = self.create_button(
            container,
            "📈 View My Progress",
            self.show_progress
        )

        progress_button.pack(
            pady=8
        )

        # ==========================================
        # FINISH
        # ==========================================

        finish_button = tk.Button(
            container,
            text="Finish Practice",
            command=self.root.destroy,
            width=25,
            height=2,
            font=(
                "Arial",
                11,
                "bold"
            ),
            bg="#374151",
            fg="white",
            relief="flat",
            cursor="hand2"
        )

        finish_button.pack(
            pady=8
        )

    # ==========================================
    # PROGRESS
    # ==========================================

    def show_progress(self):

        self.clear_screen()

        self.create_header(
            "📈 My Progress",
            "Track your English performance over time"
        )

        container = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        container.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=30
        )

        progress = (
            self.performance_service
            .get_daily_progress(
                self.user_id
            )
        )

        if not progress:

            label = tk.Label(
                container,
                text="No performance history found.",
                font=(
                    "Arial",
                    16
                ),
                bg=self.bg_color,
                fg=self.secondary_color
            )

            label.pack(
                pady=50
            )

            return

        # ==========================================
        # GROUP DATA
        # ==========================================

        daily_data = {}

        for record in progress:

            performance_date = record[0]

            activity_name = record[1]

            score = float(
                record[2]
            )

            if performance_date not in daily_data:

                daily_data[
                    performance_date
                ] = {}

            daily_data[
                performance_date
            ][activity_name] = score

        # ==========================================
        # TABLE
        # ==========================================

        table = self.create_card(
            container
        )

        table.pack(
            fill="x",
            pady=10
        )

        headers = [
            "Date",
            "Speaking",
            "Writing",
            "Overall"
        ]

        for column, header in enumerate(
            headers
        ):

            label = tk.Label(
                table,
                text=header,
                font=(
                    "Arial",
                    12,
                    "bold"
                ),
                bg=self.card_color,
                fg=self.text_color,
                width=18
            )

            label.grid(
                row=0,
                column=column,
                padx=5,
                pady=12
            )

        row = 1

        for performance_date, data in (
            daily_data.items()
        ):

            speaking = data.get(
                "speaking"
            )

            writing = data.get(
                "writing"
            )

            if (
                speaking is not None
                and writing is not None
            ):

                overall = (
                    speaking + writing
                ) / 2

            elif speaking is not None:

                overall = speaking

            elif writing is not None:

                overall = writing

            else:

                overall = 0

            values = [
                str(performance_date),

                (
                    f"{speaking:.0f}"
                    if speaking is not None
                    else "-"
                ),

                (
                    f"{writing:.0f}"
                    if writing is not None
                    else "-"
                ),

                f"{overall:.0f}"
            ]

            for column, value in enumerate(
                values
            ):

                label = tk.Label(
                    table,
                    text=value,
                    font=(
                        "Arial",
                        12
                    ),
                    bg=self.card_color,
                    fg=self.text_color,
                    width=18
                )

                label.grid(
                    row=row,
                    column=column,
                    padx=5,
                    pady=10
                )

            row += 1

        # ==========================================
        # BACK
        # ==========================================

        back_button = self.create_button(
            container,
            "⬅ Back to Performance",
            self.show_performance
        )

        back_button.pack(
            pady=25
        )

    # ==========================================
    # ERROR
    # ==========================================

    def show_error(
        self,
        message
    ):

        self.clear_screen()

        self.create_header(
            "⚠️ Error"
        )

        label = tk.Label(
            self.root,
            text=message,
            font=(
                "Arial",
                16
            ),
            bg=self.bg_color,
            fg=self.danger_color
        )

        label.pack(
            pady=80
        )

        button = self.create_button(
            self.root,
            "⬅ Back to Dashboard",
            self.show_timebox
        )

        button.pack()


# ==============================================
# RUN
# ==============================================

if __name__ == "__main__":

    Dashboard()