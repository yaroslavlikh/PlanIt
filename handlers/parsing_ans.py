def parse_answer(json_response):
    title = json_response.title
    start_date = json_response.start_date
    start_time = json_response.start_time
    end_time = json_response.end_time
    description = json_response.description
    type_of = json_response.type_of
    print(f'Добавляем новую задачу: {title}, {start_date}, {start_time}, {end_time}, {description}, {type_of}')

    return {
        "title": title,
        "start_date": start_date,
        "start_time": start_time,
        "end_time": end_time,
        "description": description,
        "type_of": type_of
    }