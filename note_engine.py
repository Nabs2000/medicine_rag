from llama_index.core.tools import FunctionTool
from pathlib import Path

note_file = Path('data/notes.txt')


def save_note(note):
    if not note_file.exists():
        note_file.touch()

    with open(note_file, 'a') as file:
        file.writelines([note, '\n'])

    return "note saved"


note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name='note_saver',
    description='Save a note to a file')
