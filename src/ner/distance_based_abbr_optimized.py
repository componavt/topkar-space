import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import pandas as pd
import re
import csv
from ast import Import
import nltk
import re
import time
from datetime import timedelta
from nltk.tokenize import sent_tokenize, word_tokenize

# Функция для загрузки сокращений из CSV файла
def load_abbreviations(csv_filename):
    """
    Загружает сокращения из CSV файла
    """
    print(f"⏳ Загрузка сокращений из {csv_filename}...")
    start_time = time.time()

    abbreviations = {}
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                full_name = row['Обозначение']
                short_forms_str = row['Сокращения']

                if short_forms_str:
                    # Разделяем по запятой и убираем пробелы
                    short_forms = [s.strip() for s in short_forms_str.split(',')]

                    for short in short_forms:
                        if short:
                            abbreviations[short] = full_name
                            print(f"Добавлено сокращение: '{short}' -> {full_name}")
    except Exception as e:
        print(f"Error loading abbreviations: {e}")
        # Альтернативный способ чтения если структура файла отличается
        try:
            with open(csv_filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    if ';' in line:
                        parts = line.strip().split(';')
                        if len(parts) >= 2:
                            full_name = parts[0].strip()
                            short_forms_str = parts[1].strip()
                            short_forms = [s.strip() for s in short_forms_str.split(',')]
                            for short in short_forms:
                                if short:
                                    abbreviations[short] = full_name
        except Exception as e2:
            print(f"Alternative loading also failed: {e2}")

    load_time = time.time() - start_time
    print(f" Загружено {len(abbreviations)} сокращений за {load_time:.2f} секунд")
    return abbreviations

# Функция для создания паттернов регулярных выражений
def create_abbreviation_patterns(abbreviations_dict):
    """
    Создает паттерны регулярных выражений для всех сокращений
    """
    print(f"🔧 Создание паттернов для {len(abbreviations_dict)} сокращений...")
    patterns = {}

    for short_form, full_name in abbreviations_dict.items():
        if '.' in short_form:
            # Для сокращений с точкой: ищем с точкой, после которой может быть пробел или конец строки
            pattern = r'\b' + re.escape(short_form) + r'(?=\s|$|\.|,|;)'
        else:
            # Для сокращений без точки: обычный поиск с границами слов
            pattern = r'\b' + re.escape(short_form) + r'\b'
        patterns[short_form] = (pattern, full_name)

    print(f" Паттерны созданы для {len(patterns)} сокращений")
    return patterns

# Функция для поиска сокращений в окрестности топонима
def find_nearby_abbreviations(text, toponym, patterns, distance_words=2):
    """
    Ищет сокращения в окрестности топонима используя предварительно созданные паттерны
    """
    search_start_time = time.time()
    nearby_abbreviations = []

    # Находим все вхождения топонима в тексте
    toponym_search_start = time.time()
    toponym_pattern = re.escape(toponym)
    toponym_matches = list(re.finditer(toponym_pattern, text))
    toponym_search_time = time.time() - toponym_search_start
    print(f"    Поиск топонима '{toponym}': {toponym_search_time:.4f} сек, найдено {len(toponym_matches)} вхождений")

    for toponym_match in toponym_matches:
        toponym_start = toponym_match.start()
        toponym_end = toponym_match.end()

        # Определяем окрестность вокруг топонима (в символах)
        # Приблизительно: считаем что в среднем слово = 6 символов + пробел
        approx_distance_chars = distance_words * 7

        search_start = max(0, toponym_start - approx_distance_chars)
        search_end = min(len(text), toponym_end + approx_distance_chars)

        search_area = text[search_start:search_end]

        # Ищем все сокращения в этой области
        abbreviation_search_start = time.time()
        for short_form, (pattern, full_name) in patterns.items():
            abbreviation_matches = list(re.finditer(pattern, search_area))

            for abbr_match in abbreviation_matches:
                # Вычисляем абсолютную позицию сокращения в тексте
                abbr_absolute_pos = search_start + abbr_match.start()

                # Проверяем что сокращение не является частью самого топонима
                if not (toponym_start <= abbr_absolute_pos <= toponym_end):
                    abbr_info = {
                        'abbreviation': abbr_match.group(),
                        'full_name': full_name,
                        'position': abbr_absolute_pos,
                        'context': search_area
                    }

                    # Проверяем на дубликаты
                    is_duplicate = False
                    for existing in nearby_abbreviations:
                        if (existing['abbreviation'] == abbr_info['abbreviation'] and
                            existing['full_name'] == abbr_info['full_name'] and
                            abs(existing['position'] - abbr_info['position']) < 10):
                            is_duplicate = True
                            break

                    if not is_duplicate:
                        nearby_abbreviations.append(abbr_info)

        abbreviation_search_time = time.time() - abbreviation_search_start
        print(f"    Поиск сокращений вокруг '{toponym}': {abbreviation_search_time:.4f} сек")

    total_search_time = time.time() - search_start_time
    if nearby_abbreviations:
        print(f"    Найдено {len(nearby_abbreviations)} сокращений за {total_search_time:.4f} сек")
    else:
        print(f"    Сокращения не найдены за {total_search_time:.4f} сек")

    return nearby_abbreviations

def main(max_lines):
    """
    Основная функция с ограничением количества строк

    Args:
        max_lines (int): Максимальное количество строк для обработки. Если None - обрабатывает все.
    """
    total_start_time = time.time()

    # Загружаем сокращения
    abbreviations_dict = load_abbreviations('abbreviations.csv')

    # Создаем паттерны регулярных выражений один раз для всех вызовов
    patterns_creation_start = time.time()
    patterns = create_abbreviation_patterns(abbreviations_dict)
    patterns_creation_time = time.time() - patterns_creation_start
    print(f"⏱ Общее время создания паттернов: {patterns_creation_time:.4f} сек")

    lines = df['main_text'].tolist()
    print(f"\n Всего предложений в данных: {len(lines)}")

    # Применяем ограничение по количеству строк
    if max_lines is not None:
        lines = lines[:max_lines]
        print(f" Обрабатывается только первых {max_lines} строк")

    df['main_text'] = df['main_text'].replace({float('nan'): ""})

    num = 0
    output_csv = 'output.csv'

    # Статистика
    total_toponyms = 0
    total_abbreviations = 0
    processed_sentences = 0

    # Время для статистики
    total_toponym_time = 0
    total_abbreviation_time = 0
    total_nlp_time = 0

    print(f"\n Начало обработки {len(lines)} предложений...")
    processing_start_time = time.time()

    with open(output_csv, 'w', encoding='utf-8') as outfile:
        outfile.writelines(f"sentence_id; toponyms_list; nearby_abbreviations \n")

        # ОПТИМИЗАЦИЯ: обрабатываем предложения батчами для лучшей производительности
        batch_size = 100  # Можно настроить в зависимости от объема памяти

        for i in range(0, len(lines), batch_size):
            batch_lines = lines[i:i + batch_size]
            batch_indices = list(range(i, min(i + batch_size, len(lines))))

            print(f"\n--- Обработка батча {i//batch_size + 1}/{(len(lines)-1)//batch_size + 1} ---")

            # Обрабатываем батч предложений
            nlp_start_time = time.time()
            
            # Фильтруем пустые строки перед передачей в bulk_process
            non_empty_lines = [(idx, text) for idx, text in enumerate(batch_lines) if pd.notna(text) and text != ""]
            if non_empty_lines:
                # Разделяем индексы и тексты
                non_empty_indices, non_empty_texts = zip(*non_empty_lines)
                
                # Выполняем bulk_process только для непустых текстов
                batch_docs = nlp.bulk_process(non_empty_texts)
                
                # Воссоздаем полный список документов, включая None для пустых строк
                batch_docs_full = [None] * len(batch_lines)
                for idx, doc in zip(non_empty_indices, batch_docs):
                    batch_docs_full[idx] = doc
            else:
                batch_docs_full = [None] * len(batch_lines)
                
            batch_docs = batch_docs_full
            batch_nlp_time = time.time() - nlp_start_time
            total_nlp_time += batch_nlp_time
            print(f"⏱ Время NLP обработки батча: {batch_nlp_time:.4f} сек")

            # Обрабатываем каждый документ в батче
            for j, (doc, sentence_idx) in enumerate(zip(batch_docs, batch_indices)):
                sentence = batch_lines[j]

                if doc is None:
                    # Пустая строка
                    strk = f"{sentence_idx}; ; \n"
                    outfile.writelines(strk)
                    num += 1
                    continue

                sentence_start_time = time.time()

                print(f'\n--- Предложение {sentence_idx} ---')
                print(f'Текст: {sentence[:100]}...' if len(sentence) > 100 else f'Текст: {sentence}')

                sentence_toponyms = []
                all_nearby_abbreviations = []

                # Поиск топонимов в предобработанном документе
                toponym_search_start = time.time()
                for entity in doc.ents:
                    if entity.type == "LOC":
                        entity_find_time = time.time() - toponym_search_start
                        print(f'📍 Топоним: {entity.text} (найден за {entity_find_time:.4f} сек)')
                        sentence_toponyms.append(entity.text)
                        total_toponyms += 1

                        # Обновляем время для следующего топонима
                        toponym_search_start = time.time()

                        # Ищем сокращения в окрестности этого топонима
                        abbreviation_search_start = time.time()
                        nearby_abbr = find_nearby_abbreviations_advanced(
                            sentence,
                            entity.text,
                            patterns,
                            distance_words=5
                        )
                        abbreviation_time = time.time() - abbreviation_search_start
                        total_abbreviation_time += abbreviation_time

                        print(f"    Общее время поиска сокращений для '{entity.text}': {abbreviation_time:.4f} сек")

                        for abbr_info in nearby_abbr:
                            match_str = f"{abbr_info['abbreviation']}"
                            if match_str not in all_nearby_abbreviations:
                                all_nearby_abbreviations.append(match_str)
                                total_abbreviations += 1
                                print(f"    Найдено сокращение: '{abbr_info['abbreviation']}' -> '{abbr_info['full_name']}'")

                # Если не было найдено топонимов, выводим время поиска
                if not sentence_toponyms:
                    toponym_time = time.time() - toponym_search_start
                    total_toponym_time += toponym_time
                    print(f" Время поиска топонимов: {toponym_time:.4f} сек (не найдено)")

                # Формируем строку для вывода
                toponyms_str = ', '.join(sentence_toponyms)
                abbreviations_str = ', '.join(all_nearby_abbreviations)

                strk = f"{sentence_idx}; {toponyms_str}; {abbreviations_str} \n"
                outfile.writelines(strk)

                sentence_time = time.time() - sentence_start_time
                print(f" Общее время обработки предложения: {sentence_time:.2f} сек")

                processed_sentences += 1
                num += 1

            # Прогресс после каждого батча
            elapsed = time.time() - processing_start_time
            print(f"\n Прогресс: обработано {processed_sentences}/{len(lines)} предложений")
            print(f" Прошло времени: {timedelta(seconds=int(elapsed))}")

            # Среднее время по этапам
            if processed_sentences > 0:
                avg_nlp_time = total_nlp_time / processed_sentences
                if total_toponyms > 0:
                    avg_abbr_time = total_abbreviation_time / total_toponyms
                    print(f" Среднее время поиска сокращений на топоним: {avg_abbr_time:.4f} сек")

                print(f" Среднее время NLP: {avg_nlp_time:.4f} сек")

                avg_time = elapsed / processed_sentences
                remaining = (len(lines) - processed_sentences) * avg_time
                print(f" Оставшееся время: ~{timedelta(seconds=int(remaining))}")

    total_time = time.time() - total_start_time

    # Финальная статистика с детализацией по времени
    print(f"\n ОБРАБОТКА ЗАВЕРШЕНА!")
    print(f" Статистика:")
    print(f"   - Обработано предложений: {processed_sentences}")
    print(f"   - Найдено топонимов: {total_toponyms}")
    print(f"   - Найдено сокращений: {total_abbreviations}")
    print(f"   - Общее время: {timedelta(seconds=int(total_time))}")

    if processed_sentences > 0:
        print(f"\n⏱ Детализация времени:")
        print(f"   - Среднее время на предложение: {total_time/processed_sentences:.2f} сек")
        print(f"   - Общее время NLP: {timedelta(seconds=int(total_nlp_time))}")
        print(f"   - Среднее время NLP на предложение: {total_nlp_time/processed_sentences:.4f} сек")
        print(f"   - Время создания паттернов: {patterns_creation_time:.4f} сек")

        if total_toponyms > 0:
            print(f"   - Среднее время поиска сокращений на топоним: {total_abbreviation_time/total_toponyms:.4f} сек")
            print(f"   - Среднее количество топонимов на предложение: {total_toponyms/processed_sentences:.2f}")
            print(f"   - Среднее количество сокращений на топоним: {total_abbreviations/max(total_toponyms, 1):.2f}")

    print(f"   - Результаты сохранены в: {output_csv}")
# Альтернативная версия с более точным поиском по словам
def find_nearby_abbreviations_advanced(text, toponym, patterns, distance_words=2):
    """
    Улучшенная версия поиска с учетом расстояния в словах
    """
    search_start_time = time.time()
    nearby_abbreviations = []

    # Токенизируем текст с сохранением позиций
    tokenization_start = time.time()
    words_with_positions = []
    pattern = r'\b\w+(?:\.\w+)*\b|[^\w\s]'
    for match in re.finditer(pattern, text):
        word = match.group()
        if word.strip():  # Игнорируем чистые пробелы
            words_with_positions.append({
                'word': word,
                'start': match.start(),
                'end': match.end()
            })
    tokenization_time = time.time() - tokenization_start
    print(f"    Токенизация текста: {tokenization_time:.4f} сек")

    # Находим позиции топонима
    toponym_search_start = time.time()
    toponym_positions = []
    for i, word_info in enumerate(words_with_positions):
        # Проверяем отдельные слова и комбинации слов для топонима
        if word_info['word'] in toponym:
            # Простая проверка - можно улучшить для многословных топонимов
            toponym_positions.append(i)
    toponym_search_time = time.time() - toponym_search_start
    print(f"    Поиск позиций топонима: {toponym_search_time:.4f} сек, найдено {len(toponym_positions)} позиций")

    # Для каждой позиции топонима ищем соседние сокращения
    abbreviation_search_start = time.time()
    for pos in toponym_positions:
        start_idx = max(0, pos - distance_words)
        end_idx = min(len(words_with_positions), pos + distance_words + 1)

        for i in range(start_idx, end_idx):
            word_info = words_with_positions[i]
            word = word_info['word']

            # Проверяем является ли слово сокращением
            for short_form, (pattern, full_name) in patterns.items():
                # Сравниваем с очищенной версией сокращения
                clean_short = short_form.replace('.', '')
                clean_word = word.replace('.', '')

                if clean_word == clean_short:
                    abbr_info = {
                        'abbreviation': word,
                        'full_name': full_name,
                        'position': word_info['start']
                    }

                    # Проверяем на дубликаты
                    is_duplicate = False
                    for existing in nearby_abbreviations:
                        if (existing['abbreviation'] == abbr_info['abbreviation'] and
                            existing['full_name'] == abbr_info['full_name']):
                            is_duplicate = True
                            break

                    if not is_duplicate:
                        nearby_abbreviations.append(abbr_info)

    abbreviation_search_time = time.time() - abbreviation_search_start
    total_search_time = time.time() - search_start_time

    print(f"    Поиск сокращений: {abbreviation_search_time:.4f} сек")
    if nearby_abbreviations:
        print(f"    Расширенный поиск: найдено {len(nearby_abbreviations)} сокращений за {total_search_time:.4f} сек")
    else:
        print(f"    Расширенный поиск: сокращения не найдены за {total_search_time:.4f} сек")

    return nearby_abbreviations

# Запуск основной функции
if __name__ == "__main__":
    # Обработать только первые 50 строк для тестирования
    #main(max_lines=100)

    # Или обработать все строки:
    main(None)