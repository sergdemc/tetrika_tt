def merge_intervals(intervals):
    """Объединяет пересекающиеся интервалы."""
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return merged


def intersect_intervals(intervals1, intervals2):
    """Находит пересечение двух списков интервалов."""
    result = []
    i, j = 0, 0
    while i < len(intervals1) and j < len(intervals2):
        start1, end1 = intervals1[i]
        start2, end2 = intervals2[j]
        start = max(start1, start2)
        end = min(end1, end2)
        if start < end:
            result.append([start, end])
        if end1 < end2:
            i += 1
        else:
            j += 1
    return result


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = [[intervals['lesson'][0], intervals['lesson'][1]]]
    pupil_intervals = [[intervals['pupil'][i], intervals['pupil'][i + 1]] for i in range(0, len(intervals['pupil']), 2)]
    tutor_intervals = [[intervals['tutor'][i], intervals['tutor'][i + 1]] for i in range(0, len(intervals['tutor']), 2)]

    pupil_merged = merge_intervals(pupil_intervals)
    tutor_merged = merge_intervals(tutor_intervals)

    pupil_lesson = intersect_intervals(pupil_merged, lesson)
    tutor_lesson = intersect_intervals(tutor_merged, lesson)

    common_intervals = intersect_intervals(pupil_lesson, tutor_lesson)

    total_time = sum(end - start for start, end in common_intervals)
    return total_time
