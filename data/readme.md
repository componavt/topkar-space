# ParaNames
## paranames.tsv.gz
Многоязычный параллельный ресурс имен использующий Wikidata как источник. <br >
Словарь имеет следующие стобцы: <br >
- wikidata_id - id в ресурсе wikidata <br >
- eng - написание именованной сущности на английском <br >
- label - написание именованной сущности на языке указанном в столбце language <br >
- language - язык написания название топонима <br >
- type - тип именованной сущности (PER/LOC/ORG)<br >
[paranames.tsv.gz](https://github.com/bltlab/paranames/releases/download/v2024.05.07.0/paranames.tsv.gz) <br >
## paranames_fi.csv
paranames_fi.csv - файл представляет собой структурированный набор именованных сущностей содержащих "fi" - финский язык, в столбце language и "LOC" - локация, в столбце type , автоматически извлечённых из словаря ParaNames с использованием скрипта, реализованного в <br >
[topkar-space/src/ner/paranames_pars.ipynb.](https://github.com/componavt/topkar-space/blob/main/src/ner/nltk-ru-ner.ipynb)<br >
## paranames_ru.csv
paranames_ru.csv - файл представляет собой структурированный набор именованных сущностей содержащих "ru" - русский язык, в столбце language и "LOC" - локация, в столбце type , автоматически извлечённых из словаря ParaNames с использованием скрипта, реализованного в<br >
[topkar-space/src/ner/paranames_pars.ipynb.](https://github.com/componavt/topkar-space/blob/main/src/ner/nltk-ru-ner.ipynb)
## References
[ParaNames 1.0: Creating an Entity Name Corpus for 400+ Languages using Wikidata](https://arxiv.org/abs/2405.09496)
