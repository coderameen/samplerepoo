def my_sorted_function(original_id_ranges, excluded_id_ranges):
    ranges = []
    #original_ranges = [(150, 250), (2, 99), (200, 300), (50, 100)]
    #excluded_ranges = [(10, 50), (135, 160), (90, 120), (150, 200)]
    for x in original_id_ranges:
        #X 1st iteration: x=(150,250)
        #X 2nd iteration: x=(2, 99)
        #X 3rd iteration: x=(200,300)
        #X 4th iteration: x=(50, 100)
        for y in excluded_id_ranges:
            #Y 1st iteration: x=(150,250),y=(10,50)
            #Y 2st iteration: x=(150,250),y=(135,160)
            #Y 3rd iteration: x=(161,250),y=(90, 120)
            #Y 4th iteration: x=(161,250),y=(150,200)

            #Y 1st iteration: x=(2, 99),y=(10, 50)
            #Y 2nd iteration: x=(51,99) y=(135,160)
            #Y 3rd iteration: x=(51,99),y=(90,120)
            #Y 4th iteration: x=(51,89),y=(150, 200)

            #Y 1st iteration: x=(200,300),y=(10,50)
            #Y 2nd iteration: x=(200,300),y=(135,160)
            #Y 3rd iteration: x=(200,300),y=(90,120)
            #Y 4th iteration: x=(200,300),y=(150, 200)

            #Y 1st iteration: x=(50,100),y=(10,50)
            #Y 2nd iteration: x=(51,100),y=(135,160)
            #Y 3rd iteration: x=(51,100),y=(90,120)
            #Y 4th iteration: x=(51,89),y=(150,200)
            if x[1] < y[0] or x[0] > y[1]:
                continue
            else:
                if x[0] >= y[0] and x[1] <= y[1]:
                    break
                elif x[0] >= y[0]:
                    x = (y[1]+1,x[1])#x=(161,250),(201,250),(201,300),(51,100)
                elif x[1] <= y[1]:
                    x = (x[0],y[0]-1)#x=(51,89),(51,100),(51,89)
                else:
                    ranges.append((x[0],y[0]-1))#range [(201,250),(2,9)]
                    x = (y[1]+1,x[1])#x=(51,99)
        ranges.append(x)#range=[(201,250),(2,9),(51,89),(201,300),(51,89)]
        sorted_result = sorted(ranges, key=lambda x:x[0])#sorted_result = [(2,9),(51,89),(51,89),(201,250),(201,300)]
    return sorted_result

def eliminate_excluded_ranges(original_id_ranges, excluded_id_ranges):
    sorted_result = my_sorted_function(original_id_ranges, excluded_id_ranges)
    #sorted_result=[(2,9),(51,89),(51,89),(201,250),(201,300)]

    final_result = [sorted_result[0]]#[(2,9),(51,89),(201,300)]
    # sorted_result[1:]=[(51,89),(51,89),(201,250),(201,300)]]
    for i in sorted_result[1:]:
        #I 1st iteration i=(51,89)
        #I 2nd iteration i=(51,89)
        #I 3rd iteration i=(201,250)
        #I 4th iteration i=(201,300)
        last_range = final_result[-1]#(2,9),(51,89),(51,89),(201,250)
        if i[0] <= last_range[1]:
            merge_range = (last_range[0],max(i[1],last_range[1]))#(51,max(89,89))=>(51,89),(201,max(300,250))=>(201,300)
            final_result[-1] = merge_range
        else:
            final_result.append(i)#[(2,9),(51,89),(201,250)]
    return final_result


original_id_ranges = [(150, 250), (2, 99), (200, 300), (50, 100)]
excluded_id_ranges = [(10, 50), (135, 160), (90, 120), (150, 200)]
filtered_result = eliminate_excluded_ranges(original_id_ranges, excluded_id_ranges)
#filtered_result = [(2,9),(51,89),(201,300)]
print(filtered_result)#[(2,9),(51,89),(201,300)]