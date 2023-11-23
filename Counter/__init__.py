def bowling_score(throws:list[int], max_throw=10):
    def impl(throws, max_throw):
        if len(throws) < 4:
            return sum(throws)

        score = throws[0] + throws[1]
        throw_count = 2

        if score == max_throw or throws[0] == max_throw:
            score += throws[2]

            if throws[0] == max_throw:
                throw_count = 1

        return score + bowling_score(throws[throw_count:], max_throw)

    if any(run > max_throw for run in throws):
        raise ValueError(f"Some value exceeds the maximum value of {max_throw}")

    return impl(throws, max_throw)
