def remove_excluded_ranges(original_ranges, excluded_ranges):
    import pdb;pdb.set_trace()
    original_ranges.sort()#[(2, 99), (50, 100), (150, 250), (200, 300)]
    excluded_ranges.sort()#[(10,50),(90,120),(135,160),(150,200)]

    merged_ranges = []
    i, j = 0, 0
    #2nd iteration i=1,j=0,merged_ranger=(2,9)
    while i < len(original_ranges):
        current_range = original_ranges[i]#(2,99),(50,100)

        while j < len(excluded_ranges) and excluded_ranges[j][1] < current_range[0]:
            j += 1

        if j < len(excluded_ranges) and excluded_ranges[j][0] <= current_range[1]:
            start = current_range[0]#2,50
            end = excluded_ranges[j][0] - 1#9,9

            if start <= end:
                merged_ranges.append((start, end))

            i += 1#1,2
            if excluded_ranges[j][1] >= current_range[1]:
                j += 1
        else:
            merged_ranges.append(current_range)
            i += 1

    return merged_ranges

# Test the function with the given example:
original_ranges = [(150, 250), (2, 99), (200, 300), (50, 100)]
excluded_ranges = [(10, 50), (135, 160), (90, 120), (150, 200)]
output_ranges = remove_excluded_ranges(original_ranges, excluded_ranges)
print("Output id ranges =", output_ranges)
#[(2, 9), (51, 89), (201, 300)]



