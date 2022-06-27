import json
import os



def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """
    with open('students_database.json','r') as f:
        loaded_dict = json.load(f)
    return [loaded_dict[id][0] for id in loaded_dict.keys()  if course_name in loaded_dict[id][1]]



def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    with open('students_database.json','r') as f:
        loaded_dict = json.load(f)
    list_courses=[]
    for id in loaded_dict.keys():
        list_courses=list(set(list_courses) | set(loaded_dict[id][1]))
    list_courses.sort()
    dictionary_courses={course_name:names_of_registered_students(input_json_path,course_name).len() for course_name in list_courses}
    with open('output_file_path.json','w') as f:
        json.dump(dictionary_courses,f,indent=1)



def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    list_lecturers=[]
    for file in os.listdir(json_directory_path):
        if file.endswith("json"):
            with open('students_database.json','r') as f:
                loaded_dict = json.load(f)
            for id in loaded_dict.keys():
                list_lecturers=list(set(list_lecturers) | set(loaded_dict[id][1]))
    list_lecturers.sort()

    dictionary_lecturers={lecturer:[] for lecturer in list_lecturers}

    for file in os.listdir(json_directory_path):
        if file.endswith("json"):
            with open('students_database.json','r') as f:
                loaded_dict = json.load(f)
            for id in loaded_dict.keys():
                for lecturer in loaded_dict[id][1]:
                    dictionary_lecturers[lecturer]=list(set(dictionary_lecturers[lecturer]) | set(loaded_dict[id][0]))
                    
    with open('output_json_path.json','w') as f:
        json.dump(dictionary_lecturers,f,indent=1)