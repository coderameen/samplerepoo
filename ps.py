def remove_excluded_ranges(original_ranges, excluded_ranges):
    import pdb;pdb.set_trace()
    filtered_ranges = []

    for orig_range in original_ranges:
        for excluded_range in excluded_ranges:
            # Check if the current original range overlaps with any excluded range
            if orig_range[1] < excluded_range[0] or orig_range[0] > excluded_range[1]:
                continue  # Ranges do not overlap, move to the next excluded range
            else:
                # Handle the overlapping cases between original and excluded ranges
                if orig_range[0] >= excluded_range[0] and orig_range[1] <= excluded_range[1]:
                    break  # Completely covered by excluded range, skip this original range
                elif orig_range[0] >= excluded_range[0]:
                    orig_range = (excluded_range[1] + 1, orig_range[1])  # Adjust start of original range
                elif orig_range[1] <= excluded_range[1]:
                    orig_range = (orig_range[0], excluded_range[0] - 1)  # Adjust end of original range
                else:
                    filtered_ranges.append((orig_range[0], excluded_range[0] - 1))
                    orig_range = (excluded_range[1] + 1, orig_range[1])
        
        filtered_ranges.append(orig_range)

        sorted_ranges = sorted(filtered_ranges, key=lambda x: x[0])

    output = [sorted_ranges[0]]

    for current_range in sorted_ranges[1:]:
        last_range = output[-1]

        if current_range[0] <= last_range[1]:
            merged_range = (last_range[0], max(current_range[1], last_range[1]))
            output[-1] = merged_range
        else:
            output.append(current_range)

    return output
    
        
    # return filtered_ranges





# Example usage:
original_id_ranges = [(150, 250), (2, 99), (200, 300), (50, 100)]
excluded_id_ranges = [(10, 50), (135, 160), (90, 120), (150, 200)]
output_id_ranges = remove_excluded_ranges(original_id_ranges, excluded_id_ranges)
print(output_id_ranges)