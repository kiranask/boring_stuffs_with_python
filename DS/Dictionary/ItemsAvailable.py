items = [{'mobile':'Onplus', 'tv':'TCL'}, {'table':'Wooden'},{'mobile':'Samsung', 'tv':'Sam'}]
available_items = []
a_item = {}
t_item = {}
ta_item = {}

for item in items:
    if 'mobile' in item:

        if 'mobile' not in a_item:
            a_item['mobile'] = [item['mobile']]
        else:
            a_item['mobile'].append(item['mobile'])

    if 'tv' in item :
        if 'tv' not  in t_item:
            t_item['tv'] = [item['tv']]
        else:
             t_item['tv'].append(item['tv'])


    if 'table' in item:
        if 'table' not in ta_item:
            ta_item['table'] = [item['table']]
        else:
            ta_item['table'].append(item['table'])


available_items.append(a_item)
available_items.append(t_item)
available_items.append(ta_item)

print(available_items)