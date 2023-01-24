def update_records(
    rec: dict[int, dict],
    id: int,
    attr: str,
    value: str
):
    data = rec.get(id)
    if data:
        if value == '':
            data.pop(attr, None)
        elif attr == 'tracks':
            data.setdefault('tracks', []).append(value)
        else:
            data[attr] = value
    return rec