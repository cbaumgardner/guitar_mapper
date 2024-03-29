import math
from typing import Dict, List, NewType, Union, Optional

# Type alias
ScaleTypes = NewType('ScaleTypes', List[Dict[str, Union[str, List[int]]]])
KeyNotes = NewType('KeyNotes', List[Dict[str, str]])

class ScaleChartConfig:
    def __init__(self):
        self.scale_types: ScaleTypes = [{"type": "Major (Ionian)", "scale_steps": [2, 2, 1, 2, 2, 2, 1]},
                    {"type": "Minor (Aeolian)", "scale_steps": [2, 1, 2, 2, 1, 2, 2]},
                    {"type": "Major Pentatonic", "scale_steps": [2, 2, 3, 2, 3]},
                    {"type": "Minor Pentatonic", "scale_steps": [3, 2, 2, 3, 2]},
                    {"type": "Dorian", "scale_steps": [2, 1, 2, 2, 2, 1, 2]},
                    {"type": "Phrygian", "scale_steps": [1, 2, 2, 2, 1, 2, 2]},
                    {"type": "Lydian", "scale_steps": [2, 2, 2, 1, 2, 2, 1]},
                    {"type": "Mixolydian", "scale_steps": [2, 2, 1, 2, 2, 1, 2]},
                    {"type": "Locrian", "scale_steps": [1, 2, 2, 1, 2, 2, 2]}]
        self.key_notes: KeyNotes = [{"key": "A", "key_display": "A"},
                    {"key": "A#", "key_display": "A♯ / B♭"},
                    {"key": "B", "key_display": "B"},
                    {"key": "C", "key_display": "C"},
                    {"key": "C#", "key_display": "C♯ / D♭"},
                    {"key": "D", "key_display": "D"},
                    {"key": "D#", "key_display": "D♯ / E♭"},
                    {"key": "E", "key_display": "E"},
                    {"key": "F", "key_display": "F"},
                    {"key": "F#", "key_display": "F♯ / G♭"},
                    {"key": "G", "key_display": "G"},
                    {"key": "G#", "key_display": "G♯ / A♭"}]
        self.notes: List[str] = [d["key"] for d in self.key_notes]
        self.inlay_frets: List[int] = [3, 5, 7, 9, 12, 15, 17, 19, 21]

    @property
    def scale_types(self) -> ScaleTypes:
        return self._scale_types

    @scale_types.setter
    def scale_types(self, value: KeyNotes):
        self._scale_types = value

    @property
    def key_notes(self) -> KeyNotes:
        return self._key_notes

    @key_notes.setter
    def key_notes(self, value: KeyNotes):
        self._key_notes = value

    @property
    def notes(self) -> List[str]:
        return self._notes

    @notes.setter
    def notes(self, value: List[str]):
        self._notes = value

    @property
    def inlay_frets(self) -> List[int]:
        return self._inlay_frets

    @inlay_frets.setter
    def inlay_frets(self, value: List[int]):
        self._inlay_frets = value


