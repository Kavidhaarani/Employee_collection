from collections import defaultdict


EMPLOYEE_DATA = [
    {'EmployeeID': 'E02001', 'Name': 'Karthika', 'Department': 'IT', 'Gender': 'Female'},
    {'EmployeeID': 'E02002', 'Name': 'Selvakumar', 'Department': 'HR', 'Gender': 'Male'},
    {'EmployeeID': 'E02003', 'Name': 'Uma', 'Department': 'Finance', 'Gender': 'Female'},
    {'EmployeeID': 'E02004', 'Name': 'Hafil', 'Department': 'IT', 'Gender': 'Male'},
    
]


collections = {}


def createCollection(p_collection_name):
    collections[p_collection_name] = []
    print(f"Collection '{p_collection_name}' created.")


def indexData(p_collection_name, p_exclude_column):
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' does not exist.")
        return
    for record in EMPLOYEE_DATA:
        indexed_record = {key: value for key, value in record.items() if key != p_exclude_column}
        collections[p_collection_name].append(indexed_record)
    print(f"Data indexed into '{p_collection_name}', excluding '{p_exclude_column}'.")


def searchByColumn(p_collection_name, p_column_name, p_column_value):
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' does not exist.")
        return
    results = [record for record in collections[p_collection_name] if record.get(p_column_name) == p_column_value]
    print(f"Search results in '{p_collection_name}' for {p_column_name}='{p_column_value}':")
    for result in results:
        print(result)
    return results


def getEmpCount(p_collection_name):
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' does not exist.")
        return
    count = len(collections[p_collection_name])
    print(f"Employee count in '{p_collection_name}': {count}")
    return count


def delEmpById(p_collection_name, p_employee_id):
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' does not exist.")
        return
    collections[p_collection_name] = [record for record in collections[p_collection_name] if record.get('EmployeeID') != p_employee_id]
    print(f"Employee '{p_employee_id}' deleted from '{p_collection_name}'.")


def getDepFacet(p_collection_name):
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' does not exist.")
        return
    department_count = defaultdict(int)
    for record in collections[p_collection_name]:
        department_count[record.get('Department', 'Unknown')] += 1
    print(f"Department facet for '{p_collection_name}':")
    for department, count in department_count.items():
        print(f"{department}: {count}")
    return department_count

v_nameCollection = 'Kavi'
v_phoneCollection = '1234'


createCollection(v_nameCollection)
createCollection(v_phoneCollection)

getEmpCount(v_nameCollection)

indexData(v_nameCollection, 'Department')
indexData(v_phoneCollection, 'Gender')

delEmpById(v_nameCollection, 'E02003')

getEmpCount(v_nameCollection)

searchByColumn(v_nameCollection, 'Department', 'IT')
searchByColumn(v_nameCollection, 'Gender', 'Female')
searchByColumn(v_phoneCollection, 'Department', 'IT')

getDepFacet(v_nameCollection)
getDepFacet(v_phoneCollection)
