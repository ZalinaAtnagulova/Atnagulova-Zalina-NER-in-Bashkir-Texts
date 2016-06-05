Here we present you a parser that does NER on the morphologically structured and marked corpora of Bashkir texts similar to the Russian National Corpus and was tested on the Bashkir corpora by B. Orekhov.
Basic document in the corpora has following structure:

<?xml version="1.0" encoding="utf-8"?>
<html><head></head>
<body>
<se>
<w><ana lex="опубликов" morph="а,но" gr="S,dat,acc" trans="Опубликов"></ana>Опубликовано</w>
<w><ana lex="24" gr="NUM" trans="24"></ana>24</w>
<w><ana lex="август" morph="Ø" gr="S,nom,sg" trans="август"></ana>Август</w>,
<w><ana lex="2010" gr="NUM" trans="2010"></ana>2010</w>
<w>-</w>
<w><ana lex="15" gr="NUM" trans="15"></ana>15</w>:24.
</se>
<se>
<w><ana lex="автор" morph="Ø" gr="S,nom,sg" trans="автор"></ana>Автор</w>:
<w><ana lex="лилия" morph="Ø" gr="S,nom,sg" trans="Лилия"></ana>Лилия</w>
</se>
<se>
<w><ana lex="башҡортостан" morph="Ø" gr="S,nom,sg" trans="Башкортостан"></ana>Башҡортостан</w>
<w><ana lex="рес" gr="borrowed"></ana>Рес</w>­публикаһының
<w><ana lex="мәғариф" morph="Ø" gr="S,nom,sg" trans="образование"></ana>мәғариф</w>
<w><ana lex="алдынғы" morph="һы" gr="ADJ,poss.3sg" trans="передовой"></ana>алдынғыһы</w>,
<w><ana lex="юғары" morph="Ø" gr="ADJ,nom,sg" trans="высокий"></ana>юғары</w>
<w><ana lex="категориял?" morph="ы" gr="S,poss.3sg/pl" trans="?"></ana>категориялы</w>
<w><ana lex="уҡытыусы" morph="Ø" gr="S,nom,sg" trans="учитель"></ana><ana lex="уҡытыу" morph="сы" gr="S,clit.uncert" trans="обучение"></ana>уҡытыусы</w>.
</se>
</body>
</html> 

Where
- <?xml version="1.0" encoding="utf-8"?> a commented tipe of tag containing information about xml-file;
- <html> defines structural type of file, the root of an HTML document;
- <body> defines the document's body, a main working zone of the file;
- <se> defines sentences;
- <w> defines words;
- <ana> defines morphological information about the word with the attributes lex for 'lexeme', morph for 'morphemes', gr for 'grammatical meaning' of the word and trans for the 'translation' into Russian.

Our program defines named entities like first and second names <names> (bounded), dates <date> and geographical locations <geo> by adding corresponding tags to a single <w> tag or to groups of several <w> tags where necessary. 
The code is written in Python 3. The program does not require any manual guidance, only a set of files with the list of capitalised names (NamesCapitalised.txt), capitalised second names (SnamesCapitalised.txt), different geographical locations like names of cities, rivers, mountains etc. also capitalised (Cities.txt) and a folder with the Bashkir corpora (BashCorpus) all placed in the same directory with the starting file (NER_Bash.py).
All the resulting files would appear in a new folder called Recognised that would be created automatically. 
Note that there are 47 files with syntax errors. To parse them as well you need to edit them first using regular expressions or manually. 
We point out that our program does not provide a perfect recognition and requires further improvements. For any remarks and proposals feel free to contact: zalina2804@mail.ru