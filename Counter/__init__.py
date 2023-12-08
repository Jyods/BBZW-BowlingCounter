def bowling_score(throws:list[int], max_pins=10):
    """
    Calculate a bowling score
    :param throws: Array of how many pins were knocked over.
    :param max_pins: The amount of pins to be knocked over.
    """
    def impl(throws, max_pins):
        if len(throws) < 4:
            return sum(throws)

        score = throws[0] + throws[1]
        throw_count = 2

        if score == max_pins or throws[0] == max_pins:
            score += throws[2]

            if throws[0] == max_pins:
                throw_count = 1

        return score + bowling_score(throws[throw_count:], max_pins)

    if any(run > max_pins for run in throws):
        raise ValueError(f"Some value exceeds the maximum value of {max_pins}")

    return impl(throws, max_pins)
