def ret_cal(el):
    task_parts = []

    task_parts.append(f'Название: {el["title"]}')

    if el["start_date"] and el["start_date"].strip():
        if el["start_time"] and el["start_time"].strip():
            task_parts.append(f'Начало: {el["start_date"]} в {el["start_time"]}')
        else:
            task_parts.append(f'Начало: {el["start_date"]}')

    if el["end_time"] and el["end_time"].strip():
        task_parts.append(f'Конец: {el["end_time"]}')

    if el["description"] and el["description"].strip():
        task_parts.append(f'Описание: {el["description"]}')

    print(task_parts, ', '.join(task_parts))
    return task_parts


def ret_task(el):
    task_parts = []

    task_parts.append(f'Название: {el["title"]}')

    if el["description"] and el["description"].strip():
        task_parts.append(f'Описание: {el["description"]}')

    if el["start_date"] and el["start_date"].strip():
        if el["start_time"] and el["start_time"].strip():
            task_parts.append(f'Когда надо сделать: {el["start_date"]} в {el["start_time"]}')
        else:
            task_parts.append(f'Когда надо сделать: {el["start_date"]}')

    print(task_parts, ', '.join(task_parts))
    return task_parts