class FretBoard:
    """Representation of a guitar neck used to render scale-chart.com

    Attributes:
        config (ScaleChartConfig): Configuration settings from ScaleChartConfig.
        fret_num (int): Number of frets to draw. Default to 22.
        fret_width (int): How many characters wide a fret is. Defaults to 7.
        tuning (dict[int, str]): Defaults to standard (EADGBE).
        neck (dict[int, str]): Dictionary that holds the HTML for each string.
        scale (list[str]): List of notes in the scale.
        scale_type (str): Name of the type of scale.
        key_note (str): Root note for the scale.

    Raises:
        Exception: If the given key_note is not a recognized note in key_notes.

    """
    def __init__(self, key_note: Optional[str]=None, scale_type: Optional[str]=None, fret_num: int=22):
        self.config = ScaleChartConfig()
        self.fret_num = fret_num
        self.fret_width = 7
        self.tuning = {
            1: "E",
            2: "B",
            3: "G",
            4: "D",
            5: "A",
            6: "E"
        }
        self.neck = {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        }
        self.scale = []
        if scale_type is None:
            self.scale_type = self.config.scale_types[0]["type"]
        else: 
            self.scale_type = scale_type

        if key_note is None:
            self.key_note = self.config.notes[0]
        elif key_note in self.config.notes:
            self.key_note = key_note
        else:
            raise Exception("Invalid root note")

    def draw_neck(self) -> Dict[int, str]:
        """Renders HTML for each string on the guitar neck.

        Returns:
            dict[int, str]: Dictionary containing each string number as a key and the string's HTML as the value.
        """
        
        self.scale = self._compile_scale()

        for string in self.neck:
            self.neck[string] = self._get_tuning_html(self.tuning[string])

        current_fret = 0
        while current_fret < self.fret_num:
            for string in self.neck:
                # determine current note
                open_note = self.tuning[string]
                open_note_index = self.config.notes.index(open_note)
                current_note = self.config.notes[(open_note_index + current_fret + 1
                                      ) % len(self.config.notes)]

                # add to string
                string_so_far = self.neck[string]
                updated_neck = string_so_far + self._create_string_tab(current_fret, current_note)
                self.neck[string] = updated_neck

            current_fret += 1
        
        return self.neck

    def _create_string_tab(self, fret: int, note: str) -> str:
        """Sets attribute flags and returns HTML generated by _get_string_tab_html.

        Args:
            fret (int): The fret position to create the tab for.
            note (str): The note assigned to the fret.

        Returns:
            str: HTML for the string's tab.
        """
        is_note = False
        is_root = False
        is_inlay = False

        if note in self.scale:
            if note == self.scale[0]:
                is_note = True
                is_root = True
            else:
                is_note = True
        if fret + 1 in self.config.inlay_frets:
            is_inlay = True

        return self._get_string_tab_html(note, is_note, is_root, is_inlay)

    def _compile_scale(self) -> List[str]:
        """Determines the notes in the scale for the fretboard's key.

        Returns:
            List[str]: List of notes in the scale.
        """

        scale_dict = [x for x in self.config.scale_types if x["type"] == self.scale_type][0]
        scale_steps = scale_dict["scale_steps"]

        scale = [self.key_note]

        i = 0
        while i < len(scale_steps):
            current_note_index = self.config.notes.index(scale[i])
            next_step = scale_steps[i]
            next_note = self.config.notes[(current_note_index + next_step) % len(self.config.notes)]
            scale.append(next_note)
            i += 1

        return scale

    def _add_inlay_markers(self):
        """ Adds bullets below inlay frets (not currently used)."""

        inlay_list = ["&nbsp;"] * ((self.fret_width * self.fret_num) + (self.fret_num + 1))
        for inlay in self.config.inlay_frets:
            position = math.trunc(self.fret_width * (inlay - 0.5)) + inlay
            inlay_list[position] = "&bull;"
        inlay_markers = "".join(inlay_list)
        self.neck[7] = inlay_markers

    def _get_tuning_html(self, note: str) -> str:
        """Renders HTML for the guitar's open strings.

        Args:
            note (str): Root note for the scale.

        Returns:
            str: HTML for the guitars tuning (open notes).
        """

        # Should probably change this to use flags like Corey's
        html = '<span class="string-tuning'
        if note in self.scale:
            html = html + ' note'
        if note == self.scale[0]:
            html = html + ' root'
        html = html + '">'

        if note in self.scale:
            html = html + '<span class="note-indicator">' + note + '</span>'
        else:
            html = html + note

        html = html + '</span>'

        return html

    @staticmethod
    def _get_string_tab_html(note: str, is_note: bool, is_root: bool, is_inlay: bool) -> str:
        """Builds HTML for a fret position on one of the guitar's strings.

        Args:
            note (str): The note for the fret.
            is_note (bool): Note is in the scale and should be rendered.
            is_root (bool): Note is the root note of the scale.
            is_inlay (bool): Fret contains an inlay to be rendered.

        Returns:
            str: HTML for the string's fret position tab.
        """
        html = '<span class="string-tab'
        if is_note:
            html = html + ' note'
        if is_root:
            html = html + ' root'
        if is_inlay:
            html = html + ' inlay'
        html = html + '">'

        if is_note:
            html = html + '<span class="note-indicator">' + note + '</span>'
        else:
            html = html + '&nbsp;'
        html = html + '</span>'
        return html
