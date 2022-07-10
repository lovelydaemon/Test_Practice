from dataclasses import dataclass


@dataclass
class Interval:
    start: int
    end: int


def are_intersect(lesson: Interval, interval: Interval) -> bool:
    """Return True if interval intersects lesson"""
    start = max(lesson.start, interval.start)
    end = min(lesson.end, interval.end)
    return end - start >= 0


def filter_interval(lesson: Interval, intervals: list[Interval]) -> list[Interval]:
    """Return the list of intervals that intersect lesson"""
    return [interval for interval in intervals if are_intersect(lesson, interval)]


def transform(intervals: list) -> list[Interval]:
    """Return transformed list of intervals"""
    new_intervals = []
    for index, value in enumerate(intervals):
        if index % 2 == 1:
            new_intervals.append(Interval(intervals[index-1], value))
    return new_intervals


def appearance(intervals):
    lesson = Interval(intervals['lesson'][0], intervals['lesson'][1])
    tutor = transform(intervals['tutor'])
    pupil = transform(intervals['pupil'])

    tutor = filter_interval(lesson, tutor)
    pupil = filter_interval(lesson, pupil)

    total = 0
    for p_item in pupil:
        for t_item in tutor:
            min_point = max(lesson.start, p_item.start, t_item.start)
            max_point = min(lesson.end, p_item.end, t_item.end)
            length = max_point - min_point
            if length > 0:
                total += length

    return total


tests = [
    {'data': {
        'lesson': [1594663200, 1594666800],
        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
        'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        },
        'answer': 3117
    },

    # Убрал кривые интервалы из pupil
    {'data': {
        'lesson': [1594702800, 1594706400],
        'pupil': [
                1594704512, 1594704513, 1594704564, 1594705150,
                1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875,
                ],
        'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
        },
    'answer': 1752
    },
    {'data': {
        'lesson': [1594692000, 1594695600],
        'pupil': [1594692033, 1594696347],
        'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
        },
    'answer': 3565
    },

    # Здесь дата сохранена в изначальном состоянии, но отсортирован pupil,
    # Потому что интервалы идут не по порядку
    {'data': {
        'lesson': [1594702800, 1594706400],
        'pupil': [
            1594702789, 1594702807, 1594704500, 1594704512,
            1594704513, 1594704542, 1594704564, 1594704581,
            1594704582, 1594704734, 1594705009, 1594705095,
            1594705096, 1594705106, 1594705150, 1594705158,
            1594705773, 1594705849, 1594706480, 1594706480,
            1594706500, 1594706502, 1594706503, 1594706524,
            1594706524, 1594706579, 1594706641, 1594706875],
        'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
        },
    'answer': 397
    },
]


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        print(test_answer)
        assert test_answer == test['answer'], f'Error on test case {i},got {test_answer}, expected {test["answer"]}'
