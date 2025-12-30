def ret_cal(el):
    task_parts = []

    task_parts.append(f'Название: {el[0]}')

    if el[1] and el[1].strip():
        if el[2] and el[2].strip():
            task_parts.append(f'Начало: {el[1]} в {el[2]}')
        else:
            task_parts.append(f'Начало: {el[1]}')

    if el[3] and el[3].strip():
        task_parts.append(f'Конец: {el[3]}')

    if el[4] and el[4].strip():
        task_parts.append(f'Описание: {el[4]}')

    print(task_parts, ', '.join(task_parts))
    return task_parts


def ret_task(el):
    task_parts = []

    task_parts.append(f'Название: {el[0]}')

    if el[4] and el[4].strip():
        task_parts.append(f'Описание: {el[4]}')

    if el[1] and el[1].strip():
        if el[2] and el[2].strip():
            task_parts.append(f'Когда надо сделать: {el[1]} в {el[2]}')
        else:
            task_parts.append(f'Когда надо сделать: {el[1]}')

    print(task_parts, ', '.join(task_parts))
    return task_parts
