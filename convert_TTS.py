#/usr/bin/python3
from gtts import gTTS
import glob
from pathlib import Path, WindowsPath

class ConvertTTS():
  def __init__(self) -> None:
    self.text_folder = Path('articles-text')
    self.mp3_folder = Path('articles-mp3')
      
  def scan_text_folder(self):
    self.txt_files = self.text_folder.glob('**/*.txt')
    print('Input article files in folder {}'.format(self.text_folder))
    # print([f.name for f in self.txt_files])

  def convert_save_TTS(self):
    for file in self.txt_files:
      print('Opening file {}'.format(file))
      with file.open() as f:
        lines = ' '.join(f.readlines())
        # print(lines)
        tts = gTTS(lines, slow=True)
        tts.save((self.mp3_folder / file.stem).with_suffix('.mp3'))

if __name__ == '__main__':
  Converter = ConvertTTS()
  Converter.scan_text_folder()
  Converter.convert_save_TTS()

  