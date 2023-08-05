def remove_excluded_ranges(original_ranges, excluded_ranges):
    """
    Removes all the excluded ranges from the original ranges and returns a filtered list of ranges.
    Args:
        original_ranges: A list of tuples representing the original id ranges.
        excluded_ranges: A list of tuples representing the excluded id ranges.
    Returns:
        A filtered list of the original id ranges that do not overlap with any of the excluded ranges.
    """
    # Check if the input parameters are valid.
    if not original_ranges:
        return []
    if not excluded_ranges:
        return original_ranges
    # Iterate over the original ranges and check if they overlap with any of the excluded ranges.
    filtered_ranges = []
    for original_range in original_ranges:
        min_original = original_range[0]
        max_original = original_range[1]
        for excluded_range in excluded_ranges:
            min_excluded = excluded_range[0]
            max_excluded = excluded_range[1]
            if min_original <= max_excluded and min_excluded <= max_original:
                # The original range overlaps with the excluded range. Discard the original range.
                continue
            elif min_original < min_excluded:
                # The original range is before the excluded range. Add the original range to the filtered list.
                filtered_ranges.append(original_range)
            elif max_original > max_excluded:
                # The original range is after the excluded range. Add the original range to the filtered list.
                filtered_ranges.append(original_range)
    return filtered_ranges

original_id_ranges = [(150,250),(2,99),(200,300),(50,100)]
excluded_id_ranges = [(10,50),(135,160),(90,120),(150,200)]
filtered_id_ranges = remove_excluded_ranges(original_id_ranges, excluded_id_ranges)
print("Filtered ID Ranges:", filtered_id_ranges)