#/usr/bin/python3
from logging import error
from gtts import gTTS
from pathlib import Path
import argparse
import sys
import urllib


class ConvertTTS():
  def __init__(self) -> None:
    self._text_folder = Path('articles-text')
    self._mp3_folder = Path('articles-mp3')
    self._tld = 'com'
    # Check available domains
    url = 'https://www.google.com/supported_domains'
    with urllib.request.urlopen(url) as lines:
      domains = lines.readlines()
    self._domains_suff = list()
    for domain in domains:
      domain = domain.decode('utf-8')
      domain = domain.replace('.google.', '')
      domain = domain.replace('\n', '')
      self._domains_suff.append(domain)
    # print(domains_suff)

      
  def scan_text_folder(self):
    self._txt_files = self._text_folder.glob('**/*.txt')
    print('Input article files in folder {}:'.format(self._text_folder))
    # print([f.name for f in self.txt_files])

  def convert_save_TTS(self):
    for file in self._txt_files:
      print('Converting file {}'.format(file))
      with file.open() as f:
        read_txt = f.read()
        # print(read_txt)
        tts = gTTS(read_txt, tld=self._tld, slow=False)
        tts.save((self._mp3_folder / file.stem).with_suffix('.mp3'))

  def set_input_folder(self, input_folder):
    try:
      input_folder = Path(input_folder)
      if input_folder.is_dir():
        print('Setting input folder to {}'.format(input_folder))
        self._text_folder = input_folder
      else:
        sys.exit('Input not a folder!')
    except Exception as e:
      print('Input not a valid string!', e)

  def set_output_folder(self, output_folder):
    try:
      output_folder = Path(output_folder)
      if output_folder.is_dir():
        print('Setting output folder to {}'.format(output_folder))
        self._mp3_folder = output_folder
      else:
        sys.exit('Output not a folder!')
    except Exception as e:
      print('Output not a valid string!', e)

  def set_domain(self, domain):
    try:
      domain = str(domain)
      if domain in self._domains_suff:
        print('Setting domain to {}'.format(domain))
        self._tld = str(domain)
      else:
        raise Exception('Selected domain not valid! Check: '
                        'https://www.google.com/supported_domains')
    except Exception as e:
      sys.exit(e)
      

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-in', '--input', help='input folder(default: articles-text)')
  parser.add_argument('-out', '--output', help='output folder (default: articles-mp3)')
  parser.add_argument('-d', '--domain', help='Google domain (default: com)')
  args = parser.parse_args()

  Converter = ConvertTTS()
  if args.input:
    Converter.set_input_folder(input_folder=args.input)
  if args.output:
    Converter.set_output_folder(output_folder=args.output)
  if args.domain:
    Converter.set_domain(domain=args.domain)
      
  # Scan input folder
  Converter.scan_text_folder()
  # Convert .txt files to mp3
  Converter.convert_save_TTS()

  