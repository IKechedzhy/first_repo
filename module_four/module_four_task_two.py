def get_cats_info(path):

    list_of_cats = []

    try:

        with open(path, 'r') as fh:
    
            for line in fh:
                lists_with_info = line.strip().split(",")
                cats_info = {
                    "id": lists_with_info[0],
                    "name": lists_with_info[1],
                    "age": int(lists_with_info[2])
                    }
                list_of_cats.append(cats_info)
                
        return list_of_cats
            
    except Exception as warning:
        print(f"Помилка: {warning} ")

result = get_cats_info("D:\MY_REPO\\first_repo\module_four\\task_two.txt")
print(result)