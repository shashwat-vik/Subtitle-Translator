# Subtitle-Translator

Struck in documentry/movie due to no desired language subtitle ?
Above script converts any language subtitle to English.
As the Google Translate API service is not free, Selenium is leveraged as a hack.

Below are the requiremnts for the script:
  - Python 3.x
  - Selenium
  - Firefox Browser.
  
Currently verified only on the SubRip (.srt)

**Working on 2 improvements:**
  1. For large subtitle file, it can take time to translate. Will add threading.
  2. When a sentence is distributed in multiple time slot in the subtitle file, the contextual meaning is lost as the translation is done per line basis. The main bottleneck being the fact that the translated text needs to be put in the same time slot. Will concetanate, and breakdown translation based on initial word weight of each slot.


##RUN
`python main.py <file_path>`

TEST : 
`python main.py test/portuguese_subs.srt`
