def ret_cal(el): # возвращение календарной задачи
    # el[0] - id, el[1] - user_id, el[2] - title, el[3] - start_time, el[4] - end_time, el[5] - description
    task_parts = []
    task_parts.append(f'Название: {el[2]}')
    if el[3] and str(el[3]).strip():  # start_time
        task_parts.append(f'Начало: {el[3]} в {el[4]}')
    if el[4] and str(el[4]).strip():  # end_time
        task_parts.append(f'Конец: {el[4]}')
    if el[5] and str(el[5]).strip():  # description
        task_parts.append(f'Описание: {el[5]}')
    print(task_parts, ', '.join(task_parts))
    return task_parts

def ret_task(el): # возвращение задачи
    task_parts = []
    task_parts.append(f'Название: {el[2]}')
    if el[5] and str(el[5]).strip():  # description
        task_parts.append(f'Описание: {el[5]}')
    if el[3] and str(el[3]).strip() and str(el[3]).strip():  # start_time
        task_parts.append(f'Когда надо сделать: {el[3]} в {el[4]}')
    elif el[3] and str(el[3]).strip():
        task_parts.append(f'Когда надо сделать: {el[3]}')
    print(task_parts, ', '.join(task_parts))
    return task_parts