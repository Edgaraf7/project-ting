def exists_word(word, instance):
    result = []
    for item in instance.items:
        file_path = item["nome_do_arquivo"]
        occurrences = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for idx, line in enumerate(lines, start=1):
                if word.lower() in line.lower():
                    occurrences.append({"linha": idx})
        if occurrences:
            result.append({"palavra": word,
                           "arquivo": file_path, "ocorrencias": occurrences})
    return result  #


def search_by_word(word, instance):
    result = []
    for item in instance.items:
        file_path = item["nome_do_arquivo"]
        occurrences = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for idx, line in enumerate(lines, start=1):
                if word.lower() in line.lower():
                    occurrences.append({"linha": idx,
                                        "conteudo": line.strip()})
        if occurrences:
            result.append({"palavra": word,
                           "arquivo": file_path, "ocorrencias": occurrences})
    return result
