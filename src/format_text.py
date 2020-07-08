import textwrap
import shutil


def format_text(text):
    return textwrap.fill(textwrap.dedent(text).strip(),
                         width=shutil.get_terminal_size().columns)
